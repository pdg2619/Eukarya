# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 10:07:17 2022

@author: pdg26
"""

counts = 88890

for i in range(10000, 17000):
    if counts < 99999:
        counts = counts + 10
        print("{}SHEEP.{}".format(i,counts))
