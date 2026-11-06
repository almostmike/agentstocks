# agentstocks

New to the experiment? Read the Day 1 article:
[Can AI Predict the Future? Better Call Sol](https://www.linkedin.com/pulse/can-ai-predict-future-better-call-sol-michael-todasco-zyaic/).

Public record of a real-money AI trading experiment, **July 13–November 6, 2026**.
The user ended the experiment early after autonomous execution stopped working
in practice despite repeated requests to try, and personally liquidated the final holdings.

**Final account: $959.59 (−4.041%). SPY total-return equivalent: $979.07 (−2.092946%).**
The experiment underperformed by **1.948054 percentage points ($19.48 per $1,000)**.
The SPY comparison is frozen at November 6, 10:31:16 AM PST, shortly after liquidation,
using a consistently distribution-adjusted July 10 baseline. It is an intraday
comparison, not the November 6 closing price.

See the [final report](trade-log-codex.md#2026-11-06--experiment-ended-early-final-user-liquidation-and-benchmark-comparison)
and [reproducible closing inputs](data/closure.json).

The repository is intentionally public for transparency. It contains decisions,
positions, performance data, and reproducible rules, but never brokerage account
numbers, credentials, tokens, or raw connector responses.

## Repository layout

```text
index.html                 GitHub Pages dashboard
data/codex.json            GPT-6 Astra CODEX trade/change records
data/market.json           automated latest adjusted-close snapshot
data/market-history.json   automated daily performance series
trade-log-codex.md         GPT-6 Astra CODEX detailed session log
STRATEGY.md                pre-committed selection and risk policy
AGENTS.md                  standing mandate and safety constraints
daily-kickoff.txt           scheduled-run prompt
```

## Final status

- **Ended early November 6, 2026. No positions; $959.59 cash.** Of that, $295.10
  is unsettled sale proceeds and $664.49 is settled buying power at verification.
- Final user sales: NTAP 1.226692 shares at $171.85; CSCO 0.899082 shares at $93.75.
- Scheduled manager: GPT-6 Astra effective September 23, 2026; earlier management
  and execution history are preserved.
- Recurring review paused; automatic market marking stopped. The dashboard
  displays the frozen closing snapshot, with historical data retained.
- The failure was autonomous execution in this setup. A broker rejection or
  platform-wide policy change was not established by the closing verification.
- Strategy v1.1 and recovery/setup instructions below are historical records,
  not authorization to resume trading. Reopening requires explicit user direction.

## Connect and publish from Windows

The Codex GitHub app is connected and can inspect/manage the repository through
the app. Local `git push` is a separate authentication path and requires GitHub
CLI on this computer.

For replacement-computer recovery, Robinhood MCP restoration, the mandatory
read-only reconciliation, and the daily schedule, see
[DEVICE-RECOVERY.md](DEVICE-RECOVERY.md).

1. Open PowerShell and install GitHub CLI:

   ```powershell
   winget install --id GitHub.cli
   ```

2. Close and reopen PowerShell, then authenticate:

   ```powershell
   gh auth login
   ```

   Choose `GitHub.com`, `HTTPS`, and browser authentication. Allow `gh` to
   configure Git credentials when prompted.

3. Verify authentication:

   ```powershell
   gh auth status
   ```

4. This working folder should use the following remote:

   ```powershell
   git remote add origin https://github.com/almostmike/agentstocks.git
   ```

5. After the initial push, enable GitHub Pages at repository **Settings > Pages**,
   select **Deploy from a branch**, then choose `main` and `/ (root)`. The site
   will appear at <https://almostmike.github.io/agentstocks/>.

## Daily record schema

The account JSON is a flat array with one record per executed trade or verified
broker cash event such as a dividend, fee, deposit, or withdrawal:

```json
{
  "date": "2026-07-13",
  "account_value": 1000.00,
  "cash": 1000.00,
  "positions": [],
  "spy_close": 0.00,
  "action": "BOUGHT XYZ",
  "rationale": "Public-ready explanation of the portfolio change."
}
```

Held days do not create ledger rows; the automated market files mark the portfolio
and SPY after every completed trading day. Account and SPY returns are calculated
from the same experiment inception date.
