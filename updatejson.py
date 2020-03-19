#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:26:49 2020

@author: m1ghtfr3e
"""

import pandas as pd
import glob

def updateFile():
    path = "/.../.."                      # enter your actual working directory here
    allfiles = glob.glob(path + "/*.json")

    Data = []
    for file in allfiles:
        df = pd.read_json(file)
        Data.append(df)

        alldata = pd.concat(Data)
        return alldata
