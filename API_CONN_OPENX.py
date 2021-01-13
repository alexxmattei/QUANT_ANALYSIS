'''
Using the intrinio_sdk for thier api 
This api gives mostly data about stocks along with technicals
It can be use to extract and parse news and emerging data 
'''

from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

import requests
import json

from collections import OrderedDict
from pandas.io.json import json_normalize

INTR_SECRET_API_KEY = "OmRmMDQ1NjhmNTlkNzgzYzg1YmVjYTI2NTVjMjFkNjg2"
#define default dates 
start_date = '2021-01-01'
end_date = '2021-01-12'
#define default index calculation period variables 
period = 14
fast_period = 12
slow_period = 26
signal_period = 9

adx_list = [42.34214918139969, 40.23256815129151, 38.42052009387036, 37.352134954637236, 36.375818106481795, 35.98213727237122, 35.11162904528978, 34.475432481983496, 33.437896830222165, 32.92698340519346, 32.890111355952854, 32.02366339948408, 31.6210215212636, 31.1210215212632]
rsi_list = [65.05928093771874, 85.60213592053555, 82.99776570971, 78.75118011530385, 77.7924934160109, 72.37115460851449, 77.74665808092792, 76.72619247602384, 75.86596224481654, 73.47720294750977, 74.01655398350051, 73.93632408794514, 76.40816437167945, 75.458211143695]

def calculate_rsi_move():
    rsi_move = []
    ind = 0
    for rsi in rsi_list:
        if ind < 13:
            rsi_move.append(rsi_list[ind + 1] - rsi)
            ind += 1 
        else:
            rsi_move.append(0)
            ind += 1
    return rsi_move

def calculate_adx_move():
    adx_move = []
    ind = 0
    for adx in adx_list:
        if ind < 13 :
            adx_move.append(adx_list[ind + 1] - adx)
            ind += 1
        else:
            adx_move.append(0)
            ind += 1
    return adx_move
            
class ApiClient():
    def __init__(self):
        intrinio.ApiClient().set_api_key(INTR_SECRET_API_KEY)
        intrinio.ApiClient().allow_retries(True)
        
def get_all_currencies():
    response = intrinio.ForexApi().get_forex_pairs()
    print(response)
    return response 
    
def get_quote_currency(pair, start_date, end_date):
    timeframe = 'D1'
    timezone = 'UTC'
    start_time = '00:00'
    end_time = '23:59'
    page_size = 1
    next_page = ''
    
    response = intrinio.ForexApi().get_forex_prices(pair, timeframe, timezone=timezone, start_date=start_date, start_time=start_time, end_date=end_date, end_time=end_time, page_size=page_size, next_page=next_page)
    print(response)
    return response 
    
def get_price_currency(pair, start_date, end_date):
    timeframe = 'D1'
    timezone = 'UTC'
    start_time = '00:00'
    end_time = '12:00'
    page_size = 1
    next_page = ''
    
    response = intrinio.ForexApi().get_forex_prices(pair, timeframe, timezone=timezone, start_date=start_date, start_time=start_time, end_date=end_date, end_time=end_time, page_size=page_size, next_page=next_page)
    print(response)
    return response 
    
def get_security_price(identifier, start_date, end_date):      
    frequency = 'daily'
    page_size = 100
    next_page = ''
    
    response = intrinio.SecurityApi().get_security_stock_prices(identifier, start_date=start_date, end_date=end_date, frequency=frequency, page_size=page_size, next_page=next_page)
    print(response)
    return response 

def get_security_wr(identifier, start_date, end_date):
    page_size = 100
    next_page = ''
    
    response = intrinio.SecurityApi().get_security_price_technicals_wr(identifier, period=period, start_date=start_date, end_date=end_date, page_size=page_size, next_page=next_page)
    print(response)
    return response

def get_security_adx(identifier, start_date, end_date):
    page_size = 100
    next_page = ''
    
    response = intrinio.SecurityApi().get_security_price_technicals_adx(identifier, period=period, start_date=start_date, end_date=end_date, page_size=page_size, next_page=next_page)
    print(response)
    return response 

def get_security_rsi(identifier, start_date, end_date):
    price_key = 'close'
    page_size = 100
    next_page = ''
    
    response = intrinio.SecurityApi().get_security_price_technicals_rsi(identifier, period=period, price_key=price_key, start_date=start_date, end_date=end_date, page_size=page_size, next_page=next_page)
    print(response)
    return response 

