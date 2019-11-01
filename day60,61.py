# challeng of week 9


import json

colors = ('blue', 'grey', 'green', 'red', 'orange', 'yellow')

print(colors)

colors = json.dumps(colors)
print(type(colors))
print(colors)

########################
import re 
text = 'Data is the new oil'

x = re.search("Data", text)
print(f'the word (Data) is in index #{x.start()}')
