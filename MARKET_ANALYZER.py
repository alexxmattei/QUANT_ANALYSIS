# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 22:15:55 2020

@author: alexx
"""

import csv
import tkinter
import numpy as np 
import pandas as pd



def openGBPJPYSp():
    with open("GBP_JPY Historical Data.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ",")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'{", ".join(row)}')
                line_count += 1
            else:
                print (f'\t{row[0]} {row[1]} {row[2]}, {row[3]}, {row[4]}, {row[5]}')
                    
            line_count += 1
            print(f'Processed {line_count} lines of data')
    
def openGBPJPYPd():
     with open("GBP_JPY Historical Data.csv") as csv_file:
         gbpjpy_ten_years = pd.read_csv(csv_file)
         print(gbpjpy_ten_years)
         
def readGBPJPY():
    with open("GBP_JPY Historical Data.csv") as csv_file:
         gbpjpy_ten_years = pd.read_csv(csv_file)
         print(gbpjpy_ten_years)
    return gbpjpy_ten_years
         
         
def storeDataGBPJPY():
    index = 0
    pair_file = readGBPJPY()
    for row in pair_file:
        percentage = row[5]
        storeGBPJPY_per = len(pair_file)
        storeGBPJPY_per[percentage]
    
    return storeGBPJPY_per
        
def printResultsFromGBPJPY():
    print("Using simple CSV interpreter: \n")
    openGBPJPYSp()
    print("Using the pandas CSV interpreter: \n")
    openGBPJPYPd()


def main():
    index = 0
    data_file_gbpjpy = storeDataGBPJPY()
    for elem in data_file_gbpjpy:
        print ("day {index}: {elem}")
    
if __name__ == "__main__":
    main()
    