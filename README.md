# 🦴 Bone Cancer Detection using Deep Learning

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-green)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![Status](https://img.shields.io/badge/Status-Live-success)

## 🌐 Live Demo
🚀 **App is live at:**  
👉 [https://bone-cancer.onrender.com](https://bone-cancer.onrender.com)

---

## 🧠 Project Overview
This web app uses a **Convolutional Neural Network (CNN)** to detect **Bone Cancer** from X-ray or MRI images.  
Built with **TensorFlow** and served using **Flask**, the model classifies images as either:

- 🟢 **Normal**
- 🔴 **Bone Cancer**

The interface allows users to upload an image and instantly get AI-driven predictions.

---

## 🧩 Features
✅ Upload X-ray or MRI image  
✅ Instant AI-based diagnosis  
✅ Modern and responsive user interface (HTML + CSS + Bootstrap)  
✅ Flask backend serving TensorFlow model  
✅ Fully deployed on Render  

---

## 🖼️ UI Preview
| Upload Screen | Result Screen |
|----------------|----------------|
| ![Upload Page](https://github.com/dhanyasri612/Bone_Cancer/assets/placeholder_upload.png) | ![Result Page](https://github.com/dhanyasri612/Bone_Cancer/assets/placeholder_result.png) |

*(You can replace these with real screenshots later.)*

---

## 🧰 Tech Stack
| Category | Technology |
|-----------|-------------|
| **Frontend** | HTML, CSS, Bootstrap |
| **Backend** | Flask |
| **AI/ML Model** | TensorFlow, Keras |
| **Deployment** | Render |
| **Version Control** | Git & GitHub |

---

## ⚙️ Installation & Local Setup
Follow these steps if you want to run it locally:

```bash
# 1️⃣ Clone the repository
git clone https://github.com/dhanyasri612/Bone_Cancer.git
cd Bone_Cancer

# 2️⃣ Create a virtual environment
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run the Flask app
python app.py
