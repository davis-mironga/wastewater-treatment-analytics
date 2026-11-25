# Data Inventory

Source: UCI Water Treatment Plant (Poch, 1993), `water-treatment.names`.
527 daily observations, 38 numeric variables plus a date. Missing marker: `?`.

## Naming convention
Measurement + location suffix.
- Measurements: Q flow, ZN zinc, PH pH, DBO BOD, DQO COD, SS suspended
  solids, SSV volatile suspended solids, SED sediments, COND conductivity.
- Locations: -E plant input, -P primary settler input, -D secondary
  settler input, -S plant output. RD-x-P / -S / -G = performance (removal)
  at primary stage / secondary stage / whole plant.

## Known gaps in the documentation
- No units are stated for any variable (mg/L for BOD/COD/SS is an
  unverified assumption).
- RD- descriptions are ambiguous; formula (in - out)/in verified by hand
  on one row only. To be tested on all rows.
- SSV may be a percentage of SS: unconfirmed.
- No COD measurement at the primary settler input (no DQO-P).
