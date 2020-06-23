from flask import Flask, Markup, render_template
import json
import copy
app = Flask(__name__)


with open('tableData.json') as f:
  data = json.load(f)

with open('GraphData.json') as f:
  gdata = json.load(f)

with open('ForecastData.json') as f:
  fdata = json.load(f)

with open('inferenceData.json') as f:
  f1data = json.load(f)


t_c = 0
t_a = 0
t_r = 0
st = ['Andaman and Nicobar Islands','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Daman and Diu','Delhi','Dadra and Nagar Haveli and Daman and Diu','Goa','Gujarat','Himachal Pradesh','Haryana','Jharkhand','Jammu and Kashmir','Karnataka','Kerala','Ladakh','Lakshadweep','Maharashtra','Meghalaya','Manipur','Madhya Pradesh','Mizoram','Nagaland','Odisha','Punjab','Puducherry','Rajasthan','Sikkim','Telangana','Tamil Nadu','Total','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']
l = []
g_data = {}
f1_data = {}

for j in st:
    for i in gdata:
        if i['state'] == j:
            l.append([i['date'],i['cum_confirmed'],i['cum_active'],i['cum_recovered']])
    g_data[j] = l
    l = []

l = []

for j in st:
    for i in f1data:
        if i['state'] == j:
            if i['active'] <0:
                i['active'] = 'null'
            if i['recovered'] <0:
                i['recovered'] = 'null'

            l.append([i['date'],i['active'],i['recovered']])
    f1_data[j] = l
    l = []
l = []



f_data = copy.deepcopy(g_data)
g1_data = copy.deepcopy(f1_data)


for j in st:
    for i in fdata:
        if i['state'] == j:
            f_data[j].append([i['date'],i['cum_confirmed'],i['cum_active'],i['cum_recovered']])

for i in g_data.keys():
    for j in range(11):
        g_data[i].append(['null','null','null','null'])

for i in g1_data.keys():
    if(len(g1_data[i]) != 0):
        for j in range(11):
            g1_data[i].pop()
        for j in range(11):
            g1_data[i].append(['null','null','null'])
    else:
        for j in range(11):
            g1_data[i].append(['null','null','null'])

for i in data:
    t_c = t_c+int(i['cum_confirmed'])
    t_a = t_a+int(i['cum_active'])
    t_r = t_r+int(i['cum_recovered'])


total = [t_c,t_a,t_r]
# tav = "<tr><td>{{ day }}</td><td class='freq'>'{{i['cum_confirmed']}}'</td><td class='freq'>'{{i['cum_active']}}'</td><td class='freq'>'{{i['cum_recovered']}}'</td></tr><tfoot><tr><td></td><td></td><td></td><td></td></tr></tfoot>"

@app.route('/')
def line():
    return render_template('graph.html', title='Covid19',table1 = data,table2 = fdata,total = total,st = st,gdata = g_data,g1data = g1_data,fdata = f_data,f1data = f1_data)

if __name__ == '__main__':
    app.run()