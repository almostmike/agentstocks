# Device recovery and daily operation

This file contains the non-secret setup needed to resume the `Agentic` trading
experiment on a replacement Windows computer. It intentionally contains no
credentials, OAuth tokens, full account numbers, or raw broker responses.

## Authoritative sources

- Public repository: `https://github.com/almostmike/agentstocks`
- Robinhood MCP endpoint: `https://agent.robinhood.com/mcp/trading`
- Account to use: nickname `Agentic`, masked ending `3608`
- Strategy and authority: `AGENTS.md` and `STRATEGY.md`
- Scheduled-run prompt: `daily-kickoff.txt`
- Public transaction/cash-event ledger: `data/codex.json`
- Detailed decision record: `trade-log-codex.md`

Only the dedicated `Agentic` account may be written to the public repository.
Never publish information from another Robinhood account.

## Restore the repository

Clone a fresh checkout rather than relying on a OneDrive file snapshot:

```powershell
git clone https://github.com/almostmike/agentstocks.git agentstocks-live
cd agentstocks-live
```

Before every trading run:

```powershell
git pull --rebase
git status --short --branch
```

## Restore Robinhood MCP

The Codex desktop app and Codex CLI share MCP configuration. If the desktop UI
does not offer **Streamable HTTP**, locate the bundled `codex.exe` and run:

```powershell
& "PATH_TO_CODEX_EXE" mcp add robinhood --url "https://agent.robinhood.com/mcp/trading"
& "PATH_TO_CODEX_EXE" mcp login robinhood
& "PATH_TO_CODEX_EXE" mcp list
```

Complete OAuth in Robinhood's browser flow, restart the Codex desktop app, and
confirm that `robinhood` is enabled. Never paste a token or authorization code
into the repository or a prompt.

## Recovery audit before trading

The first run on a new device must be read-only:

1. Resolve the account by nickname `Agentic`; halt if ambiguous.
2. Read account type/status, cash, settled buying power, pending deposits,
   unsettled funds, positions, sellable quantities, restrictions, and all open
   equity/option/crypto orders.
3. Compare shares, costs, and cash with the latest entry in `data/codex.json` and
   `trade-log-codex.md`.
4. Explain every difference using verified orders or cash events. Never infer a
   trade through an unexplained mismatch.
5. Only after reconciliation, resume the daily process in `AGENTS.md`.

## Daily schedule

Run at **10:15 AM America/Los_Angeles every weekday** using `gpt-6-astra` with
high reasoning. Friday runs also perform the strategy's weekly review. The first
trading day of each month includes the monthly attribution, turnover, drawdown,
forecast-hit-rate, and process-compliance review. The computer must be on and the
Codex desktop app running.

Use this durable scheduled prompt:

> Work in the `agentstocks-live` repository as GPT-6 Astra CODEX. Read and follow
> `AGENTS.md`, the current committed `STRATEGY.md`, `DEVICE-RECOVERY.md`, and
> `daily-kickoff.txt`. Pull/rebase first.
> Resolve only the Robinhood account nicknamed `Agentic`; never publish or use
> another account. Reconcile account state, settled cash, positions, restrictions,
> and orders against the public ledger. Research current primary evidence and
> make a mandate-compliant hold/buy/sell/trim decision. Submit an equity order
> only when its exact broker preview matches the documented decision and every
> constraint. Verify afterward. Record and publish only executed trades or
> verified broker cash events in `data/codex.json`, with the detailed decision in
> `trade-log-codex.md`; routine price-only changes belong to the automated market
> workflow. On Fridays, include the weekly milestone, valuation, earnings, and
> watchlist review. On the first trading day of each month, include the monthly
> attribution and process review. Note in new operational updates that the
> scheduled manager is GPT-6 Astra effective September 23, 2026, without
> rewriting historical entries. Never expose a full account number, credentials,
> OAuth data, or raw connector responses.

## Publishing checks

Before publishing a trade-changing session:

```powershell
python -m unittest discover -s tests
git diff --check
git status --short --branch
```

Stage only the files permitted by `AGENTS.md`, pull/rebase if the remote changed,
and never force-push. If publication fails after a verified broker action, keep
the local record and reconcile before any retry; never duplicate an order.
