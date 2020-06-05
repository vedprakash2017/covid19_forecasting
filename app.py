from flask import Flask , render_template , request
app = Flask(__name__)

@app.route('/')
def hello_world():
     return render_template('index.html')

@app.route('/my_form', methods=['POST','GET'])
def my_form():
    if request.method == 'POST':
        c6 = int(request.form['c6'])
        c3 = int(request.form['c3'])
        cpl = int(request.form['cpl'])
        x,y = 'stp','wrsmcduo'
        d={}
        for i in y:
            sum=0
            for j in x:
                if len(request.form[j+i])>0:
                    if j=='s':
                        sum=sum+c6*(int(request.form[j+i]))
                    if j=='t':
                        sum=sum+c3*(int(request.form[j+i]))
                    if j=='p':
                        sum=sum+cpl*(int(request.form[j+i]))
            d[i] = sum/1000
        result = {}
        for k,v in d.items():

            if k == 'w':result['Wheat'] = v
            if k == 'r':result['Rice'] = v
            if k == 's':result['Soyabean'] = v
            if k == 'm':result['Murmura'] = v
            if k == 'c':result['Chna'] = v
            if k == 'd':result['Dal'] = v
            if k == 'u':result['Sugar'] = v
            if k == 'o':result['Oil'] = v

        return render_template('res.html',result=result)

if __name__ == '__main__':
     app.debug = True
app.run()
app.run(debug = True)
