# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 22:13:46 2021

@author: tccmi
"""

import quandl

quandl.ApiConfig.api_key = "YOUR API KEY HERE"

gdp = quandl.get("FRED/GDP")
gdp.reset_index(inplace=True)

ur = quandl.get("FRED/UNRATE")
ur.reset_index(inplace=True)

ir = quandl.get("FRED/DFF")
ir.reset_index(inplace=True)
