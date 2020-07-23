# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 10:50:43 2015

@author: ldierker
"""
import pandas as pd
import numpy
# any additional libraries would be imported here

data = pd.read_csv('f:\\nesarc_pds.csv', low_memory=False)

print (len(data)) #number of observations (rows)
print (len(data.columns)) # number of variables (columns)

#setting variables you will be working with to numeric
# data['TAB12MDX'] = data['TAB12MDX'].convert_objects(convert_numeric=True)
# data['CHECK321'] = data['CHECK321'].convert_objects(convert_numeric=True)
# data['S3AQ3B1'] = data['S3AQ3B1'].convert_objects(convert_numeric=True)
# data['S3AQ3C1'] = data['S3AQ3C1'].convert_objects(convert_numeric=True)
# data['AGE'] = data['AGE'].convert_objects(convert_numeric=True)

#counts and percentages (i.e. frequency distributions) for each variable
c1 = data['S4AQ4A5'].value_counts(sort=False)
print("count of S4AQ4A5-HAD TROUBLE FALLING ASLEEP NEARLY EVERY DAY FOR 2+ WEEK,YES=1 :")
print (c1)

p1 = data['S4AQ4A5'].value_counts(sort=False, normalize=True)
print(" percentage of S2AQ4A5-HAD TROUBLE FALLING ASLEEP NEARLY EVERY DAY FOR 2+ WEEK,YES=1 :")
print (p1)

c2 = data['S4AQ4A12'].value_counts(sort=False)
print("count of S4AQ4A12-FELT WORTHLESS MOST OF THE TIME FOR 2+ WEEK,YES=1 :")
print(c2)
p2 = data['S4AQ4A12'].value_counts(sort=False, normalize=True)
print(" percentage of S4AQ4A12-FELT WORTHLESS MOST OF THE TIME FOR 2+ WEEK,YES=1 :")
print (p2)

c3 = data['S4AQ4A18'].value_counts(sort=False)
print("count of S4AQ4A18 :FELT LIKE WANTED TO DIE,YES=1")
print(c3)

p3 = data['S4AQ4A18'].value_counts(sort=False, normalize=True)
print(" percentage of S4AQ4A18 :FELT LIKE WANTED TO DIE,YES=1")
print (p3)


c4 = data['S4AQ11'].value_counts(sort=False)
print("count of S4AQ11 :ANY EPISODE BEGAN AFTER DRINKING HEAVILY/MORE THAN USUAL")
print(c4)

p4 = data['S4AQ11'].value_counts(sort=False, normalize=True)
print(" percentage of S4AQ11 :ANY EPISODE BEGAN AFTER DRINKING HEAVILY/MORE THAN USUAL")
print (p4)

c5 = data['S4AQ12'].value_counts(sort=False)
print("count of S4AQ12 :ANY EPISODE BEGAN WHEN EXPERIENCING BAD AFTEREFFECTS OF DRINKING")
print(c5)

p5 = data['S4AQ12'].value_counts(sort=False, normalize=True)
print(" percentage of S4AQ12:ANY EPISODE BEGAN WHEN EXPERIENCING BAD AFTEREFFECTS OF DRINKING")
print (p5)

c6 = data['S4AQ20A'].value_counts(sort=False)
print("count of S4AQ20A :EVER DRANK ALCOHOL TO IMPROVE LOW MOOD/MAKE SELF FEEL BETTER")
print(c6)

p6 = data['S4AQ20A'].value_counts(sort=False, normalize=True)
print(" percentage of S4AQ20A :EVER DRANK ALCOHOL TO IMPROVE LOW MOOD/MAKE SELF FEEL BETTER")
print (p6)







# freqeuncy disributions using the 'bygroup' function
ct1= data.groupby('S4AQ4A5').size()
print (ct1)

pt1 = data.groupby('S4AQ4A5').size() * 100 / len(data)
print (pt1)

ct2= data.groupby('S4AQ4A18').size()
print (ct2)

pt2 = data.groupby('S4AQ4A18').size() * 100 / len(data)
print (pt2)

ct3= data.groupby('S4AQ11').size()
print (ct3)

pt3 = data.groupby('S4AQ11').size() * 100 / len(data)
print (pt3)

ct4= data.groupby('S4AQ20A').size()
print (ct4)

pt4 = data.groupby('S4AQ20A').size() * 100 / len(data)
print (pt4)

#subset data to young adults age 18 to 25 who have wanted to die
sub1=data[(data['AGE']>=18) & (data['AGE']<=25) & (data['S4AQ4A18']==1)]

#make a copy of my new subsetted data
sub2 = sub1.copy()

# frequency distritions on new sub2 data frame
print( 'counts for AGE')
c7 = sub2['AGE'].value_counts(sort=False)
print(c7)

print ('percentages for AGE')
p7 = sub2['AGE'].value_counts(sort=False, normalize=True)
print (p7)



#upper-case all DataFrame column names - place afer code for loading data aboave
data.columns = map(str.upper, data.columns)

# bug fix for display formats to avoid run time errors - put after code for loading data above
pd.set_option('display.float_format', lambda x:'%f'%x)


OUTPUT:
  43093
3010
count of S4AQ4A5-HAD TROUBLE FALLING ASLEEP NEARLY EVERY DAY FOR 2+ WEEK,YES=1 :
     29340
1     7422
2     6146
9      185
Name: S4AQ4A5, dtype: int64
 percentage of S2AQ4A5-HAD TROUBLE FALLING ASLEEP NEARLY EVERY DAY FOR 2+ WEEK,YES=1 :
     0.680853
1    0.172232
2    0.142622
9    0.004293
Name: S4AQ4A5, dtype: float64
count of S4AQ4A12-FELT WORTHLESS MOST OF THE TIME FOR 2+ WEEK,YES=1 :
     29340
1     5798
2     7782
9      173
Name: S4AQ4A12, dtype: int64
 percentage of S4AQ4A12-FELT WORTHLESS MOST OF THE TIME FOR 2+ WEEK,YES=1 :
     0.680853
1    0.134546
2    0.180586
9    0.004015
Name: S4AQ4A12, dtype: float64
count of S4AQ4A18 :FELT LIKE WANTED TO DIE,YES=1
     29340
1     4468
2     9163
9      122
Name: S4AQ4A18, dtype: int64
 percentage of S4AQ4A18 :FELT LIKE WANTED TO DIE,YES=1
     0.680853
1    0.103683
2    0.212633
9    0.002831
Name: S4AQ4A18, dtype: float64
count of S4AQ11 :ANY EPISODE BEGAN AFTER DRINKING HEAVILY/MORE THAN USUAL
     34276
1      585
2     8190
9       42
Name: S4AQ11, dtype: int64
 percentage of S4AQ11 :ANY EPISODE BEGAN AFTER DRINKING HEAVILY/MORE THAN USUAL
     0.795396
1    0.013575
2    0.190054
9    0.000975
Name: S4AQ11, dtype: float64
count of S4AQ12 :ANY EPISODE BEGAN WHEN EXPERIENCING BAD AFTEREFFECTS OF DRINKING
     34276
1      383
2     8386
9       48
Name: S4AQ12, dtype: int64
 percentage of S4AQ12:ANY EPISODE BEGAN WHEN EXPERIENCING BAD AFTEREFFECTS OF DRINKING
     0.795396
1    0.008888
2    0.194602
9    0.001114
Name: S4AQ12, dtype: float64
count of S4AQ20A :EVER DRANK ALCOHOL TO IMPROVE LOW MOOD/MAKE SELF FEEL BETTER
     34276
1     1697
2     7094
9       26
Name: S4AQ20A, dtype: int64
 percentage of S4AQ20A :EVER DRANK ALCOHOL TO IMPROVE LOW MOOD/MAKE SELF FEEL BETTER
     0.795396
1    0.039380
2    0.164621
9    0.000603
Name: S4AQ20A, dtype: float64
S4AQ4A5
     29340
1     7422
2     6146
9      185
dtype: int64
S4AQ4A5
     68.085304
1    17.223215
2    14.262177
9     0.429304
dtype: float64
S4AQ4A18
     29340
1     4468
2     9163
9      122
dtype: int64
S4AQ4A18
     68.085304
1    10.368273
2    21.263314
9     0.283109
dtype: float64
S4AQ11
     34276
1      585
2     8190
9       42
dtype: int64
S4AQ11
     79.539600
1     1.357529
2    19.005407
9     0.097464
dtype: float64
S4AQ20A
     34276
1     1697
2     7094
9       26
dtype: int64
S4AQ20A
     79.539600
1     3.937995
2    16.462070
9     0.060335
dtype: float64
counts for AGE
Series([], Name: AGE, dtype: int64)
percentages for AGE
Series([], Name: AGE, dtype: float64)

