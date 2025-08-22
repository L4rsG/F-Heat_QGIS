import sys
from pathlib import Path
import pandas as pd

from adjust_files import Buildings_adj


def test_extract_year():
    assert Buildings_adj.extract_year('2023-07-17') == 2023
    import numpy as np
    assert (Buildings_adj.extract_year(None) != Buildings_adj.extract_year(None))  # returns nan
