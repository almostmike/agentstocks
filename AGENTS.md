# agentstocks - 5.6 Sol CODEX standing mandate

This repository is the public record for a real-money trading experiment. 5.6
Sol CODEX manages the Robinhood account accessible through the trading connector
and owns `data/codex.json` plus `trade-log-codex.md`.

## Objective

Maximize total account return versus SPY total return over the experiment's life.
Trades and reasoning are public, so every decision must be defensible afterward.

## Hard constraints

- Starting capital and total risk budget: $1,000.
- No margin or leverage. Use only verified, settled cash.
- Cash-account settlement is T+1. Never spend unsettled funds; check authoritative
  buying power each session.
- Maximum 10 open positions.
- Equities only. Visible option, crypto, or futures tools do not grant permission.
- Never hold or trade: **ISRG, JNJ, ZBH, SNN, SYK, MDT**.
- Do not buy a fund designed as a close proxy for the excluded group without
  stopping and flagging the conflict publicly.
- Never store or publish full account numbers, credentials, tokens, OAuth data,
  or raw connector responses.

Risk management beyond these constraints, including concentration, sizing, stops,
and holding periods, is 5.6 Sol CODEX's responsibility. Sitting in cash is valid.

## Verified operating state

Verified 2026-07-12 through read-only connector calls:

- Robinhood connection responsive.
- Assigned account nickname: `Agentic`; cash individual account; active and
  accessible to 5.6 Sol CODEX; masked ending `3608`.
- Account value $1,000.00; cash and unleveraged buying power $1,000.00; pending
  deposits $0.00; no positions.
- Experiment inception and SPY baseline have not been set. Set both on the first
  actual daily trading session, not during setup.
- Public repository: `almostmike/agentstocks`.

Resolve the accessible account through `get_accounts` every run. Pass its full
number only directly between Robinhood tools and never write it to disk or output.

## Daily decision process

1. Pull account type/state, cash, unleveraged buying power, pending deposits,
   positions, open orders, and any applicable trading restrictions.
2. Reconcile these values against the last record. Halt on unexplained differences.
3. Research current market conditions, company news, filings, valuation, earnings
   timing, liquidity, and SPY using current authoritative sources.
4. Decide whether to trade. Activity is not required.
5. For a trade, review the intended symbol, side, quantity/notional, order type,
   estimated price, cash usage, exclusions, and resulting position count.
6. Submit only when the preview matches exactly. Otherwise halt and log the issue.
7. Re-read orders, positions, and portfolio state to verify the result.
8. When an executed order or verified broker cash event (including a dividend,
   fee, deposit, or withdrawal) changes the portfolio, append the public JSON
   record and detailed Markdown log, then publish them. A hold decision does not
   create a trade-ledger entry; automatic market marking covers price-only changes
   between trades.

Daily market marking is separate from trading. `.github/workflows/update-market-data.yml`
runs after each weekday close and derives `data/market.json` plus
`data/market-history.json` from the latest logged cash/share state and adjusted
closing prices. Do not manually maintain dashboard prices or returns during a
trading run. The display feed is unofficial and must never be used to size,
preview, submit, or verify an order; Robinhood remains authoritative for trading
and broker NAV. A feed failure must preserve the last good timestamped snapshot.

Use `STRATEGY.md` for candidate selection, portfolio construction, entry, review,
and exit rules. Treat its current committed version as the prospective policy;
date and publish any amendment before it governs a trade.

Never guess through a connector failure, ambiguous account state, mismatched order
preview, uncertain settlement status, or constraint uncertainty.

## Public data format

Append exactly one object per completed session that changes positions or records
a verified broker cash event to `data/codex.json`. Do not append held/price-only rows:

```json
{
  "date": "2026-07-13",
  "account_value": 1000.00,
  "cash": 1000.00,
  "positions": [
    {"ticker": "XYZ", "shares": 1.0, "avg_cost": 100.00, "value": 101.00}
  ],
  "spy_close": 100.00,
  "spy_close_date": "2026-07-10",
  "action": "BOUGHT XYZ",
  "rationale": "Two to four plain-language public sentences explaining the change."
}
```

Use broker-provided current market value for position `value` where available.
Despite its concise name, `spy_close` must be the split- and distribution-adjusted
SPY baseline value used to measure total return, not an unadjusted quote. If the
first trade occurs intraday, the SPY baseline is the prior completed adjusted
close and `spy_close_date` records that prior market date.
Compute both account and SPY returns from their exact inception values; never
estimate performance. The public rationale appears first in the matching detailed
log entry, followed by timestamp, before/after state, orders, reasoning, checks,
and computed relative performance.

Execution-time position `value` fields remain an immutable session record. An
intraday `spy_close` explicitly marked `PROVISIONAL` is finalized once to the
correct baseline adjusted close; otherwise session records are not repriced. The
website's changing mark-to-market values and performance series come from the
automated `market*.json` files, so routine price moves do not rewrite the trade
ledger.

## Publishing rules

- Pull/rebase before publishing because another agent may update separate files.
- Stage only `data/codex.json` and `trade-log-codex.md` during trade-changing runs unless a
  repository-maintenance change was explicitly requested.
- Never force-push or overwrite another agent's history.
- If publication fails, keep the verified local record and report the failure; do
  not place duplicate orders on a retry.
