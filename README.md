# 🧠 Alzheimer’s Disease Detection using Deep Learning
<p align="center">
  <!-- Repo Status Badges -->
  <img src="https://img.shields.io/github/last-commit/El-Qady/Alzahimar-Detection"/>
  <img src="https://img.shields.io/github/languages/count/El-Qady/Alzahimar-Detection"/>
  <img src="https://img.shields.io/github/repo-size/El-Qady/Alzahimar-Detection"/>
  <img src="https://img.shields.io/github/license/El-Qady/Alzahimar-Detection"/>
  <img src="https://img.shields.io/github/stars/El-Qady/Alzahimar-Detection?style=social"/>
</p>
<p align="center">
  <!-- Repo Status Badges -->
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"/>
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white"/>
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"/>
  <img src="https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"/>
</p>

A deep learning project aimed at **detecting and classifying the stage of Alzheimer’s disease** from brain MRI scans.  
The system is built using a **Convolutional Neural Network (CNN)** for accurate image classification and is deployed as a **web application** for real-time predictions.  

---

## 🚀 Key Features
- **Data Preprocessing**  
  - Applied image cleaning and preprocessing.  
  - Used `ImageDataGenerator` for augmentation to improve model generalization.  

- **Model Development**  
  - Designed and trained a CNN model for **multi-stage Alzheimer’s detection**.  
  - Optimized hyperparameters to reduce overfitting and improve accuracy.  

- **Web Application**  
  - Developed a **responsive front-end** with HTML, CSS, and JavaScript.  
  - Integrated the trained CNN model with Flask for real-time predictions.  

- **User Workflow**  
  1. User uploads an **MRI scan** via the web interface.  
  2. The model processes the image.  
  3. The system returns the predicted **Alzheimer’s disease stage** instantly.  

---

## 🛠️ Technologies Used
- **Deep Learning**: TensorFlow / Keras (CNN)  
- **Data Preprocessing**: ImageDataGenerator  
- **Web Development**: HTML, CSS, JavaScript  
- **Backend & Model Integration**: Flask  
- **Tools**: Python, Jupyter Notebook  

---

## 📂 Project Structure
```bash
├── static/              # CSS, JS, and images for frontend
├── templates/           # HTML templates for Flask
├── model/               # Saved CNN model (.h5 file)
├── app.py               # Flask backend
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## ⚙️ Installation & Usage
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/alzheimer-detection.git
   cd alzheimer-detection
   ```

2. **Create & activate virtual environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Mac/Linux
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Flask application**  
   ```bash
   python back.py
   ```

5. Open your browser and go to:  
   ```
   http://127.0.0.1:5000/
   ```

---

## 📊 Dataset
- MRI brain scan dataset for Alzheimer’s detection.  
- Preprocessed with resizing, normalization, and augmentation using **ImageDataGenerator**.  
- Supports multiple stages of Alzheimer’s disease.  

---

## 🎯 Future Improvements
- Improve accuracy using **transfer learning** (e.g., VGG16, ResNet).  
- Add support for **explainable AI (XAI)** to highlight important regions in MRI scans.  
- Deploy on **cloud platforms** (AWS, Heroku, or Streamlit Cloud).  

---

## 🤝 Contribution
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.  

---

## 📜 License
This project is licensed under the MIT License.  
