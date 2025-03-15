#Radhe Radhe
#Data Frames in pandas

import pandas as pd

data={
    "Name":['Deviji','Kamesh','Ritish','Shivangi'],
    "Age":[19,29,20,19],
    "City":['Mera Dill','Kanhaji ke charan','jammu','jammu']
}

frame=pd.DataFrame(data)

print(frame)

#OUTPUT
#        Name  Age               City
# 0    Deviji   19          Mera Dill
# 1    Kamesh   29  Kanhaji ke charan
# 2    Ritish   20              jammu
# 3  Shivangi   19              jammu