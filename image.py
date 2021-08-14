from werkzeug.utils import secure_filename
import aiofiles
import cv2 
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
import matplotlib.pyplot as plt


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
    image = process_image(image)

    image = image.reshape(1,28,28,1)
    image = image.astype('float32') / 255
    return image

def process_image(image):
    # Get higher contrast
    (thresh, image_t) = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    # See if white or black background
    nbr_val = image_t.shape[0] * image_t.shape[1]
    counter = 0
    thresh = 0.5
    
    for k in range(len(image_t)):
        for l in range(len(image_t[k])):
            counter += 1 if image_t[k][l] == 255 else 0
    
    print("Counter:", counter)
    percent_white = counter / nbr_val
    print("Percent val white", percent_white)

    if percent_white > thresh:
        #invert color
        image_t = (255-image_t)
        
        # plt.imshow(image_t)
        # plt.show()
        return image_t

    return image_t



def save_classified_image(prediction, file):

    file_name = secure_filename(file.name)
    path = ""

    if prediction["prediction"] in [str(nbr) for nbr in range(10)]:
        # np array, as original image
        img_org = cv2.imread('uploads')
        path = "./images/" + prediction["prediction"] + "/" + file_name
        cv2.imwrite(path, img_org)
    
    return file_name, path

