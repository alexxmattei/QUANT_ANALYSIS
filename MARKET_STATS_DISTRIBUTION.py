# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 03:32:24 2021

@author: alexx

File that contains probability distribution for pair, securities 
#latest?symbol=EUR/USD,USD/JPY,GBP/CHF&access_key=5sT7U5zKOMY3oDSv0h90gNA0o

aapl = yf.download('AAPL','2018-12-26', '2019-12-26')

mean = np.mean(aapl['Adj Close'])
median = np.median(aapl['Adj Close']) 

mode = statistics.mode(aapl['Adj Close'])

aapl['daily_percent_change'] = aapl['Adj Close'].pct_change()
aapl.daily_percent_change.hist(figsize=(10,7))
plt.ylabel('Frequency')
plt.xlabel('Daily Percentage Change')
plt.show()

#index reference for apple pricing 
spx = yf.download('^GSPC','2018-12-26', '2021-01-13')
spx['daily_percent_change'] = spx['Adj Close'].pct_change()
plt.figure(figsize=(10,7))
plt.scatter(aapl.daily_percent_change,spx.daily_percent_change)
plt.xlabel('AAPL Daily Returns')
plt.ylabel('SPY Daily Returns')
plt.grid()
plt.show()

correlation, _ = spearmanr(aapl.daily_percent_change.dropna(),spx.daily_percent_change.dropna())
print('Spearmans correlation is %.2f' % correlation)

data_binom = binom.rvs(n=10,p=0.8,size=10000)

ax = sns.distplot(data_binom,
                  kde=False,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Binomial Distribution', ylabel='Frequency')
"""

import requests
import statistics 
import matplotlib.pyplot as plt
import numpy as np 
import yfinance as yf
from scipy import special
from scipy.stats import spearmanr
from scipy.stats import bernoulli
import scipy.stats as ss
import yfinance as yf
import sys

'''
sys.path.append is needed in order to import other files as packages 
as we do this into out folder we can rename our packages and use them for calculations
'''
sys.path.append('D:\ProiectePersonale\PythonPrograms\QUANT_FL\QUANT_ANALYSIS')
#brokerage api connection and function
import MARKET_OPENX_CONN_API as openx_api
#technical analysis api connection and data
import API_CONN_OPENX as intr_stats
#monte carlo simulations
import MC_RISK_ASSESMENT as mc
#markov chain implementation
import MARKET_VISUALIZER as markov
#historic data parsed from csv 
import MARKET_ANALYZER as hist_parsed

'''
import market_openx_conn_api as api
import mc_risk_assesment as mc
'''


def calc_p():
    adx_list = intr_stats.adx_list
    rsi_list = intr_stats.rsi_list
    adx_move = intr_stats.calculate_adx_move()
    rsi_move = intr_stats.calculate_rsi_move()
    
    p_adx = 0
    p_rsi = 0
    
    ind = 0
    while ind < 14:
        p_adx = p_adx + adx_list[ind] * adx_move[ind]
        p_rsi = p_rsi + rsi_list[ind] * rsi_move[ind]
        ind += 1
    
    p_adx = abs(p_adx /14)
    p_rsi = abs(p_rsi /14) 
    
    print(p_adx)
    print(p_rsi)
    
    return (p_adx + p_rsi) / 2 / 100
   # for adx in adx_list:
        
    
#cdf = cumulative distribution 
def plot_beta_ind(x_range, a, b, mu, sigma = 1, cdf = True, **kwargs):
    x = x_range 


X = ss.beta(1, 3) 
  
def return_transpose():
    t = markov.tMatrix
    p = calc_p()
   
    

            
            
'''
def main():
    calc_p()
    mc.plot_security('AAPL')
    
        
    x = ss.binom(14, 1 - p)
    UP = x.cdf(4)
    CS = 1 - DN - UP
    
    i = 0
    j = 0 
    while i < 3:
        var = random(0, 5)
        while j < 3 :
            X = ss.binom(14, p)
            DN = X.cdf(var)
            t[i][j] = 
    
    print(DN)
    print(UP)
    print(CS)
    
    
    
if __name__ == "__main__":
    main()
'''





































