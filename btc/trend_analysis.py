import numpy as np
import pandas as pd
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

btc = web.get_data_yahoo('BTC-USD', start=datetime.datetime(2014,1,1), end=datetime.datetime(2019,1,1))

# btc['Open']
result = adfuller(btc['Open'].tail(1000))
print(result[0])         # computes the ADF statistic
for _, val in enumerate(result[4]):
    print(val, result[4][val])

btc['ChangeOpen'] = btc['Open'].pct_change()
result = adfuller(btc['ChangeOpen'].tail(1000))
print(result[0])         # computes the ADF statistic
for _, val in enumerate(result[4]):
    print(val, result[4][val])

# This code proves that the time series of bitcoin data had a first order trend which could be removed easily


