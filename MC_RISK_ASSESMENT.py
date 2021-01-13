# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 20:05:07 2021

@author: alexx

The following program assesses the risk on certain currency pairs 
It is used for determining the values in tMatrix in the Markov Chain algorithm 

The implementation uses the Kelly Criterion for determining optimal bet sizing 
"""

import numpy as np  
import pandas as pd  
import pandas_datareader as wb  
import matplotlib.pyplot as plt  
from scipy.stats import norm

GBPJPY = 'GBPJPY'
GBPUSD = 'GBPUSD'
USDJPY = 'USDJPY'

default_pair = GBPJPY

t_intervals = 30 
iterations = 25 

def read_file_date_price(fileName):
    data = pd.read_csv(fileName, index_col = 0, usecols = ['Date', 'Price'])
    return data

def sort_values_csv_file(data, sortBy):
    data.sort_values([sortBy], inplace = True)
    

#Settings for Monte Carlo asset data, how long, and how many forecasts 

def return_data():
    data = read_file_date_price('GBP_JPY Historical Data.csv')
    print("read file")
    return data

def plot_GBPJPY_AssetData(ticker):
    #Forex pair ticker 
    ticker = 'GBP_JPY' 
    t_intervals = 30 
    iterations = 25 
    #Read data from csv file saved from Investing.com
    data = read_file_date_price('GBP_JPY Historical Data.csv')
    #pd.read_csv('GBP_JPY Historical Data.csv',index_col=0,usecols=['Date', 'Price'])
    data.sort_values(["Date"], inplace=False)
    #sort_values_csv_file(data, "Date")
    #Preparing log returns from data
    data = data.rename(columns={"Price": ticker})
    #Plot of asset historical closing price
    log_returns = np.log(1 + data.pct_change())
    data.plot(figsize=(10, 6));
    log_returns.plot(figsize = (10, 6))
    
    print("plotted Asset Data")

#TO DO: Generalization
def return_log(pair):
    data = read_file_date_price('GBP_JPY Historical Data.csv')
    log_returns = np.log(1+ data.pct_change())
    return log_returns
    

#Setting up drift and random component in relation to asset data
def plot_firstMC_Sim():
    log_returns = return_log(default_pair)
    data = read_file_date_price('GBP_JPY Historical Data.csv')
    u = log_returns.mean()
    var = log_returns.var()
    drift = u - (0.5 * var)
    stdev = log_returns.std()
    daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))
    #Takes last data point as startpoint point for simulation
    S0 = data.iloc[-1]
    price_list = np.zeros_like(daily_returns)
    price_list[0] = S0
    #Applies Monte Carlo simulation in pair/security
    for t in range(1, t_intervals):
        price_list[t] = price_list[t - 1] * daily_returns[t]
        
    print("Plotted First Monte Carlo Simulation")
    
    plt.figure(figsize=(10,6))
    plt.plot(price_list)
    #return price points for probability algorithm
    return price_list

def plot_secondMC_Sim():
    data = return_data()
    log_returns = return_log(default_pair)
    u = log_returns.mean()
    var = log_returns.var()
    drift = u - (0.5 * var)
    stdev = log_returns.std()
    daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))#Takes last data point as startpoint point for simulation
    S0 = data.iloc[-1]
    price_list = np.zeros_like(daily_returns)
    price_list[0] = S0
    #Applies Monte Carlo simulation in pair/security
    for t in range(1, t_intervals):
        price_list[t] = price_list[t - 1] * daily_returns[t]
    
    print("Plotted Second Monte Carlo Simulation")
    
    plt.figure(figsize=(10,6))
    plt.plot(price_list)
    #return price points for probability algorithm
    return price_list

def plot_security(ticker):
    #stock ticker - Apple Inc
    ticker = 'AAPL' 
    #Time intervals for the future forecast 
    t_intervals = 30 
    #Number of simulation for mc 
    iterations = 25 
    #Acquiring data
    data = pd.DataFrame()
    #Data Reader takes data 
    data[ticker] = wb.DataReader(ticker, data_source='yahoo', start='2015-1-1')['Adj Close']
    print(ticker)
    print("Active days price data: ")
    print(data[ticker])
    #Preparing log returns from data
    log_returns = np.log(1 + data.pct_change())
    #Plot of asset historical closing price
    data.plot(figsize=(10, 6));
    
    
def main():
    plot_GBPJPY_AssetData(GBPJPY)
    plot_firstMC_Sim()
    plot_secondMC_Sim()
    plot_security('AAPL')
    
if __name__ == "__main__":
    main()	

    