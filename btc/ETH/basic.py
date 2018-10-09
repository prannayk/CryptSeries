import numpy as np
import pandas as pd
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

eth = web.get_data_yahoo('ETH-USD', start=datetime.datetime(2014,1,1), end=datetime.datetime(2019,1,1))

eth['PctChangeVolume'] = eth['Volume'].pct_change()
eth['LogReturnVolume'] = np.log(1. + eth['PctChangeVolume'])

plt.plot(eth['LogReturnVolume'].tail(1400))
plt.show()
