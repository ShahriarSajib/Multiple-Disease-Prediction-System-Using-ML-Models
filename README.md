🏥 Multiple Disease Prediction System Using Machine Learning

A web-based health prediction system that uses Machine Learning models to predict the likelihood of three major diseases: **Heart Disease**, **Diabetes**, and **Parkinson’s Disease** based on user-provided medical parameters.

The application is built with **Streamlit** for an interactive and user-friendly web interface.

🚀 Live Demo
🔗 https://multiple-disease-prediction-system-using-ml-models.streamlit.app/


📌 Project Overview

This system allows users to input medical data and receive predictions for:

- ❤️ Heart Disease
- 🩸 Diabetes
- 🧠 Parkinson’s Disease

Each prediction is powered by trained ML models saved as `.sav` files.


🧠 Machine Learning Models

The system uses pre-trained models trained on standard datasets:

| Disease | Dataset | Model File |
|--------|--------|------------|
| Heart Disease | heart.csv | heart_disease_model.sav |
| Diabetes | diabetes.csv | diabetes_model.sav |
| Parkinson’s | parkinsons.csv | parkinsons_model.sav |

Algorithms used may include:
- Logistic Regression
- Support Vector Machine (SVM)
- Random Forest (depending on notebook experimentation)


🏗️ Project Structure


Multiple-Disease-Prediction-System-Using-ML-Models/
│
├── Multiple diseases prediction system.py # Main Streamlit app
├── hui.py # Additional UI/helper logic
│
├── diabetes.ipynb
├── heart_disease.ipynb
├── Parkinsons_disease.ipynb
│
├── diabetes.csv
├── heart.csv
├── parkinsons.csv
│
├── diabetes_model.sav
├── heart_disease_model.sav
├── parkinsons_model.sav
│
├── requirements.txt
└── README.md



⚙️ Installation & Setup

1. Clone the repository
git clone https://github.com/ShahriarSajib/Multiple-Disease-Prediction-System-Using-ML-Models.git

cd Multiple-Disease-Prediction-System-Using-ML-Models

2. Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

3. Install dependencies
pip install -r requirements.txt

4. Run the Streamlit app
streamlit run Multiple diseases prediction system.py

📊 Features
Simple and interactive UI using Streamlit
Real-time disease prediction
Separate modules for each disease
Pre-trained ML models for fast inference
Clean and modular project structure

🛠️ Technologies Used
Python 🐍
Streamlit 🎈
Scikit-learn 🤖
Pandas 📊
NumPy 🔢
Machine Learning Models

📈 Future Improvements
Improve model accuracy with deep learning
Add more diseases (Cancer, Kidney, Liver, etc.)
Integrate database for patient history
Add user authentication system
Deploy with Docker for scalability

👨‍💻 Author
Shahriar Sajib
