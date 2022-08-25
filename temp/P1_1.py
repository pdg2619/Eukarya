# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 09:47:09 2022

@author: pdg26
"""

counts = 0;
"99999 / 6 = 16666.5"
for i in range(0, 10000):
    if i < 10 :
        counts = counts + 6
        print("{}SHEEP.{}".format(i,counts))
    elif i < 100:
        counts = counts + 7
        print("{}SHEEP.{}".format(i,counts))
    elif i < 1000:
        counts = counts + 8
        print("{}SHEEP.{}".format(i,counts))
    elif i < 10000:
        counts = counts + 9
        print("{}SHEEP.{}".format(i,counts))   
#    else :
#        counts = counts + 10
#        print("{}SHEEP{}".format(i,counts))
    elif counts == 99999:
        counts = counts + 10
        print("{}SHEEP.{}".format(i,counts))