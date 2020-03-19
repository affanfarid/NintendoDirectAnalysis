import pandas as pd
import yfinance as yf
import yahoofinancials
import fix_yahoo_finance as fyf

import numpy as sp
import matplotlib.pylab as plt
import datetime
#import pandas_datareader as pdr
from pandas_datareader import data as pdr
pd.core.common.is_list = pd.api.types.is_list_like

#fyf.pdr_override()
#
#goog = pdr.get_data_yahoo('NTDOY',start='2017-01-01')
#goog.head()

goog = fyf.download('NTDOY',start='2017-01-01')
goog.head()
#print(goog)
#2017-02-13
x = datetime.datetime(2017, 2, 12)
y = datetime.datetime(2017, 3, 13)

test = fyf.download(
'NTDOY', start=x, end=y
    #interval="1d"
    )
    
test.plot(kind='scatter',x='High',y='Open',color='red')
plt.show()
print(test)
#print(test.at[x,'High'])
#tsla_df = yf.download('TSLA',
#                      start='2019-01-01',
#                      end='2019-12-31',
#                      progress=False)
#x = tsla_df.head()
#print(x)

#ticker = yf.Ticker('NTDOY')
#
#tsla_df = ticker.history(period="max")
#
#tsla_df['Close'].plot(title="NTDOY's stock price")

#plt.show()




#data = yf.download(
#    "NTDOY",
#    start=x,
#    end=x#,
#    #interval="5d"
#)
#print(data)
#data = fyf.download(
#    "NTDOY",
#    start="2019-01-01",
#    end="2019-01-02",
#    #interval="5d"
#)
    
    
#type is dataframe??
#print(data.columns)

#x = pd.DataFrame(data,
#    #index=['2017-01-06', '2020-02-10'],
#    columns=['Open','Close','High','Low']
#    )
#print(x)
#print( sp.version.version )
#
#A = sp.array([[1,2,3],[1,2,3],[1,2,3]])
#AT = sp.transpose(A)
#plt.ion()

#t = sp.linspace(0,1,100)
#plt.plot(t, t**2)
##plt.plot(t, t**1)
#plt.show()
