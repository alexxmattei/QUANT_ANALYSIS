# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 11:15:58 2021

@author: alexx
"""

#importing the requests library 
import requests  
  
# api-endpoint 
BASE_URL = "http://xapia.x-station.eu:5124"
#password for the 'login' entry data 
PASSWORD = "xoh31812"
#account number and user id are the same in the documentation
#'login' field data  
ACC_NUMBER = "11716696"
userId = "11716696"

json_req_body = {
	"command": "login",
	"arguments": {
		"userId": "11716696",
		"password": "xoh31812",
		"appId": "test",
		"appName": "test"
	}
}
    
# defining a params dict for the parameters to be sent to the API 
PARAMS = {'userId':userId, 'password': PASSWORD} 
  
# sending get request and saving the response as response object 

# extracting data in json format 
def getLoginResponseXTB():
    r = requests.get(url = BASE_URL, params = PARAMS) 
    data = r.json() 
    print(str(data))

def main():
    getLoginResponseXTB()

if __name__ == '__main__':
    main()

