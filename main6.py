#Radhe Radhe
# Adding a new column to the dataframe

import pandas as pd

data={
    "Name":['Deviji','Kamesh','Ritish','Shivangi'],
    "Age":[19,29,20,19],
    "City":['Mera Dill','Kanhaji ke charan','jammu','jammu']
}

frame=pd.DataFrame(data)
#Adding a new column

frame['Gender']=['F','M','M','F']
print(frame)
#OUTPUT
#        Name  Age               City Gender
# 0    Deviji   19          Mera Dill      F       
# 1    Kamesh   29  Kanhaji ke charan      M       
# 2    Ritish   20              jammu      M       
# 3  Shivangi   19              jammu      F 

#Radhe Radhe