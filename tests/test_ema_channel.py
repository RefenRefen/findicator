import pandas as pd
from findicator import ema_channel

def test_ema_channel():
    close = pd.Series([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

    # Test ATR version
    result_atr = ema_channel(close, use_atr=True)

    assert 'ema' in result_atr.columns
    assert 'upper_1atr' in result_atr.columns
    assert 'lower_1atr' in result_atr.columns

    # Test coefficient version
    result_coeff = ema_channel(close, use_atr=False, coeff=0.05)

    assert 'ema' in result_coeff.columns
    assert 'upper' in result_coeff.columns
    assert 'lower' in result_coeff.columns

    # Test plain EMA (no bands)
    result_plain = ema_channel(close, use_atr=False, coeff=0.0)
    assert list(result_plain.columns) == ['ema']

    print(result_atr.tail())
    print(result_coeff.tail())
    print(result_plain.tail())
