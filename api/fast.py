"""
FastAPI application for serving the zoologist model.
"""
import os

import pandas as pd
from fastapi import FastAPI
from src.taxifare.predict import load_model,predict

# FastAPI instance
app = FastAPI()

MODEL_PATH = "models/linreg_pipeline.joblib"


# Root endpoint
@app.get("/")
def root():
    """Root endpoint returning a greeting."""
    return {"greeting": "hello"}


# Dummy endpoint
@app.get("/dummy")
def dummy(number: int):
    """Dummy endpoint that returns the square of the input number."""
    return {"result": number ** 2}

# prediction endpoint
@app.get("/predict")
def predict_fare_amount(pickup_datetime,pickup_longitude:float,
                        pickup_latitude:float,dropoff_longitude:float,
                        dropoff_latitude:float,passenger_count:int):
    """predict endpoint that returns fare amount of taxifare"""


    dic_map = {
    "pickup_datetime":[pickup_datetime],
    "pickup_longitude":[pickup_longitude],
    "pickup_latitude":[pickup_latitude],
    "dropoff_longitude":[dropoff_longitude],
    "dropoff_latitude":[dropoff_latitude],
    "passenger_count":[passenger_count]
    }
    X_pred = pd.DataFrame(dic_map)
    #print(X_pred)
    model = load_model(MODEL_PATH)
    predictions = predict(model,X_pred)


    return {"amount": predictions[0]}
