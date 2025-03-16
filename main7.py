#Radhe Radhe
#Removing a column from the dataframe

import pandas as pd

data={
    "Name":['Deviji','Kamesh','Ritish','Shivangi'],
    "Age":[19,29,20,19],
    "City":['Mera Dill','Kanhaji ke charan','jammu','jammu']
}

frame=pd.DataFrame(data)

frame.drop('Age',axis=1,inplace=True)
print(frame)

frame.drop(columns='City',inplace=True)
print(frame)

#axis=1 means column and axis=0 means row
#Radhe Radhe    