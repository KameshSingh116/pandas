#Radhe Radhe
#Modifying Data

import pandas as pd
data={
    "Name":['Deviji','Kamesh','Ritish','Shivangi'],
    "Age":[19,29,20,19],
    "City":['Mera Dill','Kanhaji ke charan','jammu','jammu']
}
frame=pd.DataFrame(data)

# frame.at[[1,'Age']]=20

# print(frame)

#Output
#        Name  Age               City
# 0    Deviji   19          Mera Dill
# 1    Kamesh   20  Kanhaji ke charan
# 2    Ritish   20              jammu
# 3  Shivangi   19              jammu
#The age of Kamesh was changed from 29 to 20.
#We can also use update method to change the values of a dataframe.

frame.update(pd.DataFrame({'Age':[30,40,50,60]}))
print(frame)

#Output
#        Name  Age               City
# 0    Deviji   30          Mera Dill
# 1    Kamesh   40  Kanhaji ke charan
# 2    Ritish   50              jammu
# 3  Shivangi   60              jammu


#We can check two different forms by uncommenting the code.
