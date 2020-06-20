import json

with open('TableData.json') as f:
  data = json.load(f)

h = ['ved']

for i in data:
	print('\''+i['state']+'\'',end=',')

print(h)