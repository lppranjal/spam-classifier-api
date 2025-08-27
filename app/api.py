from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import joblib
import os

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

# Serve static Angular files
app.mount("/", StaticFiles(directory="app/static", html=True), name="static")

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

# Serve Angular index.html for root and SPA routes
@app.get("/{full_path:path}")
def serve_spa(full_path: str):
    index_path = os.path.join("app/static", "index.html")
    return FileResponse(index_path)