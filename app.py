from flask import Flask, Markup, render_template
import json

app = Flask(__name__)
with open('tableData.json') as f:
  data = json.load(f)

#del data[34]


with open('GraphData.json') as f:
  gdata = json.load(f)
g1data = gdata
for i in gdata:
    if i["state"] == 'Total':
        i["cum_confirmed"] = int(i["cum_confirmed"])



print(i["cum_confirmed"])
'''
labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

values = [
    967.67, 1190.89, 1079.75, 1349.19,
    2328.91, 2504.28, 2873.83, 4764.87,
    4349.29, 6458.30, 9907, 16297
]'''
t_c = 0
t_a = 0
t_r = 0
st = ['Andaman and Nicobar Islands','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Daman and Diu','Delhi','Dadra and Nagar Haveli and Daman and Diu','Goa','Gujarat','Himachal Pradesh','Haryana','Jharkhand','Jammu and Kashmir','Karnataka','Kerala','Ladakh','Lakshadweep','Maharashtra','Meghalaya','Manipur','Madhya Pradesh','Mizoram','Nagaland','Odisha','Punjab','Puducherry','Rajasthan','Sikkim','Telangana','Tamil Nadu','Total','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']

for i in data:
    t_c = t_c+int(i['cum_confirmed'])
    t_a = t_a+int(i['cum_active'])
    t_r = t_r+int(i['cum_recovered'])

total = [t_c,t_a,t_r]

d = {'labels':[967.67, 1190.89, 1079.75, 1349.19,2328.91, 2504.28, 2873.83, 4764.87,4349.29, 6458.30, 9907, 16297],'values':[967.67, 1190.89, 1079.75, 1349.19,2328.91, 2504.28, 2873.83, 4764.87,4349.29, 6458.30, 9907, 16297]}
@app.route('/')
def line():
    line_labels=d['labels']
    line_values=d['values']
    return render_template('graph.html', title='Covid19', max=17000, labels=line_labels, values=line_values,table = data,total = total,gdata = gdata,st = st,g1data = g1data)

if __name__ == '__main__':
    app.run()