from image import save_image, load_image, save_classified_image
from cnn import model_load, predict
from sanic import Sanic, response as res
import time


app = Sanic('app')
model = model_load()

# enable frontend to be served from root
# app.static('/', './frontend/uploads')


@app.post('/api/predict')
async def make_predictions(req):

  t0 = time.time()

  prediction_list = []

  for i in range(len(req.files)):

    a = i + 1
    file = req.files.get('image' + str(a))

    await save_image(file,app)
    image = load_image()

    # add filename here instead if save is deleted / uncommented
    prediction = predict(model, image)

    # This is unnecessary if there is no point of saving the file backend
    data = save_classified_image(prediction, file)

    # Skicka filename utan path kan göras direkt här utan
    # data[] från save_classified som ev tas bort
    prediction["file_name"] = data[0]
    prediction["path"] = data[1]

    # print("Prediction: ", prediction)
    prediction_list.append(prediction)


  t1 = time.time()
  print('Time all predictions (s): ', t1 - t0 )

  return res.json(prediction_list)


if __name__ == '__main__':
  app.run(port=5000)