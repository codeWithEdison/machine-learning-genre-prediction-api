from flask import Flask, request, jsonify
import joblib
import os
import pandas as pd
app = Flask(__name__) # name of current module


# load model 
model = joblib.load('genre_model.joblib')
label_encoder = joblib.load('label_encoder.joblib') 

# endpoint to home page

@app.route('/')
def home():
    return "Welcome to Music Genre Prediction API"

# enpoint to predict
@app.route('/predict' , methods=['POST'])
def predict_genre():
    try:
        data = request.get_json()
        age = data.get('age')
        gender = data.get('gender')
        # Basic validation
        if age is None or gender is None:
            return jsonify({"error": "Missing required fields"}), 400
        
        features = pd.DataFrame({
            'age': [age],
            'gender': [gender]
        })
        predict = model.predict(features)
        
        predicted_genre = label_encoder.inverse_transform(predict)[0]
        return  jsonify({
            "prediction": predicted_genre,
            "age": age,
            "gender": gender
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
        
# healt check enpoint 

@app.route('/health')
def health_check():
    return jsonify({"status": "OK"})

# run the app


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 1000))
    app.run(host='0.0.0.0', port=port)