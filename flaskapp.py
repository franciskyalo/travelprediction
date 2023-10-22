import pandas as pd
import numpy as np
import pickle
import joblib
from flask import Flask, request, jsonify, render_template
from sklearn.base import BaseEstimator, TransformerMixin
from pipeline import ConvertColumnsTransformer

app = Flask(__name__)

# Load the pickle model
model = pickle.load(open('model.pkl', 'rb'))

# load the pipeline

pipeline = joblib.load('preproc_pipeline.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    Age = float(request.form['Age'])
    Employment_type = str(request.form['Employment Type'])
    Graduateornot = str(request.form['GraduateOrNot'])
    Annualincome = float(request.form['AnnualIncome'])
    Familymembers = float(request.form['FamilyMembers'])
    Chronicdiseases = str(request.form['ChronicDiseases'])
    Frequentflyer = str(request.form['FrequentFlyer'])
    Evertravelledabroad = str(request.form['EverTravelledAbroad'])

    # Create a DataFrame from the input values
    query_df = np.array([[Age, Employment_type, Graduateornot, AnnulIncome,Familymembers, Chronicdiseases, Frequentflyer, Evertravelledabroad]])
    
    df = pipeline.fit_tranform(query_df)

    # Make the prediction using the loaded model
    prediction = model.predict(df)
    predicted_class = prediction[0]

    return render_template('index.html', prediction_text=f'Predicted class: {predicted_class}')

if __name__ == '__main__':
    app.run(debug=True)