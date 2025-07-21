from findicator import force_index  
import pandas as pd


def test_force_index():
    close = pd.Series([10, 10.5, 11, 10.8, 11.2])
    volume = pd.Series([1000, 1100, 1050, 1200, 1150])

    fi = force_index(close, volume)

    assert isinstance(fi, pd.Series)
    assert len(fi) == len(close)
    assert not fi.isnull().all()
