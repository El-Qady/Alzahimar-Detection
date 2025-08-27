import numpy as np
import tensorflow as tf
from PIL import Image
import os
import gdown
CLASSES_NAMES = ['Mild Demented', 'Moderate Demented', 'Non Demented', 'Very MildDemented']  # Assumes this is a list or array of class names
MODEL_PATH = "./Alzheimer_Model_binary.h5"
url='https://drive.google.com/file/d/1En9_ggZQvhsVk2a6UgUy3J4ah0QhE4HJ/view?usp=sharing'
if not os.path.exists(MODEL_PATH):
    gdown.download(url, MODEL_PATH, quiet=False)
MODEL = tf.keras.models.load_model(MODEL_PATH)

def img_processing(img_path):
    # Open the image using Pillow
    img = Image.open(img_path)
    
    # Convert the image to RGB (removes the alpha channel if it exists)
    img = img.convert('RGB')
    
    # Resize the image to (224, 224)
    img = img.resize((224, 224))
    
    # Convert the image to a NumPy array
    img = np.array(img)
    
    # Normalize the pixel values to [0, 1]
    img = img / 255.0
    
    # Add batch dimension (1, 224, 224, 3)
    img = np.expand_dims(img, axis=0)
    return img


def img_prediction(processed_img):
    pred = MODEL.predict(processed_img)  # Make predictions
    pred_class = np.argmax(pred, axis=1)[0]  # Extract the class index
    return pred_class


def classification_name(class_res):
    # Map the class index to the class name
    return CLASSES_NAMES[class_res]

