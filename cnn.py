from tensorflow.keras.models import load_model
import pandas as pd
import numpy as np
import time

t0 = time.time()

def model_load():
    model = load_model('bestCNNmodel.h5')
    X_test = pd.read_csv('test.csv')
    X_test = X_test / 255

    return (model, X_test)


def predict(model, X_test):

    y_test_pred = model.predict(X_test)

    pred_prob = format(np.max(y_test_pred), ".3f")
    pred_nbr = np.argmax(y_test_pred)

    # return a dict with predicted values
    return { "prediction": str(pred_nbr), "probability": pred_prob }


