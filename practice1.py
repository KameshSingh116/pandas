#Radhe Radhe
 #1 Select 'Name' for rows 'A' and 'C' or '1' and '3'.

import pandas as pd
data={
    "Name":['Deviji','Kamesh','Ritish','Shivangi'],
    "Age":[19,29,20,19],
    "City":['Mera Dill','Kanhaji ke charan','jammu','jammu']
}
frame=pd.DataFrame(data)

print(frame.loc[[0,2],'Name'])

#OUTPUT:
# 0    Deviji
# 2    Ritish
# Name: Name, dtype: object

#2 Select first two rows and first two columns.

print(frame.iloc[0:2,0:2])

#OUTPUT:
#      Name  Age
# 0  Deviji   19
# 1  Kamesh   29