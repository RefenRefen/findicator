import pandas as pd
import numpy as np
import pytest

from findicator import atr  # Replace with the actual import path

def test_atr_basic():
    # Example data
    data = {
        "high": [10, 11, 12, 13, 14, 15],
        "low":  [ 9,  9, 10, 11, 12, 13],
        "close":[ 9.5, 10.5, 11.5, 12.5, 13.5, 14.5],
    }
    df = pd.DataFrame(data)

    # Compute manually
    prev_close = df["close"].shift(1)
    tr1 = df["high"] - df["low"]
    tr2 = (df["high"] - prev_close).abs()
    tr3 = (df["low"] - prev_close).abs()
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)

    # Use period=3 for a shorter window
    period = 3
    expected_atr = tr.rolling(window=period).mean()

    # Call your function
    result_atr = atr(df["high"], df["low"], df["close"], period=period)

    # Use pandas testing to check equal (including NaNs!)
    pd.testing.assert_series_equal(result_atr, expected_atr, check_names=False)
