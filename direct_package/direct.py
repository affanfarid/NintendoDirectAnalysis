import numpy as sp
import matplotlib.pylab as plt
import datetime as dt
import re
import csv

import pandas as pd
import yfinance as yf
import yahoofinancials

monthDict = {    '01':'January',
'02':'February',
'03':'March',
'04':'April',
'05':'May',
'06':'June',
'07':'July',
'08':'August',
'09':'September',
'10':'October',
'11':'November',
'12':'December'
}

class Direct:
    def __init__(self,title, desc, date, reigions):
        self.title = title
        self.desc = desc
        self.date = self.formatDate(date)
        self.reigions = reigions
        self.category = self.getCategory(title)
        self.stockData = None
        self.stockPrices = {-1:None,
                            0:None,
                            1:None
                            
                            }
        
        
    def getCategory(self,title):
        titleLower = title.lower()
        if ("smash" in titleLower):
            return "Smash"
        elif ("pok" in titleLower):
            return "Pokemon"
        elif ("indie" in titleLower):
            return "Indie"
        elif ("dragalia" in titleLower):
            return "Dragalia"
        elif ("feh" in titleLower):
            return "Fire Emblem Heroes"
        elif ("e3" in titleLower):
            return "E3"
        elif ("switch" in titleLower or "wii u" in titleLower):
            return "Hardware"
        elif ("mini" in titleLower or "micro" in titleLower):
            return "Mini"
#        elif ("---" in titleLower):
#            return "Showcase"
        else:
            return "General"
        
            
    def formatDate(self,date):
        dArr = re.split('[\s,]+',date)
        month = [key for key in monthDict.items() if key[1] == dArr[0]][0][0]
        x = dt.datetime(int(dArr[2]),int(month),int(dArr[1]))
        return x
        
    monthDict = {    '01':'January',
    '02':'February',
    '03':'March',
    '04':'April',
    '05':'May',
    '06':'June',
    '07':'July',
    '08':'August',
    '09':'September',
    '10':'October',
    '11':'November',
    '12':'December'
    }
        



