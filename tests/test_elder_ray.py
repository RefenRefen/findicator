import pandas as pd
import numpy as np
from findicator import elder_ray  # Replace with your actual module name

def test_elder_ray():
    high = pd.Series([12, 13, 14, 15, 16])
    low = pd.Series([10, 11, 12, 13, 14])
    close = pd.Series([11, 12, 13, 14, 15])

    bull, bear = elder_ray(high, low, close)

    assert isinstance(bull, pd.Series)
    assert isinstance(bear, pd.Series)
    assert len(bull) == len(close)
    assert len(bear) == len(close)
