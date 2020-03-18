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
    names = list(data.columns)
    names = sorted(names)
    for x in names:
        print(x)


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


def relateConfirmedDeaths(normalized_series):
    """
    visualizes relation between 
    confirmed cases and death
    """
    normalized_series.plot.scatter(x='confirmed', y='deaths')
    
# graph doesn't make sense
# number of recovered > confirmed ?!
def relateAll(normalized_series):
    """
    brings all columns to one
    area graph, not too under-
    standable with small differences
    """
    normalized_series.plot.area()

    
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
    

    print("Here is an overview of country names:")
    getCountryNames(data)
        
    
    print("\n\nYou can access data for a specific country with its name.\n")
    
    getCountrySeries(data)  # defines country
    
    while True:
        option = input(""" Which graph you want to access:
            1) Evolution of cases after dates and category
            2) Relation between confirmed cases and deaths
            3) Relation between all 
                \n""")
        
        if option == '1':
            plotCountryEvolv(normalized_series)
        if option == '2':
            relateConfirmedDeaths(normalized_series)
        if option == '3':
            relateAll(normalized_series)
        else:
            print("Program is stopping.")
            return False


if __name__ == '__main__':
    main()