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