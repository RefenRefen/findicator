from findicator import stochastic_oscillator  
import pandas as pd


def test_stochastic_oscillator():
    high = pd.Series([14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27])
    low = pd.Series([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])
    close = pd.Series([11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])

    percent_k, percent_d = stochastic_oscillator(high, low, close)

    assert isinstance(percent_k, pd.Series)
    assert isinstance(percent_d, pd.Series)
    assert len(percent_k) == len(close)
    assert len(percent_d) == len(close)
