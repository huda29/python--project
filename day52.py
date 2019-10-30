#Python Datetime

import datetime

x = datetime.datetime.now()
print(x)

#Return the year and name of weekday
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))




#Creating Date Objects
import datetime 
x = datetime.datetime(2020, 5, 17)
print(x)


#The strftime() Method 
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))