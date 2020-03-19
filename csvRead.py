import numpy as sp
import matplotlib.pylab as plt
import datetime as dt
import re
import csv

import pandas as pd
import yfinance as yf
import yahoofinancials


#monthDict = {    '01':'January',
#'02':'February',
#'03':'March',
#'04':'April',
#'05':'May',
#'06':'June',
#'07':'July',
#'08':'August',
#'09':'September',
#'10':'October',
#'11':'November',
#'12':'December'
#}
#
#class Direct:
#    def __init__(self,title, desc, date, reigions):
#        self.title = title
#        self.desc = desc
#        self.date = formatDate(date)
#        self.reigions = reigions
#
#    def formatDate(self,date):
#        dArr = re.split('[\s,]+',date)
#        month = [key for key in monthDict.items() if key[1] == dArr[0]][0][0]
#        x = dt.datetime(int(dArr[2]),int(month),int(dArr[1]))
        
        
fileName = 'directListFINAL.csv'
with open(fileName,'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    next(csv_reader)
    
    for line in csv_reader:
        print(line)



#tsla_df = yf.download('TSLA',
#                      start='2019-01-01',
#                      end='2019-12-31',
#                      progress=False)
#x = tsla_df.head()
#print(x)

#ticker = yf.Ticker('TSLA')
#
#tsla_df = ticker.history(period="max")
#
#tsla_df['Close'].plot(title="TSLA's stock price")
#plt.show()


#print( sp.version.version )
#
#A = sp.array([[1,2,3],[1,2,3],[1,2,3]])
#AT = sp.transpose(A)
#plt.ion()

#t = sp.linspace(0,1,100)
#plt.plot(t, t**2)
##plt.plot(t, t**1)
#plt.show()
