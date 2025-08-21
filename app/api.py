from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load the model pipeline
model = joblib.load('app/model.joblib')

# FastAPI app initialization
app = FastAPI()

# Request body schema
class Message(BaseModel):
    text: str

@app.post('/predict')
def predict_spam(message: Message):
    prediction = model.predict([message.text])
    probs = model.predict_proba([message.text])[0]
    probability = probs[prediction]
    result = 'spam' if prediction == 1 else 'ham'
    return {
        "result": result,
        "probability": float(probability)
    }

