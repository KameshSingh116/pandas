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