from fastapi import FastAPI

import pickle
import pandas as pd

from fastapi.responses import JSONResponse

from model.predict import predict_output
from schema.user_input import UserInput

MODEL_VERSION = '1.0.0'



with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

app = FastAPI()



@app.get("/")
def home():
    return {"message": "insurance premium prediction api"}


@app.get("/health")
def health_check():
    return {
        "status": "OK",
        "version": MODEL_VERSION
    }
@app.post("/predict")
def predict_premium(data:UserInput):
    user_input = {
        "bmi": data.bmi,
        "age_group": data.age_group,
        "lifestyle_risk": data.lifestyle_risk,
        "city_tier": data.city_tier,
        "income_lpa": data.income_lpa,
        "occupation": data.occupation,


    }

    prediction = predict_output(user_input)
    return JSONResponse(status_code=200, content={'predicted_category': prediction})





