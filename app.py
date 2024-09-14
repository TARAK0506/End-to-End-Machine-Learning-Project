import pickle
from flask import Flask, request, app, jsonify,url_for,redirect,render_template

import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the model
model = pickle.load(open(r'C:\Users\tarak\Downloads\Data Science\Machine Learning\Regression\Boston House Price Prediction\Notebook\boston_house_price_prediction_model.pkl','rb'))
scaler = pickle.load(open(r'C:\Users\tarak\Downloads\Data Science\Machine Learning\Regression\Boston House Price Prediction\Notebook\boston_house_price_prediction_scaler.pkl','rb'))
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

if __name__ == "__main__":
    app.run(debug=True)
    