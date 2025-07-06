import pandas as pd
import numpy as np
from findicator import macd  # replace with your module name

def test_macd_with_histogram():
    close = pd.Series([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

    macd_line, signal_line, histogram = macd(close)

    assert isinstance(macd_line, pd.Series)
    assert isinstance(signal_line, pd.Series)
    assert isinstance(histogram, pd.Series)

    # Length checks
    assert len(macd_line) == len(close)
    assert len(signal_line) == len(close)
    assert len(histogram) == len(close)

    # Check that the first value matches the math: fast EMA and slow EMA are equal at t=0
    assert np.isclose(macd_line.iloc[0], 0.0)

    # Final values should be finite numbers
    assert np.isfinite(macd_line.iloc[-1])
    assert np.isfinite(signal_line.iloc[-1])
    assert np.isfinite(histogram.iloc[-1])

    # Histogram = macd_line - signal_line
    np.testing.assert_allclose(
        histogram[-5:],
        macd_line[-5:] - signal_line[-5:],
        rtol=1e-5, atol=1e-8
    )
