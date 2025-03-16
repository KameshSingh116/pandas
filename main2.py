#Radhe Radhe 
#Dataframe operations.

import pandas as pd

data={
    "Name":['Deviji','Kamesh','Ritish','Shivangi'],
    "Age":[19,29,20,19],
    "City":['Mera Dill','Kanhaji ke charan','jammu','jammu']
}

frame=pd.DataFrame(data)

print(frame['Name'])

#OUTPUT
# 0      Deviji
# 1      Kamesh
# 2      Ritish
# 3    Shivangi
# Name: Name, dtype: object

#If we want to display more than one column then we can use the following syntax:
print(frame[['Name','Age']])

#OUTPUT
#        Name  Age
# 0    Deviji   19
# 1    Kamesh   29
# 2    Ritish   20
# 3  Shivangi   19