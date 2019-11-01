# week 9
#Regular Expressions 

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if (x):
    print("YES! we have a match!")
else:
    print("NO match")


