import pickle
from flask import Flask, request, app, jsonify,render_template 
from urllib.parse import quote

import numpy as np 
import pandas as pd 

app = Flask(__name__)


import os

# Use relative path
model_path = os.path.join("boston_house_price_prediction_model.pkl")

# Load the model
try:
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    print(f"File not found: {model_path}")
    
# Use relative path
scaler_path = os.path.join("boston_house_price_prediction_scaler.pkl")

# Load the model
try:
    with open(scaler_path, 'rb') as file:
        scaler = pickle.load(file)
except FileNotFoundError:
    print(f"File not found: {scaler_path}")
    



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    
    data = request.json['data']
    print(data)
    prediction = model.predict(scaler.transform(pd.DataFrame(data,index=[0])))
    output = prediction[0]
    return jsonify(output)

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(scaler.transform(final_features))
    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text='House price should be $ {}'.format(output))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

    