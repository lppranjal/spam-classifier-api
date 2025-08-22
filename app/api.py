from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib

# Load the model pipeline
model = joblib.load('app/model.joblib')

# FastAPI app initialization
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # you can replace "*" with your Angular domain(s) for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

