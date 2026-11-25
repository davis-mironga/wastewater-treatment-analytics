# Analysis Plan
Written before any analysis of results. Changes are recorded at the bottom.

## Data
UCI Water Treatment Plant (Poch, 1993). 527 daily records, 1990-91, one urban plant.
Used for a methods demonstration, not as evidence about any Kenyan facility.

## Q1: Variation across stages
- Variables: pH, BOD (DBO), COD (DQO), suspended solids (SS) at -E, -P, -D, -S.
- Summarise with median and IQR (data are expected to be skewed). Show distributions as boxplots.
- Sort by `date_parsed` before any time-based plot.

## Q2: Removal efficiency
- Definition: (in - out) / in × 100.
- Overall: BOD (DBO-E to DBO-S), COD (DQO-E to DQO-S), SS (SS-E to SS-S).
- Use only rows where both values are present (n reported for each).
- No imputation. Missing values are excluded per calculation and counted.
- Exclude rows where the inlet is zero.
- Validation: recompute the RD- columns and compare. Agreement = within 1 percentage point. Mismatches are listed and investigated, not deleted.
- Report median removal with a bootstrap 95% confidence interval.
- Inlet vs outlet comparison: Wilcoxon signed-rank test, with effect size.

## Q3: Unusual patterns
- Two methods applied to effluent BOD, COD and SS:
  1. Robust z-score (median/MAD), flag |z| > 3.5.
  2. IQR rule, flag values beyond 1.5 × IQR.
- A day is "flagged" only if both methods agree.
- Flags are called statistical anomalies, never pollution incidents.
- Optional check: compare flags with the documented operating-state classes in the `.names` file.

## Known limitations
- One plant, 1990-91, non-continuous daily records.
- No units in the dictionary (mg/L assumed, unverified).
- Observations are sequential, so not fully independent.
- Original purpose was fault classification, not compliance.

## Change log
(Record any change to this plan here, with date and reason.)
