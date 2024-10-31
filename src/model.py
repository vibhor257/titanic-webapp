# model.py

import numpy as np

# Load the model from the pickle file


# Prediction function
def predict(input_data, model):
     # Load the model
    # Make prediction
    print(np.array(input_data).reshape(1, -1))
    prediction = model.predict(np.array(input_data).reshape(1, -1))
    return prediction[0]  # Return the first element from the prediction
