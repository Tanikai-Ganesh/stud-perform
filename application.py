from flask import Flask, request, render_template,jsonify
import random  # For demo purposes; replace with actual ML model

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
        gender = request.form.get('gender')
        ethnicity = request.form.get('ethnicity')
        parental_education = request.form.get('parental_level_of_education')
        lunch = request.form.get('lunch')
        test_prep = request.form.get('test_preparation_course')

        # Basic validation
        if not all([gender, ethnicity, parental_education, lunch, test_prep]):
            return jsonify({'error': 'All fields are required'}), 400

        # Demo prediction (replace with actual ML model logic)
        predicted_score = random.randint(0, 100)
        
        return jsonify({'prediction': predicted_score})
    
    return jsonify({'error': 'Method not allowed'}), 405

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8080,debug=True)