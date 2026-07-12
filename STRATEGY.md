# 5.6 Sol CODEX strategy — Quality, Revision, Momentum

Version 1.0 — adopted 2026-07-12, before the first live trade

## Aim and honest premise

The objective is to compound the account faster than SPY total return. There is
no promise that this will happen. The hurdle is severe: 79% of active U.S.
large-cap funds underperformed the S&P 500 in 2025, and only 30% of S&P 500
stocks beat the index that year. A portfolio that resembles the index is
therefore unlikely to produce meaningful positive active return. This strategy
accepts measured concentration and high active share in exchange for a real
chance to outperform.

The approach is **Quality, Revision, Momentum (QRM)**: own four to six liquid
companies whose business results are improving, whose price trend confirms the
fundamental evidence, and whose valuation still offers favorable asymmetry.
Hold winners while the evidence persists, remove broken theses quickly, and
avoid trading merely because a daily run occurred.

## Where the potential edge comes from

1. **Fundamental underreaction.** Strong earnings are more useful when revenue
   and forward guidance confirm them. Markets and analyst forecasts can adjust
   gradually to new information.
2. **Medium-term momentum.** Relative winners have historically tended to keep
   winning over intermediate horizons. Price strength is confirmation, not a
   substitute for understanding the company.
3. **Business quality.** Profitability, durable growth, balance-sheet safety,
   and disciplined capital allocation help distinguish persistent winners from
   speculative momentum.
4. **Concentration with guardrails.** Outperformance requires weights that
   differ from SPY. Four to six positions are concentrated enough to matter but
   diversified enough that one ordinary mistake should not ruin the account.
5. **Low friction.** Expected holding periods are measured in months. Limiting
   turnover reduces spread, slippage, settlement complications, and behavioral
   mistakes.

This is a long-only stock-selection strategy, not a day-trading strategy and
not a forecast of tomorrow's index move.

## Eligible universe

A new position must be:

- a U.S.-listed common stock with market capitalization normally above $10
  billion;
- priced above $5 with ample trading liquidity;
- supported by current company filings, investor materials, and reliable price
  data;
- outside every standing exclusion in `AGENTS.md` and not a disguised proxy for
  an excluded group; and
- profitable on an operating basis or positive in trailing free cash flow.

ADRs, recent IPOs, pre-profit companies, narrow thematic ETFs, leveraged or
inverse products, and binary clinical-stage or litigation trades are excluded
by default. An exception requires a prospective strategy amendment before any
order, not a one-off improvisation in the trade log.

## The QRM score

Every purchase needs a written 0–100 score. The score is a decision checklist,
not a claim of mathematical precision.

| Pillar | Weight | Evidence required |
|---|---:|---|
| Price and relative momentum | 30 | Positive 6- and 12-month return relative to SPY (the 12-month measure skips the most recent month); normally above rising 50- and 200-day averages; healthy reaction to material news rather than a one-day spike. |
| Fundamental revisions | 25 | Latest revenue, earnings, margins, backlog or other relevant operating metric versus prior expectations; direction of management guidance; subsequent estimate direction where reliable data are available. |
| Business quality | 20 | Positive cash generation, durable or improving margins, sensible leverage, limited dilution, and credible capital allocation. Sector-appropriate measures may replace generic ones but must be stated. |
| Valuation and asymmetry | 15 | A 6–12 month bear/base/bull valuation using an appropriate multiple or cash-flow framework; base-case upside divided by bear-case downside should normally be at least 1.5. |
| Catalyst and durability | 10 | A concrete reason the market may continue revising expectations, plus evidence the opportunity can last beyond a few trading days. |

New positions require at least **70/100**, no zero-score pillar, and a clearly
stated thesis, bear case, invalidation condition, and maximum entry price. A
score above 70 is permission to consider a trade, not an obligation to buy.

## Portfolio construction

- Normal portfolio: **4–6 stocks**.
- Normal initial weight: **15–22%** of account value.
- Maximum at purchase: **25%**. Trim if appreciation takes a position above
  **30%**, unless an order-size minimum makes the trim immaterial.
- Maximum combined weight in one GICS sector: **40%** at purchase.
- Never exceed the mandate's ten-position hard ceiling.
- Fractional shares and notional orders may be used if the connector supports
  them and the preview is exact.
- Do not average down merely because a price fell. Adding requires fresh
  evidence, a refreshed score of at least 70, and compliance with the weight
  limits.

Cash is an output, not a permanent allocation. When SPY is above its 200-day
moving average and qualifying ideas exist, the target is 85–100% invested. When
SPY is below its 200-day average and that average is falling, normal exposure is
50–75%. Exposure may be lower when no stock qualifies. This regime rule is a
position-sizing modifier; it does not authorize shorting, leverage, or inverse
funds.

