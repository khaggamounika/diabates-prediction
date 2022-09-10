from flask import Flask,render_template,request
import pickle

model=pickle.load(open('model.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def homePage():
    return (render_template('index.html'))

@app.route('/predict',methods=['POST'])
def collectData():
    P=float(request.form['P'])
    G=float(request.form['G'])
    B=float(request.form['B'])
    S=float(request.form['S'])
    I=float(request.form['I'])
    BM=float(request.form['BM'])
    D=float(request.form['D'])
    A=float(request.form['A'])
    print(P,G,B,S,I,BM,D,A)
    result=model.predict([[P,G,B,S,I,BM,D,A]])
    return(str(result[0]))


if __name__=="__main__":
    app.run(debug=True)