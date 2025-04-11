from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import io
import os
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model with error handling
try:
    model = load_model('emotion_model.h5')
except Exception as e:
    raise RuntimeError(f"Failed to load model: {str(e)}")

# Emotion configuration
EMOTIONS = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]

# Audio files mapping
AUDIO_FILES = {
    "Angry": "audio/angry.mp3",
    "Disgust": "audio/disgust.mp3",
    "Fear": "audio/fear.mp3",
    "Happy": "audio/happy.mp3",
    "Sad": "audio/sad.mp3",
    "Surprise": "audio/surprise.mp3",
    "Neutral": "audio/neutral.mp3"
}

# Supportive messages for each emotion
MESSAGES = {
    "Angry": "Take a deep breath. It's okay to feel angry, but try to stay calm.",
    "Disgust": "Acknowledge what's bothering you, then let it go.",
    "Fear": "Face your fears with courage. You're stronger than you think!",
    "Happy": "Your happiness brightens the world! Keep smiling!",
    "Sad": "This feeling will pass. You're not alone.",
    "Surprise": "Life is full of surprises! Embrace the unexpected.",
    "Neutral": "Stay balanced and centered. Your calm is your strength."
}

class PredictionResponse(BaseModel):
    emotion: str
    confidence: float
    scores: Dict[str, float]
    message: str
    audio_file: str

@app.post("/predict", response_model=PredictionResponse)
async def predict(file: UploadFile = File(...)):
    try:
        # Verify file is an image
        if not file.content_type.startswith('image/'):
            raise HTTPException(status_code=400, detail="File must be an image")
            
        contents = await file.read()
        img = Image.open(io.BytesIO(contents)).convert('L').resize((48, 48))
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=(0, -1))
        
        pred = model.predict(img_array)
        predicted_emotion = EMOTIONS[np.argmax(pred)]
        
        return {
            "emotion": predicted_emotion,
            "confidence": float(np.max(pred)) * 100,
            "scores": {EMOTIONS[i]: float(pred[0][i]) * 100 for i in range(7)},
            "message": MESSAGES[predicted_emotion],
            "audio_file": f"/audio/{predicted_emotion.lower()}.mp3"  # URL path to audio
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/audio/{emotion}")
async def get_audio(emotion: str):
    audio_path = AUDIO_FILES.get(emotion.capitalize())
    if not audio_path or not os.path.exists(audio_path):
        raise HTTPException(status_code=404, detail="Audio file not found")
    return FileResponse(audio_path, media_type="audio/mpeg")

@app.get("/")
async def health_check():
    return {"status": "API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)