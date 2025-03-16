#Radhe Radhe
# Filtering Data with Conditions

import pandas as pd
data={
    "Name":['Deviji','Kamesh','Ritish','Shivangi'],
    "Age":[19,29,20,19],
    "City":['Mera Dill','Kanhaji ke charan','jammu','jammu']
}

frame=pd.DataFrame(data)
filtered=frame[frame['Age']>19]

print(f'Filtered Data:{filtered}')
#OUTPUT
# Filtered Data:
#    Name    Age               City
# 1  Kamesh   29  Kanhaji ke charan
# 2  Ritish   20              jammu


filtered1=frame[(frame['Age']>19) & (frame['City']=='Kanhaji ke charan')]
print("Filtered Data1:")
print(filtered1)

#OUTPUT
# Filtered Data1:
#      Name  Age               City
# 1  Kamesh   29  Kanhaji ke charan
