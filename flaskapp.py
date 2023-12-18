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

#
# Define the column_fct and categorical_cols variables
column_fct = ["ChronicDiseases"]
categorical_cols = ["Employment Type", "GraduateOrNot", "ChronicDiseases", "FrequentFlyer", "EverTravelledAbroad"]
numeric_cols = ["Age","AnnualIncome","FamilyMembers"]


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
    query_df = pd.DataFrame([[Age, Employment_type, Graduateornot, Annualincome, Familymembers, Chronicdiseases, Frequentflyer, Evertravelledabroad]],
                            columns=["Age", "Employment Type", "GraduateOrNot", "AnnualIncome", "FamilyMembers", "ChronicDiseases", "FrequentFlyer", "EverTravelledAbroad"])
    
    print("query_df shape:", query_df.shape)
    
    df = pipeline.transform(query_df)
    

    # Make the prediction using the loaded model
    prediction = model.predict(df)
    predicted_class = prediction[0]
    
    if predicted_class == 1:
        prediction_text = "The customer will buy travel insurance."
    else:
        prediction_text = "The customer will not buy travel insurance."

    return render_template('index.html', prediction_text=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)