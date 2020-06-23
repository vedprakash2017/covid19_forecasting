import json

with open('inferenceData.json') as f:

  g1data = json.load(f)

cout = 0;
for i in g1data:
	if i['date'] == '2020-07-02':
		cout+=1
print(cout)