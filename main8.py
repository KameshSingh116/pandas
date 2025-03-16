#Radhe #Radhe
#Detecting Missing Values in Dataframe
# Checking for missing values using .isna() or .isnull()

import pandas as pd
import numpy as np

data={
    "Name":['Deviji','Kamesh','Ritish','Shivangi'],
    "Age":[19,29,np.nan,19],
    "City":['Mera Dill','Kanhaji ke charan','jammu','jammu']
}

frame=pd.DataFrame(data)

print(frame)

#output
#        Name   Age               City
# 0    Deviji  19.0          Mera Dill
# 1    Kamesh  29.0  Kanhaji ke charan
# 2    Ritish   NaN              jammu
# 3  Shivangi  19.0              jammu

print(frame.isna())

#output
#    Name    Age   City
# 0  False  False  False
# 1  False  False  False
# 2  False   True  False
# 3  False  False  False