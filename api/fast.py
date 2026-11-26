"""
FastAPI application for serving the zoologist model.
"""
import os

import pandas as pd
from fastapi import FastAPI

# FastAPI instance
app = FastAPI()


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
def predict():
    """predict endpoint that returns the class of a pengium"""
    return {"results":"AHAHAHAHa!!!"}
