import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load model
with open('rf_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Page config
st.set_page_config(page_title="Heart Disease Predictor", page_icon="❤️")
st.title("❤️ Heart Disease Risk Prediction App")
st.write("This app uses a trained Random Forest model to predict the likelihood of heart disease based on medical data.")

# ================= SIDEBAR ==================
st.sidebar.title("📌 Info Panel")

st.sidebar.subheader("🔍 Risk Guidelines (Typical)")
st.sidebar.markdown("""
- **Age** > 50 → higher risk  
- **Cholesterol** > 240 mg/dl  
- **BP** > 130 mm Hg  
- **Max HR** < 100 bpm  
- **Oldpeak** > 1.5  
- **CA > 0** → Blockage likely  
- **Thal = 2 or 3** → Abnormal  
""")

st.sidebar.subheader("🧬 Feature Descriptions")
st.sidebar.markdown("""
- **cp**: Chest pain (0–3)  
- **fbs**: Fasting blood sugar  
- **restecg**: ECG results  
- **exang**: Exercise-induced angina  
- **slope**: ST segment slope  
- **ca**: No. of colored vessels  
- **thal**: Thalassemia result  
""")

# ============== MANUAL INPUT ==============
st.header("🧑‍⚕️ Enter Patient Data")

with st.form("manual_form"):
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 20, 100, 50)
        sex = st.selectbox("Sex", ["Male", "Female"])
        cp = st.selectbox("Chest Pain Type", ["0 - Typical Angina", "1 - Atypical", "2 - Non-anginal", "3 - Asymptomatic"])
        trestbps = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
        chol = st.number_input("Serum Cholesterol (mg/dl)", 100, 600, 200)
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["Yes", "No"])
        restecg = st.selectbox("Resting ECG Results", ["0 - Normal", "1 - ST-T Abnormality", "2 - LV Hypertrophy"])

    with col2:
        thalachh = st.number_input("Maximum Heart Rate Achieved", 60, 220, 150)
        exang = st.selectbox("Exercise Induced Angina", ["Yes", "No"])
        oldpeak = st.number_input("Oldpeak (ST Depression)", 0.0, 6.0, 1.0, step=0.1)
        slope = st.selectbox("Slope of ST Segment", ["0 - Upsloping", "1 - Flat", "2 - Downsloping"])
        ca = st.selectbox("Major Vessels Colored", [0, 1, 2, 3])
        thal = st.selectbox("Thalassemia", ["1 - Normal", "2 - Fixed Defect", "3 - Reversible Defect"])

    submit = st.form_submit_button("🔍 Predict Risk")

# ========== PREDICTION ==========
if submit:
    # Encoding
    sex = 1 if sex == "Male" else 0
    cp = int(cp.split(" ")[0])
    fbs = 1 if fbs == "Yes" else 0
    restecg = int(restecg.split(" ")[0])
    exang = 1 if exang == "Yes" else 0
    slope = int(slope.split(" ")[0])
    thal = int(thal.split(" ")[0])

    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                            thalachh, exang, oldpeak, slope, ca, thal]])
    
    prediction = model.predict(input_data)[0]
    probability = round(model.predict_proba(input_data)[0][1] * 100, 2)

    if prediction == 1:
        st.error(f"🔴 High Risk of Heart Disease ({probability}%)")
    else:
        st.success(f"🟢 Low Risk of Heart Disease ({100 - probability}%)")

# ============ BATCH PREDICTION =============
st.header("📁 Upload CSV or Excel File")

uploaded_file = st.file_uploader("Upload File (CSV or XLSX)", type=["csv", "xlsx"])

if uploaded_file:
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.success("✅ File uploaded successfully.")
        st.dataframe(df.head())

        # Predict
        predictions = model.predict(df)
        probs = model.predict_proba(df)[:, 1]
        df['Risk Prediction'] = np.where(predictions == 1, "High Risk", "Low Risk")
        df['Risk Probability (%)'] = (probs * 100).round(2)

        st.subheader("📊 Prediction Summary")
        st.dataframe(df[['Risk Prediction']].value_counts().reset_index().rename(columns={0: "Count"}))

        st.subheader("📋 Full Results")
        st.dataframe(df)

        csv_download = df.to_csv(index=False).encode()
        st.download_button("⬇️ Download Results as CSV", csv_download, "heart_risk_predictions.csv", "text/csv")

    except Exception as e:
        st.error(f"❌ Error processing file: {e}")
