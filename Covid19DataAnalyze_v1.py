#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:39:38 2020

@author: m1ghtfr3e
"""

import pandas as pd
import sys


# =============================================================================
# part one of program
# =============================================================================
data = pd.read_json('timeseries.json')   #enter here name of json file
#data = up.updateFile()

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
    if country == 'exit':
        sys.exit()
    else:
            # exception handling if there is unknown input
        try:
            country_series = data[country]
            global normalized_series
            normalized_series = pd.json_normalize(data=country_series)
            return normalized_series # flattened list of series (pd.DataFrame)

        except KeyError:
            print("Unknown. Please check the list and reenter.")
            getCountrySeries(data)

    return normalized_series



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
    try:
        if opt == '1':
            date_info = normalized_series.at[date, 'confirmed']
            print("\n There are {} confirmed cases on {}".format(date_info, date))
        if opt == '2':
            date_info = normalized_series.at[date, 'recovered']
            print("\n There are {} recovered cases on {}".format(date_info, date))
        if opt == '3':
            date_info = normalized_series.at[date, 'deaths']
            print("\n There are {} death cases on {}".format(date_info, date))
    except KeyError:
        print(KeyError)
        print("Maybe you entered date in a wrong format.")
    
    return
        

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
    normalized_series.plot(x='confirmed', y='deaths', title='''
                                   Relation: confirmed and death cases
                                   ''')


def relateConfirmedRecovered(normalized_series):
    """
    visualizes relation between confirmed cases and deaths
    """
    normalized_series.plot(x='confirmed', y='recovered', title='''
                           Relation: confirmed and recovered cases''')


# graphs doesn't make too much sense when number range is too big
def relateAll(normalized_series):
    """
    brings all columns to one
    area graph, not too under-
    standable with small differences
    """
    normalized_series.plot(x='date', y=['confirmed', 'recovered',
                                        'deaths'], kind='bar', title='Overview')
    #normalized_series.plot(x=date_list, y=[c, r, d], kind='bar')
    

# FIX THIS
def worldwideOverview(data):  # NOT working now
    """
    plot worldwide data
    """
    countries = []
    for d in data:
        countries.append(d)
    
    #worldwide = data[countries]
    #worldwide = []
        for c in countries:
            worldwide = data[c]
    
            for w in worldwide:
                print(worldwide)
    
    dates = []
    
    
def main():
    #getCountrySeries(data)
    while True:
        getCountrySeries(data)  # defines country
        
        option = input(""" Which graph you want to access:
            1) Evolution of cases after dates and category
            2) Relation between confirmed cases and deaths
            3) Relation between all
            4) Relation between confirmed and recovered cases
            5) Get Numbers of cases on a specific date
                \n""")
        
        if option == '1':
            plotCountryEvolv(normalized_series)
        if option == '2':
            relateConfirmedDeaths(normalized_series)
        if option == '3':
            relateAll(normalized_series)
        if option == '4':
            relateConfirmedRecovered(normalized_series)
        if option == '5':   
            getCountryInfo(normalized_series)
        if option == 'exit':
            sys.exit()
        else:
            False


if __name__ == '__main__':
    #worldwideOverview(data)
    print("""
          Welcome. This program is analyzing
          and mainly visualizing datasets about
          the current COVID-19 (Corona Virus) situation.
    """)
    
    print("""
          There are several options to choose, 
          accesible with the country name
          and the index number of options.
          Type 'exit' to stop the program.
    """)
    
    print("""
          Data-Sets are from:
              
    https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset & 
    https://pomber.github.io/covid19/timeseries.json
    
    ([program coded by m1ghtfr3e])
    """)
    

    print("Here is an overview of country names:")
    getCountryNames(data)
        
    
    print("\n\nYou can access data for a specific country with its name.\n")
    
    main()