# week 9
#Python RegEx 3 
#The sub() Function 

import re
#replace all white- space character with  the digit "9":

str = "The rain in Spain"
x = re.sub("\s", "9", str)
print(x)

