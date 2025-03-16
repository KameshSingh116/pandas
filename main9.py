#Radhe Radhe
# Removing Missing Values
# Removing rows with missing values (dropna())


import pandas as pd
import numpy as np

data={
    "Name":['Deviji','Kamesh','Ritish','Shivangi'],
    "Age":[19,np.nan,np.nan,19],
    "City":['Mera Dill','Kanhaji ke charan','jammu','jammu']
}
frame=pd.DataFrame(data)
print(frame)

#output
#        Name   Age               City
# 0    Deviji  19.0          Mera Dill
# 1    Kamesh   NaN  Kanhaji ke charan
# 2    Ritish   NaN              jammu
# 3  Shivangi  19.0              jammu

# we will use dropna() method to remove rows with missing values
# frame.dropna(inplace=True)
# #inplace=True will modify the original dataframe
# print(frame)

print(frame.dropna(inplace=True)) #None