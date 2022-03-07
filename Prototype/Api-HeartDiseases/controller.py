import joblib
import numpy as np


def _load_model(model_name):
    model = "models/" + str(model_name) + ".pkl"
    return joblib.load(model)


def predict_heart_disease(model_name, data):
    array = np.array(data)
    model = _load_model(model_name)
    return model.predict(array)
