# CNN-classifier
This application classifies images of a single digit, 0 - 9, using a CNN-model.
The start view has an area to click or drag and drop the images you want to classify.
You can choose between two CNN-models, the best model is the standard model with 99% accuracy.
That model handles digits and backgrounds of different colors. The image needs to have 
enough contrast between the digit and the background.

The classifications will be displayed as cards; showing the image, a prediction and
a probability. They predictions will be sorted first by class, second by probability.
In the same view you can download the classifications sorted and renamed in a zip-file,
containing 0 - 9 folders and a summery. In the navbar you can view the classifications 
in a diagram, showing the number of classifications for each label.


#Project setup (Windows)
* Sanic and Vue vite needs to be up and running for the app to work.

Terminal 1 (Sanic server)
1. Create a virtual environment:
    <br/>py -m venv venv
    <br/>venv\Scripts\activate.bat
2. pip install -r requirements.txt 


Terminal 2 (Vue vite server)
1. cd frontend
2. npm install
3. npm run dev






