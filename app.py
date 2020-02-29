# app.py
from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

# prediction function 
def ValuePredictor(to_predict_list): 
    to_predict = np.array(to_predict_list).reshape(1, -1) 
    print(to_predict)
    loaded_model = pickle.load(open("model1.pkl", "rb")) 
    result = loaded_model.predict(to_predict) 
    return result[0] 
@app.route('/') 
def index():
	return render_template("index.html")
@app.route('/result', methods = ['POST']) 
def result(): 
    if request.method == 'POST': 
        to_predict_list = request.form.to_dict() 
        to_predict_list = list(to_predict_list.values()) 
        to_predict_list = list(map(int, to_predict_list)) 
        result = ValuePredictor(to_predict_list)         
        if int(result)== 1: 
            prediction ='Genuine'
        else: 
            prediction ='fraud'            
        return render_template("result.html", prediction = prediction)

if __name__ == '__main__':
    app.run()