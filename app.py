from flask import Flask, Markup, render_template

app = Flask(__name__)
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

d = {'labels':[967.67, 1190.89, 1079.75, 1349.19,2328.91, 2504.28, 2873.83, 4764.87,4349.29, 6458.30, 9907, 16297],'values':[967.67, 1190.89, 1079.75, 1349.19,2328.91, 2504.28, 2873.83, 4764.87,4349.29, 6458.30, 9907, 16297]}
@app.route('/')
def line():
    line_labels=d['labels']
    line_values=d['values']
    return render_template('line_chart.html', title='Covid19', max=17000, labels=line_labels, values=line_values)

if __name__ == '__main__':
    app.run()