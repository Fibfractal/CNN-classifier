from werkzeug.utils import secure_filename
import aiofiles
import cv2 
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array


async def save_image(file, app):

    app.config["UPLOAD_FOLDER"] = "uploads"
    file_path = f'{app.config["UPLOAD_FOLDER"]}'

    async with aiofiles.open(file_path, 'wb') as f:
        await f.write(file.body)

    f.close()


def load_image():
    # 1 channel
    image = load_img('uploads', grayscale=True, target_size=(28,28))
    image = img_to_array(image)
    image = image.reshape(1,28,28,1)
    image = image.astype('float32') / 255
    return image


def save_classified_image(prediction, file):

    file_name = secure_filename(file.name)
    path = ""

    if prediction["prediction"] in [str(nbr) for nbr in range(10)]:
        # np array, as original image
        img_org = cv2.imread('uploads')
        path = "./images/" + prediction["prediction"] + "/" + file_name
        cv2.imwrite(path, img_org)
    
    return file_name, path

