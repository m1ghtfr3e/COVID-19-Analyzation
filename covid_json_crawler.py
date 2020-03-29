#!/usr/bin/python3

import wget

def updateFile():

    url = "https://pomber.github.io/covid19/timeseries.json"

    wget.download(url, 'timeseries.json')
