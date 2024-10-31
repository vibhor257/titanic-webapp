from flask import Flask, request, jsonify
from model import predict
from pymongo import MongoClient
from bson.objectid import ObjectId  # Import ObjectId for MongoDB document IDs
from mongo import get_document  # Import the get_document function
import pickle

app = Flask(__name__)

# MongoDB connection setup
client = MongoClient("mongodb://mongo:27017/")  # Adjust if needed
db = client['Titanic_Survival']  # Your database name
collection = db['Predictions']  # Replace with your collection name


def load_model():
    with open('log_reg.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model() 

@app.route('/predict', methods=['POST'])
def predict_route():
    # Get JSON data from the request
    data = request.get_json()
    print(data)
    
    # Extract input features safely using .get()
    Pclass = data.get('Pclass')
    Sex = data.get('Sex')
    Age = data.get('Age')
    Fare = data.get('Fare')
    
    # Check for missing values and return an error if any are found
    if Pclass is None or Sex is None or Age is None or Fare is None:
        return jsonify({"error": "Please provide all fields: Pclass, Sex, Age, Fare."}), 400
    
    # Convert Sex to a numerical value
    Sex_n = 1 if Sex.lower() == 'male' else 0

    # Prepare input for prediction
    x = [Pclass, Sex_n, Age, Fare]

    # Make prediction using the model
    result = predict(x, model)
    result_new = "Survived" if result == 1 else "died"
    
    # Print the result in the terminal for verification
    print(f"Prediction result: {result_new}")

    # Store the request and response in MongoDB
    document = {
        "Pclass": Pclass,
        "Sex": Sex,
        "Age": Age,
        "Fare": Fare,
        "Survived Or Died": result_new
    }
    result_id = collection.insert_one(document).inserted_id  # Insert and get the ID

    # Return the result and the MongoDB ID as a JSON response
    return jsonify({"Survived Or Died": result_new, "Document ID": str(result_id)})

@app.route('/result/<string:doc_id>', methods=['GET'])
def get_result(doc_id):
    """Get a prediction result by its MongoDB ID."""
    print(f"Received request for document ID: {doc_id}")  # Log incoming request
    document = get_document(doc_id)
    if document:
        return jsonify(document)
    else:
        return jsonify({"error": "Document not found."}), 404
    


@app.route('/preprocess', methods=['GET'])
def pre():
    return jsonify({"name": "vibhor was here"})


app.run(debug=False, host="0.0.0.0", port=8000)
    
