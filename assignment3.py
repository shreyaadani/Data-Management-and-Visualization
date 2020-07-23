# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 22:39:14 2020

@author: Shreyaa Dani
"""


#On the topic I have selected, the program would be:


import pandas as pd
import numpy as np


data = pd.read_csv('f:\\nesarc_pds.csv', low_memory=False)

sub = data[data['S1Q213'] <= 1]
# a copy of dataset where undesired data has been removed

c4 = data['S1Q213'].value_counts(dropna = False)
d4 =  sub['S1Q213'].value_counts(dropna = False)
print(f"DURING PAST 4 WEEKS, HOW OFTEN FELT DOWNHEARTED AND DEPRESSED:")
print('BEFORE:')
print(c4)
print('AFTER')
print(d4)

print("-"*42)

d3=data['S4AQ4A18'].value_counts(dropna = False)
c1 = sub['S4AQ4A18'].value_counts(dropna = False)
print(f"\WANTED TO DIE, YES=1:" )
print('BEFORE:')
print(d3)
print('AFTER')
print(c1)




d3=data['S4AQ11'].value_counts(dropna = False)
c1 = sub['S4AQ11'].value_counts(dropna = False)
#sub['S4AQ11'] = sub['S4AQ11' ].replace(i, np.nan) #refused, dont know and not applicable converted to NaN
print(f"\ANY EPISODE BEGAN AFTER DRINKING HEAVILY/MORE THAN USUAL" )
print('BEFORE:')
print(d3)
print('AFTER')
print(c1)




d3=data['S7Q31B '].value_counts(dropna = False)
c1 = sub['S7Q31B '].value_counts(dropna = False)
#sub['S7Q31B '] = sub['S7Q31B ].replace(i, np.nan) #refused, dont know and not applicable converted to NaN
print(f"\DRANK ALCOHOL TO AVOID SOCIAL PHOBIA IN LAST 12 MONTHS YES=1" )
print('BEFORE:')
print(d3)
print('AFTER')
print(c1)


OUTPUT:
  DURING PAST 4 WEEKS, HOW OFTEN FELT DOWNHEARTED AND DEPRESSED:
BEFORE:
5    22127
4    11305
3     6286
2     2051
1      907
9      417
Name: S1Q213, dtype: int64
AFTER
1    907
Name: S1Q213, dtype: int64
------------------------------------------
\WANTED TO DIE, YES=1:
BEFORE:
     29340
2     9163
1     4468
9      122
Name: S4AQ4A18, dtype: int64
AFTER
1    326
     325
2    245
9     11
Name: S4AQ4A18, dtype: int64
\ANY EPISODE BEGAN AFTER DRINKING HEAVILY/MORE THAN USUAL
BEFORE:
     34276
2     8190
1      585
9       42
Name: S4AQ11, dtype: int64
AFTER
     447
2    419
1     38
9      3
Name: S4AQ11, dtype: int64
\DRANK ALCOHOL TO AVOID SOCIAL PHOBIA IN LAST 12 MONTHS YES=1
BEFORE:
     37682
2     5223
1      148
9       40
Name: S7Q31B, dtype: int64
AFTER
     723
2    169
1     12
9      3
Name: S7Q31B, dtype: int64



