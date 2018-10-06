import numpy as np
import pandas as pd
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

btc = web.get_data_yahoo('BTC-USD', start=datetime.datetime(2014,1,1), end=datetime.datetime(2019,1,1))

btc['PctChangeVolume'] = btc['Volume'].pct_change()
btc['LogReturnVolume'] = np.log(1. + btc['PctChangeVolume'])

plt.plot(btc['LogReturnVolume'].tail(1400))
plt.show()