## Entry rules

1. Complete the score and thesis using information available before the order.
2. Prefer entries after a fundamental catalyst has been reported and absorbed;
   do not initiate within two trading days before scheduled earnings.
3. Trade only during regular, liquid market hours. Prefer a limit order when
   supported. Do not chase a price more than 2% above the recorded decision
   price or above the thesis's maximum entry price.
4. Confirm settled buying power, the resulting weight and position count, the
   exclusion list, and the exact order preview before submission.
5. Scale in only when doing so is part of the original plan. An incomplete fill
   is not a reason to loosen the price limit.

## Hold, review, and exit rules

Positions are reviewed daily for new facts and formally rescored each weekend.
The default holding period is roughly one to six months.

Sell or reduce when the first applicable rule is met:

1. **Thesis break:** guidance is cut, the key operating metric deteriorates,
   the original catalyst fails, accounting or governance risk emerges, or the
   security becomes prohibited. Exit promptly once the account and order can
   be verified.
2. **Trend failure:** two consecutive closes below the 50-day average **and**
   negative 20-trading-day relative return versus SPY. This avoids reacting to
   one noisy session while refusing to normalize persistent weakness.
3. **Loss discipline:** a 10% closing loss from average cost forces a documented
   re-underwrite. A 12% closing loss is a default full exit at the next liquid
   opportunity. Any exception must rest on new public fundamental evidence and
   be documented before the order decision; hope and a lower price are not new
   evidence.
4. **Time stop:** after eight weeks, replace a position that has lagged SPY
   since entry and has no positive fundamental revision.
5. **Better use of capital:** at the weekly review, replace a holding only when
   an eligible candidate scores at least 10 points higher. This hurdle limits
   churn.
6. **Concentration:** trim above 30% or when a sector exceeds 45% because of
   appreciation.

There is no automatic profit target. Winners are allowed to compound. Before a
subsequent earnings report, reassess the event risk three trading days in
advance; a position above 20% should normally be reduced to 15–20% unless the
log explicitly supports carrying the larger exposure.

## Cadence

- **Daily:** reconcile the broker account, inspect holdings and material news,
  enforce exits, and evaluate only genuinely actionable candidates.
- **Weekend:** refresh the full watchlist, QRM scores, earnings calendar, and
  portfolio regime.
- **Monthly:** review attribution, turnover, drawdown, and whether the recorded
  decisions followed this policy. Strategy changes are not made just because a
  few trades lost.

Same-day round trips are prohibited as normal practice. Settlement status is
authoritative; a good idea never justifies spending unavailable cash.

## Measurement and falsifiability

The experiment begins with the first live session. Capture account net asset
value and SPY's split- and distribution-adjusted closing value on the same
inception date. Thereafter:

```text
account return = current NAV / inception NAV - 1
SPY total return = current adjusted SPY value / inception adjusted SPY value - 1
active return = account return - SPY total return
```

Use broker NAV after settled and pending orders are reconciled. If external cash
flows ever occur, report them and switch the account calculation to a
time-weighted return. The existing `spy_close` JSON field stores the adjusted
SPY value used for total-return measurement, despite its short field name.

Report active return, account and SPY drawdowns, turnover, win rate, average
winner/loser, and attribution by position. Success means higher cumulative
total return than SPY over the declared experiment horizon—not one good trade,
lower volatility, or a conveniently selected subperiod.

## Governance

This version is locked before the first trade to prevent hindsight rewriting.
It may be amended prospectively when evidence or operating constraints change.
Every amendment must be dated, explained in the public log, and committed before
it governs a trade. No backtest or historical result is claimed for this exact
implementation.

## Evidence base

- S&P Dow Jones Indices, [SPIVA U.S. Year-End 2025](https://www.spglobal.com/spdji/en/spiva/article/spiva-us/).
- Jegadeesh and Titman, [Profitability of Momentum Strategies](https://www.nber.org/papers/w7159), NBER Working Paper 7159.
- Asness, Frazzini, and Pedersen, [Quality Minus Junk](https://www.aqr.com/-/media/AQR/Documents/Insights/Working-Papers/Quality-Minus-Junk.pdf).
- Jegadeesh and Livnat, [Post-Earnings-Announcement Drift: The Role of Revenue Surprises](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=903767).
- Chen, Narayanamoorthy, Sougiannis, and Zhou, [Analyst Underreaction and the Post-Forecast Revision Drift](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4157053).
- Moskowitz, Ooi, and Pedersen, [Time Series Momentum data and paper summary](https://www.aqr.com/Insights/Datasets/Time-Series-Momentum-Original-Paper-Data).
- Bessembinder, [Do Stocks Outperform Treasury Bills?](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2900447).

Historical evidence does not guarantee that these effects will persist or that
this implementation will beat SPY.
