import os
import numpy as np
from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Initialize Flask app
app = Flask(__name__)

# Load trained CNN model
MODEL_PATH = "model/bone_cancer_cnn.h5"
model = load_model(MODEL_PATH)

# Define upload folder
UPLOAD_FOLDER = "static/uploads/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Class labels
CLASSES = ["Normal", "Bone Cancer"]

def preprocess_image(img_path):
    """Preprocess the image for model prediction"""
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            filename = file.filename
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(file_path)

            # Preprocess & Predict
            img_array = preprocess_image(file_path)
            prediction = model.predict(img_array)
            result = CLASSES[int(prediction[0][0] > 0.5)]

            return render_template("index.html", uploaded_image=file_path, result=result)

    return render_template("index.html", uploaded_image=None, result=None)

if __name__ == "__main__":
    app.run(debug=True)
