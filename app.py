from flask import Flask,render_template, request
import numpy as np
import pickle

model2=pickle.load(open('ad_hospitalizado.pkl','rb'))

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def new():
    return render_template('new.html')

@app.route('/predict', methods=['POST','GET'] )
def predict():
    data1=int(request.form['a'])
    data2=int(request.form['b'])
    data3=int(request.form['c'])
    data4=int(request.form['d'])
    data5=int(request.form['e'])
    data6=int(request.form['f'])
    data7=int(request.form['g'])
    data8=int(request.form['h'])
    data9=int(request.form['i'])
    data10=int(request.form['j'])
    data11=int(request.form['k'])
    data12=int(request.form['l'])
    data13=int(request.form['m'])
    data14=int(request.form['n'])
    data15=int(request.form['o'])
    data16=int(request.form['p'])
    features=np.array([data1,data2,data3,data4+data5+data6+data7+data8,data9+data10,data11+data12+data13,data14+data15+data16])
    pred = model2.predict([features])
    
    def statement():
        if pred == 1:
                        return 'Resultado: El modelo ha pronosticado con un 87% de exactitud que los síntomas descritos no conllevan una hospitalización pero debe cuidarse.'
        elif pred == 2:
            return 'El modelo ha pronosticado con un 87% de exactitud que los síntomas descritos conllevan una hospitalización.'
    return render_template('new.html',statement=statement())


if __name__=='__main__':
    app.run()