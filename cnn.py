import numpy as np


def predict(model, image):

    y_pred = model.predict(image)
    pred_prob = format(np.max(y_pred), ".3f")
    pred_nbr = np.argmax(y_pred)

    # return a dict with predicted values
    return { "prediction": str(pred_nbr), "probability": pred_prob }