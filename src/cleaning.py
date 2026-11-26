"""Cleaning functions for the UCI Water Treatment Plant data.

Rule: raw files are never modified. This module only reads them and
returns a new, tidier table.
"""
from pathlib import Path
import pandas as pd

COLS = ["date",
 "Q-E","ZN-E","PH-E","DBO-E","DQO-E","SS-E","SSV-E","SED-E","COND-E",
 "PH-P","DBO-P","SS-P","SSV-P","SED-P","COND-P",
 "PH-D","DBO-D","DQO-D","SS-D","SSV-D","SED-D","COND-D",
 "PH-S","DBO-S","DQO-S","SS-S","SSV-S","SED-S","COND-S",
 "RD-DBO-P","RD-SS-P","RD-SED-P","RD-DBO-S","RD-DQO-S",
 "RD-DBO-G","RD-DQO-G","RD-SS-G","RD-SED-G"]


def load_clean(raw_path):
    """Read the raw file and return a date-sorted table."""
    # 1. Read: no header row, '?' means missing (blank lines are skipped)
    df = pd.read_csv(raw_path, header=None, names=COLS, na_values="?")
    # 2. Remember each row's original position in the raw file
    df["file_row"] = df.index
    # 3. Turn text like 'D-1/3/90' into a real date
    df["date_parsed"] = pd.to_datetime(
        df["date"].str.replace("D-", "", regex=False), format="%d/%m/%y")
    # 4. Sort by date (the raw file is in scrambled month blocks)
    return df.sort_values("date_parsed").reset_index(drop=True)


if __name__ == "__main__":
    raw = Path("data/raw/water-treatment.data")
    out = Path("data/processed/water_treatment_clean.csv")
    df = load_clean(raw)
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out, index=False)
    print("Rows:", len(df), "| Columns:", df.shape[1])
    print("In date order:", df["date_parsed"].is_monotonic_increasing)
    print("Duplicate dates:", df["date_parsed"].duplicated().sum())
    print("Saved to", out)
