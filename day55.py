# weeek 9

import json 

x = '{"name":"huda", "id":200, "city":"khobar"}'


y= json.loads(x)


z = json.dumps(y)
print(x)
print(y['name'])
print(z)