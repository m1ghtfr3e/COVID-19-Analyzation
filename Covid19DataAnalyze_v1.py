#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:39:38 2020

@author: m1ghtfr3e
"""

import pandas as pd
import DataPipe
from pandas.io.json import json_normalize
import json


# =============================================================================
# part two of program
# =============================================================================
files_csv = DataPipe.DataPipeCSV()
for file in files_csv:
    pandaFiles_csv = pd.read_csv(file)
    pandaFiles_csv = pandaFiles_csv.fillna(0)

"""
files_json = DataPipe.DataPipeJSON_meta()
for f in files_json:
    with open(f) as f:
        metaFiles = json.load(f)
        #for meta in metaFiles:
        metaFrame = pd.DataFrame.from_dict(meta)
"""


# =============================================================================
# part one of program
# =============================================================================
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


def getCountryInfo(normalized_series): # data: Series | date format: yyyy/m/d(d)
    """
    user can enter country and choose
    a date; function will return
    infos belonging to input
    """
    date = input("choose a date [yyyy-m-d(d)]: ")
    normalized_series = normalized_series.set_index('date')
    # date_info = normalized_series.at[date, confirmed]
    
    opt = input("Choose (1)confirmed / (2)recovered / (3)deaths: ")
    if opt == '1':
        date_info = normalized_series.at[date, 'confirmed']
        print("\n There are {} confirmed cases on {}".format(date_info, date))
    if opt == '2':
        date_info = normalized_series.at[date, 'recovered']
        print("\n There are {} recovered cases on {}".format(date_info, date))
    if opt == '3':
        date_info = normalized_series.at[date, 'deaths']
        print("\n There are {} death cases on {}".format(date_info, date))

    return date_info
        

def plotCountryEvolv(normalized_series):
    print("""
          You have three options of which plot you wanna see:
              1) Confirmed 
              2) Recovered
              3) Deaths
          """)
    opt = input("choose option: ")
    if opt == '1':
        normalized_series.plot(x='date', y='confirmed', title='Confirmed cases')
    if opt == '2':
        normalized_series.plot(x='date', y='recovered', title='Recovered cases')
    if opt == '3':
        normalized_series.plot(x='date', y='deaths', title='Death cases')


def relateConfirmedDeaths(normalized_series):
    """
    visualizes relation between 
    confirmed cases and death
    """
    normalized_series.plot.scatter(x='confirmed', y='deaths', title='''Relation 
                                   Confirmed and death cases''')
    
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
            4) Get Numbers of cases on a specific date
                \n""")
        
        if option == '1':
            plotCountryEvolv(normalized_series)
        if option == '2':
            relateConfirmedDeaths(normalized_series)
        if option == '3':
            relateAll(normalized_series)
        if option == '4':
            getCountryInfo(normalized_series)

        continue
        """else:
            print("Program is stopping.")
            return False"""


if __name__ == '__main__':
    main()