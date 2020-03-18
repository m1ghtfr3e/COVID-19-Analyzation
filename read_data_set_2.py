#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 00:13:51 2020

@author: m1ghtfr3e
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy


confirmed = pd.read_csv('time_series_19-covid-Confirmed.csv')

deaths = pd.read_csv('time_series_19-covid-Deaths.csv')

recovered = pd.read_csv('time_series_19-covid-Recovered.csv')

##############################################################################

def dates_to_array():
    date = input("choose date: ")
    date_array = confirmed[date].to_numpy()
    return date_array    
#############################################################################
    
def countries_to_array():
    countryNew = confirmed.set_index('Country/Region', 'Province/State')
    
    country = input("choose a country: ")
    country_array = countryNew.loc[country].to_numpy()
    return country_array
##############################################################################



    
    
def main():
    dates_to_array()
    countries_to_array()
