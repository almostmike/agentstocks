#!/usr/bin/env python3
"""Build the public end-of-day market snapshot from the latest trade ledger."""

from __future__ import annotations

import json
import math
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
LEDGER_PATH = ROOT / "data" / "codex.json"
SNAPSHOT_PATH = ROOT / "data" / "market.json"
HISTORY_PATH = ROOT / "data" / "market-history.json"
STARTING_CAPITAL = 1000.0
PROVISIONAL_SPY_RATIONALE_TEXT = (
    "The SPY field is temporarily the July 10 adjusted close and will be replaced "
    "with the official July 13 adjusted close when available."
)
FINAL_SPY_RATIONALE_TEXT = (
    "The SPY baseline has been finalized to the official July 13 adjusted close."
)


def read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def finite_number(value: Any, label: str) -> float:
    number = float(value)
    if not math.isfinite(number) or number < 0:
        raise ValueError(f"{label} must be a finite non-negative number")
    return number


def latest_ledger_state(ledger: list[dict[str, Any]]) -> dict[str, Any]:
    if not ledger:
        raise ValueError("data/codex.json has no trading session")
    state = ledger[-1]
    if not state.get("date"):
        raise ValueError("latest ledger entry has no date")
    if "cash" not in state or "positions" not in state:
        raise ValueError("latest ledger entry is missing cash or positions")
    return state


def download_adjusted_closes(
    tickers: list[str], start_date: str
) -> dict[str, dict[str, float]]:
    import yfinance as yf

    start = date.fromisoformat(start_date) - timedelta(days=7)
    end = datetime.now(timezone.utc).date() + timedelta(days=1)
    raw = yf.download(
        tickers=tickers,
        start=start.isoformat(),
        end=end.isoformat(),
        interval="1d",
        auto_adjust=True,
        group_by="ticker",
        threads=False,
        progress=False,
        timeout=30,
    )
    if raw is None or raw.empty:
        raise RuntimeError("market-data download returned no rows")

    closes: dict[str, dict[str, float]] = {}
    for ticker in tickers:
        try:
            series = raw[ticker]["Close"] if len(tickers) > 1 else raw["Close"]
        except (KeyError, TypeError) as exc:
            raise RuntimeError(f"missing adjusted close series for {ticker}") from exc
        cleaned = series.dropna()
        if cleaned.empty:
            raise RuntimeError(f"adjusted close series for {ticker} is empty")
        closes[ticker] = {
            index.strftime("%Y-%m-%d"): finite_number(value, f"{ticker} close")
            for index, value in cleaned.items()
        }
    return closes


def latest_common_market_date(closes: dict[str, dict[str, float]]) -> str:
    common = set.intersection(*(set(series) for series in closes.values()))
    if not common:
        raise RuntimeError("symbols have no common completed trading date")
    return max(common)


def finalize_provisional_spy(
    ledger: list[dict[str, Any]], market_date: str, adjusted_close: float
) -> bool:
    changed = False
    for entry in ledger:
        status = str(entry.get("spy_close_status", ""))
        if entry.get("date") == market_date and status.startswith("PROVISIONAL"):
            entry["spy_close"] = round(adjusted_close, 4)
            entry["spy_close_date"] = market_date
            entry["spy_close_status"] = "FINAL: automated adjusted close"
            if isinstance(entry.get("rationale"), str):
                entry["rationale"] = entry["rationale"].replace(
                    PROVISIONAL_SPY_RATIONALE_TEXT,
                    FINAL_SPY_RATIONALE_TEXT,
                )
            entry.pop("spy_live_at_check", None)
            changed = True
    return changed


def build_snapshot(
    state: dict[str, Any],
    closes: dict[str, dict[str, float]],
    market_date: str,
    inception_spy: float,
) -> tuple[dict[str, Any], dict[str, Any]]:
    cash = finite_number(state["cash"], "cash")
    positions = []
    equity_value = 0.0
    for item in state["positions"]:
        ticker = str(item["ticker"]).upper()
        shares = finite_number(item["shares"], f"{ticker} shares")
        price = closes[ticker][market_date]
        value = shares * price
        equity_value += value
        positions.append(
            {
                "ticker": ticker,
                "shares": shares,
                "avg_cost": round(finite_number(item["avg_cost"], f"{ticker} cost"), 4),
                "price": round(price, 4),
                "value": round(value, 2),
            }
        )

    account_value = cash + equity_value
    spy_close = closes["SPY"][market_date]
    account_return = account_value / STARTING_CAPITAL - 1
    spy_return = spy_close / inception_spy - 1
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    snapshot = {
        "market_date": market_date,
        "generated_at": generated_at,
        "price_type": "split-and-distribution-adjusted closing prices",
        "source": "Yahoo Finance via yfinance",
        "source_status": "unofficial display feed; not used for order execution",
        "portfolio": {
            "cash": round(cash, 2),
            "equity_value": round(equity_value, 2),
            "account_value": round(account_value, 2),
            "return_pct": round(account_return * 100, 6),
        },
        "benchmark": {
            "symbol": "SPY",
            "adjusted_close": round(spy_close, 4),
            "inception_adjusted_close": round(inception_spy, 4),
            "return_pct": round(spy_return * 100, 6),
        },
        "positions": positions,
    }
    history_row = {
        "date": market_date,
        "account_value": round(account_value, 2),
        "spy_adjusted_close": round(spy_close, 4),
        "account_return_pct": round(account_return * 100, 6),
        "spy_return_pct": round(spy_return * 100, 6),
    }
    return snapshot, history_row


def main() -> None:
    ledger = read_json(LEDGER_PATH, [])
    state = latest_ledger_state(ledger)
    inception_date = str(ledger[0]["date"])
    symbols = sorted({str(item["ticker"]).upper() for item in state["positions"]})
    tickers = symbols + ["SPY"]
    closes = download_adjusted_closes(tickers, inception_date)
    market_date = latest_common_market_date(closes)
    now_et = datetime.now(ZoneInfo("America/New_York"))
    if market_date == now_et.date().isoformat() and now_et.time() < time(16, 15):
        raise RuntimeError("current U.S. trading session has not completed")
    if market_date < inception_date:
        raise RuntimeError(
            f"latest completed market date {market_date} predates inception {inception_date}"
        )
    if inception_date not in closes["SPY"]:
        raise RuntimeError(f"SPY has no adjusted close for inception date {inception_date}")

    inception_spy = closes["SPY"][inception_date]
    snapshot, history_row = build_snapshot(
        state, closes, market_date, inception_spy
    )
    history = read_json(HISTORY_PATH, [])
    history = [row for row in history if row.get("date") != market_date]
    history.append(history_row)
    history.sort(key=lambda row: row["date"])

    write_json(SNAPSHOT_PATH, snapshot)
    write_json(HISTORY_PATH, history)
    if finalize_provisional_spy(ledger, market_date, closes["SPY"][market_date]):
        write_json(LEDGER_PATH, ledger)
    print(
        f"Updated {market_date}: account ${snapshot['portfolio']['account_value']:.2f}; "
        f"SPY {snapshot['benchmark']['adjusted_close']:.4f}"
    )


if __name__ == "__main__":
    main()
