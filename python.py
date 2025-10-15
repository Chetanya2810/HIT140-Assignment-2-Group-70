#!/usr/bin/env python3
"""
analysis_assessment3.py

Reproducible analysis for HIT140 Assessment 3 (Chetanya Thukral)
- Cleans dataset1.csv and dataset2.csv
- Creates derived features and summaries
- Performs descriptive and inferential analysis
- Saves figures and output files to /results
"""

import os
import json
import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import chi2_contingency
from pathlib import Path

warnings.filterwarnings("ignore", category=UserWarning)

# ==============================
# Load and prepare datasets
# ==============================
def load_and_clean():
    # Load datasets (ensure they're in the same folder as this script)
    df1 = pd.read_csv("dataset1.csv")
    df2 = pd.read_csv("dataset2.csv")

    # Clean column names
    df1.columns = [c.strip() for c in df1.columns]
    df2.columns = [c.strip() for c in df2.columns]

    # Convert relevant columns to numeric or datetime
    time_cols = ['start_time','rat_period_start','rat_period_end','sunset_time','time']
    for col in time_cols:
        for df in [df1, df2]:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors='coerce')

    numeric_cols1 = ['bat_landing_to_food','seconds_after_rat_arrival','hours_after_sunset']
    numeric_cols2 = ['hours_after_sunset','bat_landing_number','food_availability','rat_minutes','rat_arrival_number']
    for col in numeric_cols1:
        if col in df1.columns:
            df1[col] = pd.to_numeric(df1[col], errors='coerce')
    for col in numeric_cols2:
        if col in df2.columns:
            df2[col] = pd.to_numeric(df2[col], errors='coerce')

    # Derive rats_present
    if 'seconds_after_rat_arrival' in df1.columns:
        df1['rats_present'] = np.where(df1['seconds_after_rat_arrival'] >= 0, 1, 0)

    # Clean season labels if present
    if 'season' in df1.columns:
        df1['season'] = df1['season'].astype(str).str.strip()
    if 'season' in df2.columns:
        df2['season'] = df2['season'].astype(str).str.strip()

    return df1, df2

# ==============================
# Analysis functions
# ==============================
def
