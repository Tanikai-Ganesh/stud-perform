from flask import Flask, request, render_template,jsonify
import random  # For demo purposes; replace with actual ML model
import numpy as np
import pandas as pd
import os
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application = Flask(__name__)

@application.route('/')
def home():
    return render_template('index.html')

@application.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    if request.method == 'POST':
        # Get form data

        gender = request.form.get('gender'),
        ethnicity = request.form.get('ethnicity'),
        parental_education = request.form.get('parental_level_of_education'),
        lunch = request.form.get('lunch'),
        test_prep = request.form.get('test_preparation_course'),
        reading_score=float(request.form.get('writing_score')),
        writing_score=float(request.form.get('reading_score'))

        # Basic validation
        if not all([gender, ethnicity, parental_education, lunch, test_prep,reading_score,writing_score]):
            return jsonify({'error': 'All fields are required'}), 400

        data = CustomData(
                gender,ethnicity,parental_education,lunch,test_prep,reading_score,writing_score
        )
        

        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")

        # Demo prediction (replace with actual ML model logic)
        predicted_score = predict_pipeline.predict(pred_df)

        print("after Prediction")
        
        return jsonify({'prediction': predicted_score[0]})
    
    return jsonify({'error': 'Method not allowed'}), 405

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8080,debug=True)