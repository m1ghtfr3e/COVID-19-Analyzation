#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:39:38 2020

@author: n0way
"""

import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_json('timeseries.json')


def getCountryNames(data):
    """
    prints out a countries list
    """
    names = list(data.columns)   #sort alphabetically later
    print(names)


def getCountrySeries(data):
    
    """
    user can choose a country,
    function will return series
    of chosen country
    """
    
    country = input("choose a country: ")
    country_series = data[country]
    
    global normalized_series
    normalized_series = pd.json_normalize(data=country_series)
    
    #normalized_series.plot(x='date', y='confirmed')
    
    ##print(normalized_series)
    return country_series
    return normalized_series # flattened list of series (pd.DataFrame)
    

def plotCountryEvolv(normalized_series):
    print("""
          You have three options of which plot you wanna see:
              1) Confirmed 
              2) Recovered
              3) Deaths
          """)
    opt = input("choose option: ")
    if opt == '1':
        normalized_series.plot(x='date', y='confirmed')
    if opt == '2':
        normalized_series.plot(x='date', y='recovered')
    if opt == '3':
        normalized_series.plot(x='date', y='deaths')
        
def main():
    print("""
          Welcome. This is program is analyzing
          and mainly visualizing datasets about
          the current COVID-19 (Corona Virus).
    """)
    print("""
          There are several options to choose, 
          mostly accesible with the country name
          and the index number of options.
    """)
    
    countryList = input("""Do you want to have an overview of country names?
                        (y/n):  """)
    if countryList == 'y':
        getCountryNames(data)

    if countryList == 'n':
        main()
    
    print("You can access data for a specific country with its name.")
    getCountrySeries(data)
    plotCountryEvolv(normalized_series)


if __name__ == '__main__':
    main()