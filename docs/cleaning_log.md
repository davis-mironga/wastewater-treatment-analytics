# Cleaning Log

Every change to the data is recorded here: what, why, and row counts.
Raw files in `data/raw/` are never modified.

| # | Date | Finding / Action | Rows before | Rows after | Raw file changed? |
|---|------|------------------|-------------|------------|-------------------|
| 1 | 2026-11-25 | `water-treatment.data` has 596 lines: 527 data rows plus 69 blank lines. Each data row has 39 fields (date + 38 attributes). No duplicate dates. Blank lines are ignored at load time. | 596 lines | 527 rows | No |
| 2 | 2026-11-25 | Parsed `date` (format `D-d/m/yy`) into new column `date_parsed` in memory. 527 rows, no duplicates, range 1990-01-01 to 1991-10-30. | 527 | 527 | No |
| 3 | 2026-11-25 | Missing-value counts match the `.names` documentation for all 38 variables. | 527 | 527 | No |
| 4 | 2026-11-25 | No variable exceeds 12% missing (highest: RD-DBO-P 11.8%). No values imputed or removed. | 527 | 527 | No |
| 5 | 2026-11-25 | Documentation names the last variable `RD-SED-G` in one place and `RD-SSED-G` in another. We use `RD-SED-G`. | 527 | 527 | No |
