import pandas as pd
import numpy as np
from findicator import rsi  # Replace with actual import path

def test_rsi():
    close = pd.Series([44, 45, 46, 44, 43, 42, 43, 44, 45, 46, 47, 46, 45, 44, 43, 42])
    
    rsi_values = rsi(close)

    assert isinstance(rsi_values, pd.Series)
    assert len(rsi_values) == len(close)
    assert rsi_values.max() <= 100
    assert rsi_values.min() >= 0
    assert rsi_values.isnull().sum() > 0  # RSI should start with NaNs

    # Optional visual/debug check
    print(rsi_values)
