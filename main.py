from image import save_image, load_image_model_1, load_image_model_2
from cnn import predict
from sanic import Sanic, response as res
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
import time


app = Sanic('app')

@app.post('/api/predict/standard')
async def make_predictions_model_1(req):

  t0 = time.time()

  model = load_model('bestCNNmodel.h5')
  prediction_list = []

  for i in range(len(req.files)):

    a = i + 1
    file = req.files.get('image' + str(a))

    await save_image(file,app)
    image = load_image_model_1()

    prediction = predict(model, image)
    prediction["file_name"] = secure_filename(file.name)
    prediction_list.append(prediction)


  t1 = time.time()
  print('Time all predictions (s): ', t1 - t0 )

  return res.json(prediction_list)


@app.post('/api/predict/transferlearning')
async def make_predictions_model_2(req):

  t0 = time.time()

  model = load_model('bestCNNimageNet.h5')
  prediction_list = []

  for i in range(len(req.files)):

    a = i + 1
    file = req.files.get('image' + str(a))

    await save_image(file,app)
    image = load_image_model_2()

    prediction = predict(model, image)
    prediction["file_name"] = secure_filename(file.name)
    prediction_list.append(prediction)


  t1 = time.time()
  print('Time all predictions (s): ', t1 - t0 )

  return res.json(prediction_list)


if __name__ == '__main__':
  app.run(port=5000)