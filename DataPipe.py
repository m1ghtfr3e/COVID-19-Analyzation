#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 21:58:51 2020

@author: m1ghtfr3e
"""

import glob

def DataPipe():
    """
    getting daily datasets (55, in csv format)
    """
    path = '~/datasets/csse_covid_19_daily_reports' #enter your path here
    files = glob.glob(path + '/*.csv')
    return files
