from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import pathlib

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

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", include_in_schema=False)
def ui():
    index_path = pathlib.Path("app/static/index.html")
    return FileResponse(index_path)
