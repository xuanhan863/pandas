from pandas import *
import pandas.util.testing as tm
import random
import numpy as np

# didn't add to namespace until later
try:
    from pandas.core.index import MultiIndex
except ImportError:
    pass
