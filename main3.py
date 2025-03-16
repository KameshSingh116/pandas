#Radhe Radhe
#Selecting Rows using loc and iloc

#1)We use loc[] when selecting rows based on labels.

import pandas as pd

data={
    "Name":['Deviji','Kamesh','Ritish','Shivangi'],
    "Age":[19,29,20,19],
    "City":['Mera Dill','Kanhaji ke charan','jammu','jammu']
}

frame=pd.DataFrame(data)

print(frame.loc[0])
print(frame.loc[1])

#OUTPUT
# Name       Deviji
# Age            19
# City    Mera Dill
# Name: 0, dtype: object
# Name               Kamesh
# Age                    29
# City    Kanhaji ke charan
# Name: 1, dtype: object

#For multiple rows
print(frame.loc[0:1])

#      Name  Age               City
# 0  Deviji   19          Mera Dill
# 1  Kamesh   29  Kanhaji ke charan


#2)We use iloc[] when selecting rows based on index.

print(frame.iloc[0])


#OUTPUT
# Name       Deviji
# Age            19
# City    Mera Dill
# Name: 0, dtype: object

#For loc[] , we use labels as a reference to select rows.
#For iloc[], we use index as a reference to select rows.
#Radhe Radhe