#Radhe Radhe
# Filling Missing Values in Pandas (fillna())
# Instead of dropping missing values, you can replace them with meaningful values using .fillna().

import pandas as pd
import numpy as np

data={
    "Name":['Deviji','Kamesh','Ritish','Shivangi'],
    "Age":[19,np.nan,np.nan,19],
    "City":['Mera Dill','Kanhaji ke charan','jammu','jammu']
}

frame=pd.DataFrame(data)
print("Original DataFrame")
print(frame)

#Output:    
#        Name   Age               City
# 0    Deviji  19.0          Mera Dill
# 1    Kamesh   NaN  Kanhaji ke charan
# 2    Ritish   NaN              jammu
# 3  Shivangi  19.0              jammu

#filling missing values with 0
frame.fillna(00,inplace=True)
print("DataFrame after filling missing values with 0")
print(frame)
