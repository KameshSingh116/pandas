#Radhe Radhe
#  Forward Fill (ffill) and Backward Fill (bfill)
# Instead of a fixed value, we can propagate values from nearby data.

import pandas as  pd
import numpy as np

data={
    "Name":['Deviji','Kamesh','Ritish','Shivangi'],
    "Age":[19,np.nan,20,19],
    "City":['Mera Dill','Kanhaji ke charan','jammu','jammu']
}

frame=pd.DataFrame(data)
print(frame)

# frame.fillna(method='ffill',inplace=True)
# print(frame)

# C:\Users\lenovo\Desktop\pandas\pandas\main12.py:16: FutureWarning: DataFrame.fillna with 'method' is deprecated and will raise in a future version. Use obj.ffill() or obj.bfill() instead.
#   frame.fillna(method='ffill',inplace=True)      
#        Name   Age               City
# 0    Deviji  19.0          Mera Dill
# 1    Kamesh  19.0  Kanhaji ke charan
# 2    Ritish  20.0              jammu
# 3  Shivangi  19.0              jammu
# C:\Users\lenovo\Desktop\pandas\pandas\main12.py:19: FutureWarning: DataFrame.fillna with 'method' is deprecated and will raise in a future version. Use obj.ffill() or obj.bfill() instead.
#   frame.fillna(method='bfill',inplace=True)      
#        Name   Age               City
# 0    Deviji  19.0          Mera Dill
# 1    Kamesh  19.0  Kanhaji ke charan
# 2    Ritish  20.0              jammu
# 3  Shivangi  19.0              jammu


frame.fillna(method='bfill',inplace=True)
print(frame)

#        Name   Age               City
# 0    Deviji  19.0          Mera Dill
# 1    Kamesh   NaN  Kanhaji ke charan
# 2    Ritish  20.0              jammu
# 3  Shivangi  19.0              jammu
# C:\Users\lenovo\Desktop\pandas\pandas\main12.py:36: FutureWarning: DataFrame.fillna with 'method' is deprecated and will raise in a future version. Use obj.ffill() or obj.bfill() instead.
#   frame.fillna(method='bfill',inplace=True)      
#        Name   Age               City
# 0    Deviji  19.0          Mera Dill
# 1    Kamesh  20.0  Kanhaji ke charan
# 2    Ritish  20.0              jammu
# 3  Shivangi  19.0              jammu

#We  can see different workings off different functions in the code above by removing or managing the comments.

#Radhe Radhe