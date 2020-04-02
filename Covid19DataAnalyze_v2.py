#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:10:06 2020

@author: m1ghtfr3e
"""

import os
import os.path
import pandas as pd
import sys
import matplotlib.pyplot as plt
import covid_json_crawler as crawl
import time


# =============================================================================
# part one of program
# =============================================================================

# checks if (older) data exists and deletes

start = input("""\nBefore we start do you have an internet connection to get
most recent data? (y / n): """)

if start == 'y':
    if os.path.isfile('timeseries.json'):
        os.remove('timeseries.json')
        print("\n Loading Data \n")
        data = crawl.updateFile()        # downloads new dataset
    else:
        print("\n Loading Data \n")
        data = crawl.updateFile() 
else:
    print("If there is no data available the program won't work, otherwise\
          it will start now.")

data = pd.read_json('timeseries.json')


def getCountryNames(data):
    """
    prints out a countries list
    """
    names = list(data.columns)
    names = sorted(names)
    
    for word in names:
        print(word)
        time.sleep(.10)


def getCountrySeries(data):
    
    """
    user can choose a country,
    function will return series
    of chosen country
    """
    global country
    country = input("choose a country: ")
    if country == 'exit':
        print("Goodbye.")
        time.sleep(3)
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
    return country


# data: Series | date format: yyyy/m/d(d)
def getCountryInfo(normalized_series, country): 
    
    """
    user can enter country and choose
    a date; function will return
    infos belonging to input
    """
    date = input("choose a date [yyyy-m-d(d)]: ")
    normalized_series = normalized_series.set_index('date')
    # date_info = normalized_series.at[date, confirmed]
    
    try:	

        inf_conf = normalized_series.at[date, 'confirmed']
        inf_rec = normalized_series.at[date, 'recovered']
        inf_dead = normalized_series.at[date, 'deaths']
        print(f"""
The official numbers for {country} on {date} are:
  -> confirmed cases:  {inf_conf}
  -> recovered cases:  {inf_rec}
  -> death cases:      {inf_dead}
""")

    except KeyError:
        print(KeyError)
        print("Maybe you entered date in a wrong format.")
    
    return
        

def plotCountryEvolv(normalized_series, country):
    
    print("""
          You have three options of which plot you wanna see:
              1) Confirmed 
              2) Recovered
              3) Deaths
          """)
    opt = input("choose option: ")
    if opt == '1':
        normalized_series.plot(x='date', y='confirmed', title='''
                               Confirmed cases in {}'''.format(country))
        plt.show()

    if opt == '2':
        normalized_series.plot(x='date', y='recovered', title='''
                               Recovered cases in {}'''.format(country))
        plt.show()

    if opt == '3':
        normalized_series.plot(x='date', y='deaths', title=''''
                               Death cases in {}'''.format(country))
        plt.show()


def relateConfirmedDeaths(normalized_series, country):
    """
    visualizes relation between 
    confirmed cases and death
    """
    normalized_series.plot(x='confirmed', y='deaths', title='''
                                   Relation: confirmed and death cases
                                             in {}'''.format(country))
    plt.show()


def relateConfirmedRecovered(normalized_series, country):
    """
    visualizes relation between confirmed cases and deaths
    """
    normalized_series.plot(x='confirmed', y='recovered', title='''
                           Relation: confirmed and recovered cases
                                     in {}'''.format(country))
    plt.show()

# graphs doesn't make too much sense when number range is too big
def relateAll(normalized_series, country):
    """
    brings all columns to one
    area graph, not too under-
    standable with small differences
    """
    normalized_series.plot(x='date', y=['confirmed', 'recovered',
                                        'deaths'], kind='bar', title='''
                            Overview in {}'''.format(country))
    #normalized_series.plot(x=date_list, y=[c, r, d], kind='bar')
    plt.show()

    
def worldwideNumbers(data):
    
    """ counting cases worldwide """
    
    last = data.index[-1]     #last row is most actual one
    last_row = data.loc[last]  #getting series of last row
    
    worldwide_now = pd.json_normalize(data=last_row)  #dataframe of all
    
    confirmed = 0
    recovered = 0
    deaths = 0
    
    for con in worldwide_now['confirmed']:
        confirmed += con
        
    for rev in worldwide_now['recovered']:
        recovered += rev
        
    for dead in worldwide_now['deaths']:
        deaths += dead
                
                
                
    print(f"""
Until {worldwide_now.loc[1]['date']} there are officially:
  --> confirmed cases: {confirmed}
  --> recovered cases: {recovered}
  --> death cases :    {deaths}
          """)
    
    



    
def main():
    #getCountrySeries(data)
    while True:
        
        option = input(""" Which graph you want to access:
                       
            1) Evolution of cases after dates and category
            2) Relation between confirmed cases and deaths
            3) Relation between all
            4) Relation between confirmed and recovered cases
            5) Get Numbers of cases on a specific date
            6) Worldwide numbers until most recent date
                \n""")
        
        if option == '1':
            getCountrySeries(data)  # defines country
            plotCountryEvolv(normalized_series, country)
        if option == '2':
            getCountrySeries(data)  # defines country
            relateConfirmedDeaths(normalized_series, country)
        if option == '3':
            getCountrySeries(data)  # defines country
            relateAll(normalized_series, country)
        if option == '4':
            getCountrySeries(data)  # defines country
            relateConfirmedRecovered(normalized_series, country)
        if option == '5':
            getCountrySeries(data)  # defines country
            getCountryInfo(normalized_series, country)
        if option == '6':
            worldwideNumbers(data)
        
        if option == 'exit':
            print("Goodbye.")
            time.sleep(3)
            sys.exit()
        else:
            False


if __name__ == '__main__':

    
    text = """\n\n
          Welcome. This program is analyzing
          and mainly visualizing datasets about
          the current COVID-19 (Corona Virus) situation.
          
          
          There are several options to choose, 
          accesible with the country name
          and the index number of options.
          Type 'exit' to stop the program.
          
          Data-Sets are from:
              
    https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset
                  &
    https://pomber.github.io/covid19/timeseries.json
    
    ([code by m1ghtfr3e])
    
    
    Loading all country names now: 
"""

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.03)



    getCountryNames(data)
        
    
    print("\n\nYou can access data for a specific country with its name.\n")
    
    main()

