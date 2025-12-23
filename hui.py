"""
@author:SH Sajib
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Page configuration
st.set_page_config(
    page_title="Health Prediction System",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
<style>

/* =========================
   Theme Variables
   ========================= */
:root {
    --primary: #ff4b4b;
    --primary-hover: #ff6b6b;

    --bg-light: #ffffff;
    --bg-dark: #0e1117;

    --box-light: #f0f2f6;
    --box-dark: #1c1f26;

    --text-light: #000000;
    --text-dark: #fafafa;

    --border-radius: 12px;
}

/* =========================
   Base Layout
   ========================= */
.main {
    padding: 1rem 1.5rem;
}

/* =========================
   Headings
   ========================= */
h1, h2, h3 {
    font-weight: 700;
}

h1 {
    color: var(--primary);
}

/* =========================
   Buttons
   ========================= */
.stButton > button {
    width: 100%;
    padding: 0.6rem 1rem;
    font-weight: 600;
    border-radius: var(--border-radius);
    border: none;
    background-color: var(--primary);
    color: white;
    transition: background-color 0.2s ease-in-out;
}

.stButton > button:hover {
    background-color: var(--primary-hover);
}

/* =========================
   Info & Prediction Boxes
   ========================= */
.info-box,
.prediction-box {
    padding: 1rem 1.25rem;
    border-radius: var(--border-radius);
    margin-bottom: 1rem;
    font-size: 0.95rem;
}

/* =========================
   Light Mode
   ========================= */
@media (prefers-color-scheme: light) {

    .info-box {
        background-color: var(--box-light);
        color: var(--text-light);
    }

    .prediction-box {
        background-color: #e8f0fe;
        color: var(--text-light);
    }
}

/* =========================
   Dark Mode
   ========================= */
@media (prefers-color-scheme: dark) {

    .info-box {
        background-color: var(--box-dark);
        color: var(--text-dark);
    }

    .prediction-box {
        background-color: #1f2937;
        color: var(--text-dark);
    }
}

/* =========================
   Sidebar Tweaks
   ========================= */
section[data-testid="stSidebar"] {
    padding-top: 1rem;
}

/* =========================
   Footer
   ========================= */
.footer {
    text-align: center;
    font-size: 0.85rem;
    color: gray;
    padding: 1rem 0;
}

</style>
""", unsafe_allow_html=True)


# Loading the saved models
try:
    diabetes_model = pickle.load(open('C:/Users/mohmmad/python/diabetes_model.sav', 'rb'))
    heart_disease_model = pickle.load(open('C:/New folder (5)/Multiple Disease Prediction System/heart_disease_model.sav','rb'))
    parkinsons_model = pickle.load(open('C:/New folder (5)/Multiple Disease Prediction System/parkinsons_model.sav', 'rb'))
except FileNotFoundError as e:
    st.error(f"⚠️ Error loading models: {e}")
    st.stop()

# Sidebar for navigation
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/health-checkup.png", width=100)
    st.title("🏥 Health Predictor")
    
    selected = option_menu(
    'Disease Prediction System',
    ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
    icons=['droplet-fill', 'heart-pulse-fill', 'person-fill'],
    menu_icon="hospital-fill",
    default_index=0,
    styles={
        "container": {"padding": "5!important"},
        "icon": {"color": "var(--primary-color)", "font-size": "23px"},
        "nav-link": {
            "font-size": "16px",
            "text-align": "left",
            "margin": "0px",
            "--hover-color": "var(--hover-color, #eee)",
        },
        "nav-link-selected": {
            "background-color": "var(--primary-color)",
            "color": "var(--text-color)",
        },
    }
)
    
    st.markdown("---")
    st.markdown("### ℹ️ About")
    st.info("This system uses Machine Learning to predict the likelihood of various diseases based on medical parameters.")

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('🩸 Diabetes Prediction')
    st.markdown("### Enter Patient Information")
    
    with st.container():
        st.markdown('<div class="info-box">Please fill in all the fields below with accurate medical data.</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=20, value=0, help="Total number of pregnancies")
        SkinThickness = st.number_input('Skin Thickness (mm)', min_value=0, max_value=100, value=20, help="Triceps skin fold thickness")
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=3.0, value=0.5, step=0.01, help="Diabetes heredity score")
        
    with col2:
        Glucose = st.number_input('Glucose Level (mg/dL)', min_value=0, max_value=300, value=120, help="Plasma glucose concentration")
        Insulin = st.number_input('Insulin Level (μU/mL)', min_value=0, max_value=900, value=80, help="2-Hour serum insulin")
        Age = st.number_input('Age (years)', min_value=1, max_value=120, value=30)
    
    with col3:
        BloodPressure = st.number_input('Blood Pressure (mm Hg)', min_value=0, max_value=200, value=70, help="Diastolic blood pressure")
        BMI = st.number_input('BMI (kg/m²)', min_value=0.0, max_value=70.0, value=25.0, step=0.1, help="Body Mass Index")
    
    diab_diagnosis = ''
    
    if st.button('🔬 Predict Diabetes Risk'):
        with st.spinner('Analyzing data...'):
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            
            if diab_prediction[0] == 1:
                diab_diagnosis = '⚠️ High Risk: The person is likely to be diabetic'
                st.error(diab_diagnosis)
            else:
                diab_diagnosis = '✅ Low Risk: The person is not likely to be diabetic'
                st.success(diab_diagnosis)

