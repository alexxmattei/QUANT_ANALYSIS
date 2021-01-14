# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 02:41:06 2021

@author: alexx
"""
import sys
sys.path.append('D:\ProiectePersonale\PythonPrograms\QUANT_FL\QUANT_ANALYSIS')
import MARKET_STATS_DISTRIBUTION as mktool
import MARKET_VISUALIZER as markov
import MC_RISK_ASSESMENT as mcra

def main():
    mktool.set_transpose_values(mktool.stock_beta)
    markov.run_markov()
    mcra.plot_GBPJPY_AssetData(mcra.GBPJPY)
    mcra.plot_firstMC_Sim()
    mcra.plot_secondMC_Sim()
    mcra.plot_security('AAPL')

    
if __name__ == "__main__":
    main()