from pymongo import MongoClient
from bson import ObjectId
from flask_cors import CORS
from flask import Flask

app = Flask(__name__)
CORS(app)  # This should allow all domains by default


# Establish a connection to the MongoDB server
client = MongoClient('mongodb://mongo:27017/')
db = client['Titanic_Survival']  # Replace with your database name
collection = db['Predictions']  # Replace with your collection name

def insert_document(data):
    """Insert a document into the collection and return its ID."""
    result = collection.insert_one(data)
    return str(result.inserted_id)

def get_document(doc_id):
    """Fetch a document from MongoDB by its ID."""
    try:
        print(f"Attempting to fetch document with ID: {doc_id}")
        object_id = ObjectId(doc_id)  # Ensure it's converted to ObjectId
        document = collection.find_one({"_id": ObjectId(doc_id)})

        if document:
            print("Document found:", document)
            document["_id"] = str(document["_id"])
            return document
        else:
            print("No document found with this ID.")
            return None
    except Exception as e:
        print(f"Error fetching document: {e}")
        return None
