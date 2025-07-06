import pandas as pd
import numpy as np
from findicator import impulse_system  
def test_impulse_system():
    close = pd.Series([10, 11, 12, 13, 14, 13, 12, 11, 12, 13, 14, 15])

    impulse = impulse_system(close)

    assert isinstance(impulse, pd.Series)
    assert len(impulse) == len(close)

    # Should contain only -1, 0, or 1
    assert impulse.isin([-1, 0, 1]).all()

    # First few values may be neutral due to diff()
    assert impulse.iloc[0] == 0

    # Spot-check: positive slope => should see +1 somewhere
    assert (impulse == 1).any()

    # Spot-check: negative slope => should see -1 somewhere
    assert (impulse == -1).any()

    print(impulse)
