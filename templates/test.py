import json

with open('TableData.json') as f:
  data = json.load(f)

h = ['ved']

for i in data:
	print("<option value=\""+i['state']+"\">"+i['state']+"</option>")

print(h)