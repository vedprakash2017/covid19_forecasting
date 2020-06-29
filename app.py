from flask import Flask, Markup, render_template
import json
import copy
# import DailyDataJson
# import InferenceForecastDataJson
import time
# import atexit
# from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

# def change_data():
#     DailyDataJson.dd()
#     InferenceForecastDataJson.ifd(0.3)
#     InferenceForecastDataJson.ifd(0.4)
#     InferenceForecastDataJson.ifd(0.5)
#     InferenceForecastDataJson.ifd(0.6)
#     InferenceForecastDataJson.ifd(0.7)
#     InferenceForecastDataJson.ifd(0.8)


# scheduler = BackgroundScheduler()
# scheduler.add_job(func=change_data, trigger="cron", hour='00', minute='30')
# scheduler.start()

# # Shut down the scheduler when exiting the app
# atexit.register(lambda: scheduler.shutdown())
b_values = ['0.3','0.4','0.5','0.7','0.6','0.8']

tfbdata={}
fbdata = {}
f1bdata = {}
f1b1junedata = {}

f_data = {}

f1_data = {}
f1_1junedata = {}
g1_data = {}

g_data = {}

with open('TotalData.json') as f:
  tdata = json.load(f)

with open('tableData.json') as f:
  data = json.load(f)

with open('GraphData.json') as f:
  gdata = json.load(f)

t_c = tdata[0]['cum_confirmed']
t_a = tdata[0]['cum_active']
t_r = tdata[0]['cum_recovered']

st = ['Andaman and Nicobar Islands','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Daman and Diu','Delhi','Dadra and Nagar Haveli and Daman and Diu','Goa','Gujarat','Himachal Pradesh','Haryana','Jharkhand','Jammu and Kashmir','Karnataka','Kerala','Ladakh','Lakshadweep','Maharashtra','Meghalaya','Manipur','Madhya Pradesh','Mizoram','Nagaland','Odisha','Punjab','Puducherry','Rajasthan','Sikkim','Telangana','Tamil Nadu','Total','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']
l = []





for j in st:
    for i in gdata:
        if i['state'] == j:
            l.append([i['date'],i['cum_confirmed'],i['cum_active'],i['cum_recovered']])
    g_data[j] = l
    l = []
l = []

for b in b_values:
    f1_data[b] = {}
    f1_1junedata[b] = {}

for b in b_values:
    with open('ForecastData'+b+'.json') as f:
        tfbdata[b] = json.load(f)
  
    with open('ForecastGData'+b+'.json') as f:
        fbdata[b] = json.load(f)

    with open('InferenceData'+b+'.json') as f:
        f1bdata[b] = json.load(f)

    with open('InferenceData1June'+b+'.json') as f:
        f1b1junedata[b] = json.load(f)

    for j in st:
        for i in f1bdata[b]:
            if i['state'] == j:
                if i['active'] <0:
                    i['active'] = 'null'
                if i['recovered'] <0:
                    i['recovered'] = 'null'
                l.append([i['date'],i['active'],i['recovered']])
        f1_data[b][j] = l
        l = []
    l = []

    for j in st:
        for i in f1b1junedata[b]:
            if i['state'] == j:
                if i['active'] <0:
                    i['active'] = 'null'
                if i['recovered'] <0:
                    i['recovered'] = 'null'
                l.append([i['date'],i['active'],i['recovered']])
        f1_1junedata[b][j] = l
        l = []
    l = []

    
    f_data[b] = copy.deepcopy(g_data)
    g1_data[b] = copy.deepcopy(f1_data[b])
    
    for j in st:
        for i in fbdata[b]:
            if i['state'] == j:
                f_data[b][j].append([i['date'],i['cum_confirmed'],i['cum_active'],i['cum_recovered']])

    for i in g1_data[b].keys():
        if(len(g1_data[b][i]) != 0):
            for j in range(15):
                g1_data[b][i].pop()
            for j in range(15):
                g1_data[b][i].append(['null','null','null'])
        else:
            for j in range(15):
                g1_data[b][i].append(['null','null','null'])




# with open('ForecastData0.7.json') as f:
#   tfdata = json.load(f)
  
# with open('ForecastGData0.7.json') as f:
#   fdata = json.load(f)

# with open('InferenceData0.7.json') as f:
#   f1data = json.load(f)

B_all_data = [tfbdata,f_data,g1_data,f1_data,tfbdata,f1_1junedata]





# f_data = copy.deepcopy(g_data)
# g1_data = copy.deepcopy(f1_data)


# for j in st:
#     for i in fdata:
#         if i['state'] == j:
#             f_data[j].append([i['date'],i['cum_confirmed'],i['cum_active'],i['cum_recovered']])

for i in g_data.keys():
    for j in range(11):
        g_data[i].append(['null','null','null','null'])

# for i in g1_data.keys():
#     if(len(g1_data[i]) != 0):
#         for j in range(11):
#             g1_data[i].pop()
#         for j in range(11):
#             g1_data[i].append(['null','null','null'])
#     else:
#         for j in range(11):
#             g1_data[i].append(['null','null','null'])

# for i in data:
#     t_c = t_c+int(i['cum_confirmed'])
#     t_a = t_a+int(i['cum_active'])
#     t_r = t_r+int(i['cum_recovered'])
total = [t_c,t_a,t_r]
# tav = "<tr><td>{{ day }}</td><td class='freq'>'{{i['cum_confirmed']}}'</td><td class='freq'>'{{i['cum_active']}}'</td><td class='freq'>'{{i['cum_recovered']}}'</td></tr><tfoot><tr><td></td><td></td><td></td><td></td></tr></tfoot>"

@app.route('/')
def line():
    return render_template('graph.html', title='Covid19',table1 = data,total = total,st = st,gdata = g_data,alldata = B_all_data,b_all = b_values)
# g1data = g1_data,fdata = f_data,f1data = f1_data,
if __name__ == '__main__':
    app.run(threaded=True)