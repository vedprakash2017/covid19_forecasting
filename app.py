from flask import Flask, Markup, render_template
import json
import copy
app = Flask(__name__)
with open('tableData.json') as f:
  data = json.load(f)

#del data[34]


with open('GraphData.json') as f:
  gdata = json.load(f)

with open('ForecastData.json') as f:
  fdata = json.load(f)

t_c = 0
t_a = 0
t_r = 0
st = ['Andaman and Nicobar Islands','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Daman and Diu','Delhi','Dadra and Nagar Haveli and Daman and Diu','Goa','Gujarat','Himachal Pradesh','Haryana','Jharkhand','Jammu and Kashmir','Karnataka','Kerala','Ladakh','Lakshadweep','Maharashtra','Meghalaya','Manipur','Madhya Pradesh','Mizoram','Nagaland','Odisha','Punjab','Puducherry','Rajasthan','Sikkim','Telangana','Tamil Nadu','Total','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']
l = []
g_data = {}
for j in st:
    for i in gdata:
        if i['state'] == j:
            l.append([i['date'],i['cum_confirmed'],i['cum_active'],i['cum_recovered']])
    g_data[j] = l
    l = []

length = len(g_data['Bihar'])

f_data = copy.deepcopy(g_data)

for j in st:
    for i in fdata:
        if i['state'] == j:
            f_data[j].append([i['date'],i['cum_confirmed'],i['cum_active'],i['cum_recovered']])

g1_data   = g_data 

for i in g_data.keys():
    for j in range(11):
        g_data[i].append(['null','null','null','null'])

for i in data:
    t_c = t_c+int(i['cum_confirmed'])
    t_a = t_a+int(i['cum_active'])
    t_r = t_r+int(i['cum_recovered'])
total = [t_c,t_a,t_r]
@app.route('/')
def line():
    return render_template('graph.html', title='Covid19',table = data,total = total,gdata = g_data,st = st,g1data = g1_data,fdata = f_data)

if __name__ == '__main__':
    app.run()