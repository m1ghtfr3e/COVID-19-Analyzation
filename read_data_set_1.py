#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 20:20:38 2020

@author: n0way
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


confirmed = pd.read_csv('time_series_19-covid-Confirmed.csv')
confirmed.head()
##location = confirmed.loc[confirmed['Country/Region'] == 'Germany']



"""
ax1 = confirmed.plot.scatter(x='Country/Region',
                        y='3/16/20', subplots=True)









def getIndex():
     #will do this later
    return
    
    

def foo():
    country = input("enter a country: ")
    location = confirmed.loc[confirmed['Country/Region'] == country]
    location.plot()
"""