# Heart Disease Prediction Page
elif selected == 'Heart Disease Prediction':
    st.title('❤️ Heart Disease Prediction')
    st.markdown("### Enter Patient Information")
    
    with st.container():
        st.markdown('<div class="info-box">Please provide accurate cardiac health parameters for prediction.</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age (years)', min_value=1, max_value=120, value=50)
        trestbps = st.number_input('Resting Blood Pressure (mm Hg)', min_value=80, max_value=200, value=120)
        restecg = st.selectbox('Resting ECG Results', options=[0, 1, 2], format_func=lambda x: ['Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy'][x])
        oldpeak = st.number_input('ST Depression', min_value=0.0, max_value=10.0, value=1.0, step=0.1)
        thal = st.selectbox('Thalassemia', options=[0, 1, 2], format_func=lambda x: ['Normal', 'Fixed Defect', 'Reversible Defect'][x])
        
    with col2:
        sex = st.selectbox('Sex', options=[0, 1], format_func=lambda x: 'Female' if x == 0 else 'Male')
        chol = st.number_input('Serum Cholesterol (mg/dL)', min_value=100, max_value=600, value=200)
        thalach = st.number_input('Maximum Heart Rate', min_value=60, max_value=220, value=150)
        slope = st.selectbox('ST Segment Slope', options=[0, 1, 2], format_func=lambda x: ['Upsloping', 'Flat', 'Downsloping'][x])
    
    with col3:
        cp = st.selectbox('Chest Pain Type', options=[0, 1, 2, 3], format_func=lambda x: ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'][x])
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dL', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
        exang = st.selectbox('Exercise Induced Angina', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
        ca = st.selectbox('Major Vessels (0-3)', options=[0, 1, 2, 3])
    
    heart_diagnosis = ''
    
    if st.button('🔬 Predict Heart Disease Risk'):
        with st.spinner('Analyzing cardiac data...'):
            heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            
            if heart_prediction[0] == 1:
                heart_diagnosis = '⚠️ High Risk: The person is likely to have heart disease'
                st.error(heart_diagnosis)
            else:
                heart_diagnosis = '✅ Low Risk: The person is not likely to have heart disease'
                st.success(heart_diagnosis)

# Parkinson's Prediction Page
elif selected == "Parkinsons Prediction":
    st.title("🧠 Parkinson's Disease Prediction")
    st.markdown("### Enter Voice Measurement Data")
    
    with st.container():
        st.markdown('<div class="info-box">This prediction uses voice analysis parameters. Please ensure accurate measurements.</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        fo = st.number_input('MDVP:Fo(Hz)', min_value=0.0, value=150.0, step=0.1, help="Average vocal fundamental frequency")
        RAP = st.number_input('MDVP:RAP', min_value=0.0, value=0.002, step=0.0001, format="%.6f")
        Shimmer = st.number_input('MDVP:Shimmer', min_value=0.0, value=0.03, step=0.001, format="%.5f")
        APQ3 = st.number_input('Shimmer:APQ3', min_value=0.0, value=0.015, step=0.001, format="%.5f")
        HNR = st.number_input('HNR', min_value=0.0, value=20.0, step=0.1)
        D2 = st.number_input('D2', min_value=0.0, value=2.0, step=0.01)
        
    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)', min_value=0.0, value=200.0, step=0.1, help="Maximum vocal fundamental frequency")
        PPQ = st.number_input('MDVP:PPQ', min_value=0.0, value=0.002, step=0.0001, format="%.6f")
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)', min_value=0.0, value=0.3, step=0.01)
        APQ5 = st.number_input('Shimmer:APQ5', min_value=0.0, value=0.02, step=0.001, format="%.5f")
        RPDE = st.number_input('RPDE', min_value=0.0, value=0.5, step=0.01)
        PPE = st.number_input('PPE', min_value=0.0, value=0.2, step=0.01)
        
    with col3:
        flo = st.number_input('MDVP:Flo(Hz)', min_value=0.0, value=100.0, step=0.1, help="Minimum vocal fundamental frequency")
        DDP = st.number_input('Jitter:DDP', min_value=0.0, value=0.006, step=0.0001, format="%.6f")
        APQ = st.number_input('MDVP:APQ', min_value=0.0, value=0.02, step=0.001, format="%.5f")
        DFA = st.number_input('DFA', min_value=0.0, value=0.7, step=0.01)
        
    with col4:
        Jitter_percent = st.number_input('MDVP:Jitter(%)', min_value=0.0, value=0.5, step=0.01, format="%.5f")
        NHR = st.number_input('NHR', min_value=0.0, value=0.02, step=0.001, format="%.5f")
        DDA = st.number_input('Shimmer:DDA', min_value=0.0, value=0.045, step=0.001, format="%.5f")
        spread1 = st.number_input('spread1', min_value=-10.0, max_value=0.0, value=-5.0, step=0.1)
        
    with col5:
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs)', min_value=0.0, value=0.00003, step=0.000001, format="%.8f")
        spread2 = st.number_input('spread2', min_value=0.0, value=0.2, step=0.01)
    
    parkinsons_diagnosis = ''
    
    if st.button("🔬 Predict Parkinson's Risk"):
        with st.spinner('Analyzing voice data...'):
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
            
            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "⚠️ High Risk: The person is likely to have Parkinson's disease"
                st.error(parkinsons_diagnosis)
            else:
                parkinsons_diagnosis = "✅ Low Risk: The person is not likely to have Parkinson's disease"
                st.success(parkinsons_diagnosis)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: gray; padding: 1rem;'>
        <p>⚠️ <strong>Disclaimer:</strong> This is a prediction tool and should not replace professional medical advice. 
        Always consult with healthcare professionals for accurate diagnosis and treatment.</p>
    </div>
""", unsafe_allow_html=True)