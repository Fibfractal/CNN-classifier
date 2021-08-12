from tensorflow.keras.models import load_model
import numpy as np

def model_load():
    model = load_model('bestCNNmodel.h5')
    return model


def predict(model, image):

    y_pred = model.predict(image)
    pred_prob = format(np.max(y_pred), ".3f")
    pred_nbr = np.argmax(y_pred)

    # return a dict with predicted values
    return { "prediction": str(pred_nbr), "probability": pred_prob }


