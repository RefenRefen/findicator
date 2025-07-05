import pandas as pd
from findicator import bollinger_bands

def test_bollinger_bands():
    data = {
        'High': [10, 11, 12, 13, 14, 15, 16],
        'Low': [9, 9.5, 10, 11, 12, 13, 14],
        'Close': [9.5, 10, 11, 12, 13, 14, 15],
    }
    df = pd.DataFrame(data)

    mb, ub, lb = bollinger_bands(df['High'], df['Low'], df['Close'], period=3, stddev_multiplier=2)

    # Check output lengths match input
    assert len(mb) == len(df)
    assert len(ub) == len(df)
    assert len(lb) == len(df)

    # Check that upper > middle > lower for non-NaNs
    valid = mb.dropna().index
    assert all((ub[valid] > mb[valid]) & (mb[valid] > lb[valid]))