def get_security_vol(identifier, start_date, end_date):
    page_size = 100
    next_page = ''
    
    response = intrinio.SecurityApi().get_security_price_technicals_obv(identifier, start_date=start_date, end_date=end_date, page_size=page_size, next_page=next_page)
    print(response)
    return response 

def get_security_vol_mean(identifier, start_date, end_date):
    #this indicator has a default custom value for period of 10 
    #it will be used separately here
    period = 10
    page_size = 100
    next_page = ''
    
    response = intrinio.SecurityApi().get_security_price_technicals_obv_mean(identifier, period=period, start_date=start_date, end_date=end_date, page_size=page_size, next_page=next_page)
    print(response)
    return response

def get_security_sma(identifier, start_date, end_date, period):
    price_key = 'close'
    page_size = 100
    next_page = ''
    
    response = intrinio.SecurityApi().get_security_price_technicals_sma(identifier, period=period, price_key=price_key, start_date=start_date, end_date=end_date, page_size=page_size, next_page=next_page)
    print(response)
    return response 

def get_security_adi(identifier, start_date, end_date):
    page_size = 100
    next_page = ''
    
    response = intrinio.SecurityApi().get_security_price_technicals_adi(identifier, start_date=start_date, end_date=end_date, page_size=page_size, next_page=next_page)
    print(response)
    return response 

#money-flow index
def get_security_mfi(identifier, start_date, end_date):
    page_size = 100
    next_page = ''
    
    response = intrinio.SecurityApi().get_security_price_technicals_mfi(identifier, period=period, start_date=start_date, end_date=end_date, page_size=page_size, next_page=next_page)
    print(response)
    return response 

#moving average convergence divergence 
def get_security_macd(identifier, start_date, end_date, fast_period, slow_period, signal_period):
    price_key = 'close'
    page_size = 100
    next_page = ''
    
    response = intrinio.SecurityApi().get_security_price_technicals_macd(identifier, fast_period=fast_period, slow_period=slow_period, signal_period=signal_period, price_key=price_key, start_date=start_date, end_date=end_date, page_size=page_size, next_page=next_page)
    print(response)
    return response

def get_all_securiteis_by_comp(identifier):
    next_page = ''

    response = intrinio.CompanyApi().get_company_securities(identifier, next_page=next_page)
    print(response)
    return response 

def lookfor_company(identifier):
    response = intrinio.CompanyApi().get_company(identifier)
    print(response)
    return response 

def return_security_adx():
    return adx_list

def return_security_rsi():
    return rsi_list


'''
def main():
    rsi_move = calculate_rsi_move()
    print(rsi_move)
    adx_move = calculate_adx_move()
    print(adx_move)
    
if __name__ == "__main__":
    main()
'''

'''
Tested the Api responses 



class Payload(object):
    def __init__(self, indicator, next_page, security, technicals)
'''      

'''

def main():
    currency = 'GBPJPY'
    stock_ticker = 'AAPL'
    sma_period = 200
  
    get_all_currencies()
    get_quote_currency(currency, '2018-01-01', '2020-01-05')
    get_security_adx(stock_ticker, '2018-01-01', '2020-01-05')
    get_all_securiteis_by_comp(stock_ticker)
    get_security_adi(stock_ticker, start_date, end_date)
    get_security_macd(stock_ticker, start_date, end_date, fast_period, slow_period, signal_period)
    get_security_mfi(stock_ticker, start_date, end_date)
    get_security_rsi(stock_ticker, start_date, end_date)
    get_security_sma(stock_ticker, start_date, end_date, sma_period)
    get_security_vol(stock_ticker, start_date, end_date)
    get_security_vol_mean(stock_ticker, start_date, end_date)
    
    s_date = "2018-01-06"
    e_date = "2021-01-13"
    
    adx = get_security_adx(stock_ticker, s_date, e_date)
    rsi = get_security_rsi(stock_ticker, s_date, e_date)
    #print(adx['technicals']['adx'])
    
    
    itr = 0
    for vals in adx['technicals'] :
            vals = adx[itr]
            itr = itr + 1
            #print(vals)
            
            
   
    adxobj = json.loads(adx)
    ind = 0
    adx_vals = []
    for adx_val in adxobj["technicals"][0]["adx"]:
         adx_vals[ind] = adx_val
         ind += 1
         
    print(adx_vals)
    
    a = json.dumps(str(adx), sort_keys=True, indent=4)
    #json.loads(json.JSONDecoder(adx))
    b = json.JSONDecoder().decode(str(adx))
    print(b[0])
    
    
        
    for adx in adx_data:
        print(adx['adx'])
  
    
   
    
if __name__ == '__main__':
    main()
'''

