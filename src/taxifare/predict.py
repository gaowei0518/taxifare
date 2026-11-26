"""
Load the trained TaxiFare pipeline from disk and make predictions on new data.
"""

import joblib
import pandas as pd
from sklearn import config_context

MODEL_PATH = "models/linreg_pipeline.joblib"


def load_model( model_path: str):
    """Load a trained pipeline from disk.

    Params:
    - model_path: str, path to the saved .joblib pipeline

    Returns:
    - the fitted scikit-learn pipeline
    """
    with open( model_path, "rb") as f:
        model = joblib.load(f)
    return model


def predict(model, data: pd.DataFrame):
    """Predict taxi fares with a loaded pipeline.

    Params:
    - model: fitted scikit-learn pipeline, as returned by load_model()
    - data: pd.DataFrame with the same raw columns as the training data
      (pickup_datetime, pickup/dropoff longitude and latitude, passenger_count)

    Returns:
    - np.ndarray of predicted fares
    """

    with config_context(transform_output="pandas"):
         return model.predict(data)


if __name__ ==  "__main__":
    X_dummy = pd.DataFrame([{
          'pickup_datetime': '2013-07-06 17:18:00 UTC',
          'pickup_longitude': -73.950655,
          'pickup_latitude':  40.783282,
          'dropoff_longitude': -73.984365,
          'dropoff_latitude':   40.769802,
          'passenger_count': 1
    }])

    model = load_model("models/linreg_pipeline.joblib")

    print(predict(model, X_dummy))
