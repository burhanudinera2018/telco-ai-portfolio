# deployment/src/main.py
import os
import logging
import joblib
import numpy as np
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
import uvicorn

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

PORT = int(os.getenv("AIP_HTTP_PORT", "8080"))
HEALTH_ROUTE = os.getenv("AIP_HEALTH_ROUTE", "/health")
PREDICT_ROUTE = os.getenv("AIP_PREDICT_ROUTE", "/predict")

app = FastAPI(title="Churn Prediction API")

class Request(BaseModel):
    instances: list[list[float]]

class Response(BaseModel):
    predictions: list[float]

class HealthResponse(BaseModel):
    status: str
    model_loaded: bool

MODEL_PATH = "models/churn_model.joblib"
SCALER_PATH = "models/scaler.joblib"
FEATURES_PATH = "models/feature_columns.txt"

model = None
scaler = None
feature_columns = None

def load_model():
    global model, scaler, feature_columns
    try:
        model = joblib.load(MODEL_PATH)
        scaler = joblib.load(SCALER_PATH)
        with open(FEATURES_PATH, 'r') as f:
            feature_columns = [line.strip() for line in f.readlines()]
        logger.info(f"✅ Model loaded: {type(model)}")
        return True
    except Exception as e:
        logger.error(f"❌ Failed to load: {e}")
        return False

model_loaded = load_model()

@app.get(HEALTH_ROUTE, response_model=HealthResponse)
async def health_check():
    if not model_loaded:
        raise HTTPException(status_code=503, detail="Model not loaded")
    return HealthResponse(status="healthy", model_loaded=True)

# deployment/src/main.py - bagian predict()

# deployment/src/main.py - FULL PREDICT FUNCTION (FIXED)

@app.post(PREDICT_ROUTE, response_model=Response)
async def predict(request: Request):
    try:
        if not model_loaded:
            raise HTTPException(status_code=503, detail="Model not ready")
        
        # Konversi ke numpy array
        input_data = np.array(request.instances)
        
        if input_data.ndim != 2:
            raise ValueError("Input must be 2D array")
        
        # --- SCALING KHUSUS UNTUK 3 FITUR NUMERIK ---
        # Asumsi: fitur numerik ada di indeks 0 (tenure), 1 (MonthlyCharges), 2 (TotalCharges)
        # Ini sesuai dengan urutan fitur di X.columns
        
        # Buat copy data
        input_scaled = input_data.copy()
        
        # Ambil 3 fitur numerik pertama
        numeric_indices = [0, 1, 2]
        
        # Scale hanya 3 fitur numerik
        input_scaled[:, numeric_indices] = scaler.transform(input_data[:, numeric_indices])
        
        # Prediksi dengan model
        predictions = model.predict_proba(input_scaled)[:, 1].tolist()
        
        logger.info(f"✅ Predictions generated: {predictions}")
        
        return Response(predictions=predictions)
        
    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=PORT)