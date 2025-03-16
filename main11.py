#Raddhe Radhe
#Mean , Median and Mode in Pandas

import pandas as pd
import numpy as np

data={
    "Name":['Deviji','Kamesh','Ritish','Shivangi'],
    "Age":[19,29,20,19],
    "City":['Mera Dill','Kanhaji ke charan','jammu','jammu']
}   

frame=pd.DataFrame(data)
print("Original DataFrame")
print(frame)


frame['Age'].fillna(frame['Age'].mean(),inplace=True)
print("DataFrame after filling missing values with mean")
print(frame)
#output

# Original DataFrame
#        Name  Age               City
# 0    Deviji   19          Mera Dill
# 1    Kamesh   29  Kanhaji ke charan
# 2    Ritish   20              jammu
# 3  Shivangi   19              jammu
# C:\Users\lenovo\Desktop\pandas\pandas\main11.py:18: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.
# The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.

# For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.


#   frame['Age'].fillna(frame['Age'].mean(),inplace=True)
# DataFrame after filling missing values with mean 
#        Name  Age               City
# 0    Deviji   19          Mera Dill
# 1    Kamesh   29  Kanhaji ke charan
# 2    Ritish   20              jammu
# 3  Shivangi   19              jammu

