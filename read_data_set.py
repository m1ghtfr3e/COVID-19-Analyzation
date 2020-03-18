#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:39:53 2020

@author: m1ghtfr3e
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

""" 
Data Analysis [ Corona Virus] 

"""

# time series confirmed
confirmed = pd.read_csv('time_series_19-covid-Confirmed.csv')
Confirmed = confirmed.set_index('Country/Region', 'Province/State')

deaths = pd.read_csv('time_series_19-covid-Deaths.csv')
Deaths = deaths.set_index('Country/Region')

recovered = pd.read_csv('time_series_19-covid-Recovered.csv')
Recovered = recovered.set_index('Country/Region')


##############################################################################

date_series = pd.Series(confirmed['3/16/20'])
country_series = pd.Series(confirmed['Country/Region'])

x = country_series.to_numpy()
y = date_series.to_numpy()

plt.plot(y)
plt.ylabel(x)
plt.show()

##############################################################################

#confirmed_pivot = pd.pivot_table(confirmed)

##############################################################################
# getting col names
confirmed_col = list(confirmed.columns)
deaths_col = list(deaths.columns)
recovered_col = list(deaths.columns)

##############################################################################
# choose a country and see evolution over the dates

def confirmed_countryEvolve():
    country = input("choose a country to see: ")
    
    country_toPlot = Confirmed.loc[country]
    country_toPlot.plot()


def deaths_countryEvolve():
    country = input("choose a country to see: ")

    country_toPlot = Deaths.loc[country]    
    country_toPlot.plot()
    
def recovered_countryEvolve():
    country = input("choose a country to see: ")
    
    country_toPlot = Recovered.loc[country]
    country_toPlot.plot()
#recovered_countryEvolve()
##############################################################################

# compare conf, deaths & recov for specific country
def countryOverview():
    country = input("choose a country to see: ")
    
    confirmedSeries = confirmed.loc[country]
    deathsSeries = deaths.loc[country]
    recoveredSeries = recovered.loc[country]
    
    """ just works for some countries
    frame = {'confirmed': confirmedSeries, 'deaths': deathsSeries,
             'recovered': recoveredSeries}
    overview = pd.DataFrame(frame)
    overview.plot()"""
    
    
    
    
#countryOverview()
##############################################################################   
"""
#creating series of countries
#creating series of a date
def createSeries_confirmed():
    
    date = input("choose date [m/dd/yy]: ")
    
    date_series = pd.Series(confirmed[date])
    country_series = pd.Series(confirmed['Country/Region'])


def plot_confirmed():
    createSeries_confirmed()
    new = date_series.append(country_series)
    new.plot()
    
plot_confirmed()

# plots of above
def plotConfirmed():
    confirmed.plot(x='Country/Region', y='3/16/20', kind='bar')
    
def plotDeaths():
    deaths.plot()
    
def plotRecovered():
    recovered.plot()
"""




"""    
if __name__ == '__main__':
    plotConfirmed()
    plotDeaths()
    plotRecovered()
"""
