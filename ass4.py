# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 22:20:55 2020

@author: Shreyaa Dani
"""


import pandas as pd
import numpy as np
import seaborn
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


data = pd.read_csv('f:\\nesarc_pds.csv', low_memory=False)

sub = data[data['S1Q213'] <= 1]
# a copy of dataset where undesired data has been removed

#MY PRIMARY TOPIC OR DEPENDENT VARIABLE
c4 = data['S1Q213'].value_counts(dropna = False)

#DEPENDENT VARIABLE GRAPH PLOT
seaborn.countplot(x = 'S1Q213', data=sub)

plt.title('DURING PAST 4 WEEKS, HOW OFTEN FELT DOWNHEARTED AND DEPRESSED')

seaborn.factorplot(x = 'S1Q213', y = 'S4AQ4A18',data = sub, kind = 'bar', ci= None)

plt.title('Relation between sucidaland depressed')


seaborn.factorplot(x = 'S4AQ11', y = 'S1Q213',data = sub, kind = 'bar', ci= None)
plt.title('Relation between drinking and depressed')


seaborn.distplot(c4); plt.xlabel(' DISTRIBUTION')



