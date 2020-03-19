import numpy as sp
import matplotlib.pylab as plt
import datetime as dt
import re
import csv

import pandas as pd
import yfinance as yf
import yahoofinancials
import fix_yahoo_finance as fyf
from pandas_datareader import data as pdr
pd.core.common.is_list = pd.api.types.is_list_like

from direct import *



directList = []
binEdges = sp.arange(-3.5, 3.5, 0.5).tolist()

#starting date from when you want to analyze (could add an enddate in the future
sinceDate = dt.datetime(2017, 1, 11)

categoryList = ["General", "Pokemon"]
hypeOfDirect ={ 'm1':[] }
impactOfDirect = { 'm1':[] ,'m2':[] }

#def formatToDataFrame(data):
#    x = pd.DataFrame(data,
#        #index=['2017-01-06', '2020-02-10'],
#        columns=['Open','Close','High','Low']
#    )
#
#    return x

def weekdayValid(date):
    #checks if date is between tuesday and thursday inclusive
    if date.weekday() >= 1 and date.weekday() <=3:
        return True
    else:
        return False

#d is your data, delta is the delta of days from the original date, and type is what reading you want to take, ex. "High", "Low", etc
def getPrice(d, delta, type):
    if(d == None):
        return -999
    else:
        return d.stockPrices[delta].at[d.date + dt.timedelta(days=delta) , type]
 
def calcChange(orgPrice, newPrice, measureList):
    percChange = (newPrice - orgPrice) / orgPrice
    measureList.append(percChange*100)

def calcHypeChange(d,measureList):
        newPrice = getPrice(d, 0, 'Open')
        orgPrice = getPrice(d, -1, 'Open')
        percChange = (newPrice - orgPrice) / orgPrice
        measureList.append(percChange*100)
        
def calcImpactChangeM1(d,impactOfDirect):
    calcChange(d, getPrice(d, 0, 'Open') , getPrice(0, 'High'), impactOfDirect['m1'])
    calcChange(d, getPrice(d, 0, 'Open') , getPrice(1, 'High'), impactOfDirect['m2'])

def printHistogram(dataArray, title):
    plt.hist(dataArray, bins=binEdges)
    plt.title(title)
    plt.xlabel('%Change')
    plt.ylabel('Frequency')
    plt.show()

def printLineGraph(d):
    startingPrice = getPrice(d,-1,'Open')
    datapoints = [
                startingPrice,
                getPrice(d,-1,'Close'),
                getPrice(d,0,'Open'),
                getPrice(d,0,'High'),
                getPrice(d,0,'Close'),
                getPrice(d,1,'Open'),
                getPrice(d,1,'Close')
                    ]
    yPoints = []
    for x in datapoints:
        yPoints.append ( ( x-startingPrice ) / startingPrice )
        x = ( x-startingPrice ) / startingPrice
    #binEdgesLine = sp.arange(-3.5, 3.5, 0.5).tolist()
#    print(yPoints)
#    print(datapoints)
    
    lineX = range(0,len(yPoints))
    
    plt.plot(lineX, yPoints)
    
    

def main():
    
    #directList = []
    
    #populate list of directs
    fileName = 'directListFINAL.csv'
    with open(fileName,'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        next(csv_reader)
        
        #extracts all needed data from csv, creates an object for each direct and adds it to the directList list
        for line in csv_reader:
            directList.append( Direct(line[0],line[1], str(line[2]), line[3]) )
    


    for d in directList:
        #if statement for what common categories you want to analyze
        if(d.date >= sinceDate) and d.category in categoryList and weekdayValid(d.date): #== "General":
            
            #adds the stock data for each direct to the direct object
            for delta in d.stockPrices:
                targetDate = d.date + dt.timedelta(days=delta)
                d.stockPrices[delta] = fyf.download(
                                        'NTDOY',
                                        start=targetDate,
                                        end=targetDate + dt.timedelta(days=1),
                                        #interval="5d"
                                        )
                                        
#            print(getPrice(d,-1,'High'))
            #calcHypeChange(d, hypeOfDirect['m1'])
            
            #calculating change for the hype of the direct
            calcChange(getPrice(d, -1, 'Open'), getPrice(d, 0, 'Open'), hypeOfDirect['m1'] )
            
            #calculating change for the impact of the direct, measure1
            calcChange(getPrice(d, 0, 'Open'), getPrice(d, 0, 'High'),  impactOfDirect['m1'] )
            
            #calculating change for the impact of the direct, measure2
            calcChange(getPrice(d, 0, 'Open'), getPrice(d, -1, 'Open'), impactOfDirect['m2'] )
            
            #d.stockData =
            print(d.category + " " + str(d.date) + " ^")
            #print(d.date)
            
            printLineGraph(d)
    
    plt.title('Direct Stock Patterns')
    plt.show()
    
    print("Hype of Direct " + str(hypeOfDirect['m1']))
    print("Impact of Direct M1 " + str(impactOfDirect['m1']))
    print("Impact of Direct M2 " + str(impactOfDirect['m2']))
    
    detailString = ""
    printHistogram(hypeOfDirect['m1'], "Hype of Direct: Measure 1")
    printHistogram(impactOfDirect['m1'], "Impact of Direct: Measure 1")
    printHistogram(impactOfDirect['m2'], "Impact of Direct: Measure 2" )
    

if __name__ == "__main__":
    main()
