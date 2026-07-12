# agentstocks

Public ledger for a live-money AI trading experiment. 5.6 Sol CODEX manages a
$1,000 Robinhood Agentic account under hard constraints, with results benchmarked
against SPY total return.

The repository is intentionally public for transparency. It contains decisions,
positions, performance data, and reproducible rules, but never brokerage account
numbers, credentials, tokens, or raw connector responses.

## Repository layout

```text
index.html                 GitHub Pages dashboard
data/codex.json            5.6 Sol CODEX daily public records
trade-log-codex.md         5.6 Sol CODEX detailed session log
STRATEGY.md                pre-committed selection and risk policy
AGENTS.md                  standing mandate and safety constraints
daily-kickoff.txt           scheduled-run prompt
```

## Current status

- Robinhood Agentic account connection verified.
- 5.6 Sol CODEX account verified as cash-only with $1,000 and no initial positions.
- Local Git repository initialized on `main`.
- GitHub repository: <https://github.com/almostmike/agentstocks> (public).
- First trading session has not started; current records are setup-only.
- Strategy v1.0 is documented in [STRATEGY.md](STRATEGY.md) and locked before
  the first live trade.

## Connect and publish from Windows

The Codex GitHub app is connected and can inspect/manage the repository through
the app. Local `git push` is a separate authentication path and requires GitHub
CLI on this computer.

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

Each account JSON file is a flat array with one record per completed session:

```json
{
  "date": "2026-07-13",
  "account_value": 1000.00,
  "cash": 1000.00,
  "positions": [],
  "spy_close": 0.00,
  "action": "HELD",
  "rationale": "Public-ready explanation of the decision."
}
```

Account and SPY returns are calculated from the same experiment inception date.
No placeholder record is written before the first actual trading session.
