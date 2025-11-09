import os
import numpy as np
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Flask setup
app = Flask(__name__)
CORS(app)  # ✅ Allow frontend (GitHub Pages) to call your backend

# Uploads folder
UPLOAD_FOLDER = "static/uploads/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Model + Classes
MODEL_PATH = "model/bone_cancer_cnn.h5"
CLASSES = ["Normal", "Bone Cancer"]

def preprocess_image(img_path):
    """Prepare image for prediction"""
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def predict_from_form():
    """For form submission from HTML page"""
    file = request.files["file"]
    if not file:
        return render_template("index.html", uploaded_image=None, result="No file uploaded")

    filename = file.filename
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(file_path)

    # ✅ Load model only when needed (saves memory)
    model = load_model(MODEL_PATH)
    img_array = preprocess_image(file_path)
    prediction = model.predict(img_array)
    result = CLASSES[int(prediction[0][0] > 0.5)]

    return render_template("index.html", uploaded_image=file_path, result=result)

@app.route("/predict", methods=["POST"])
def predict_api():
    """✅ API endpoint for GitHub Pages frontend"""
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    filename = file.filename
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(file_path)

    model = load_model(MODEL_PATH)
    img_array = preprocess_image(file_path)
    prediction = model.predict(img_array)
    result = CLASSES[int(prediction[0][0] > 0.5)]

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=False)
