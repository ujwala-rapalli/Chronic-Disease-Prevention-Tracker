import streamlit as st
import pandas as pd
import joblib

# ------------------------------
# Load Trained Models (.pkl files)
# ------------------------------
models = {
    "Diabetes_Risk": joblib.load("Diabetes_Risk_model.pkl"),
    "Hypertension_Risk": joblib.load("Hypertension_Risk_model.pkl"),
    "Cardio_Risk": joblib.load("Cardio_Risk_model.pkl"),
    "Cholesterol_Level": joblib.load("Cholesterol_Level_model.pkl"),
}

# ------------------------------
# Label Definitions
# ------------------------------
risk_labels = {
    'Diabetes_Risk': ['No Diabetes', 'Prediabetes', 'Diabetes'],
    'Hypertension_Risk': ['No Hypertension', 'Hypertension'],
    'Cardio_Risk': ['No Cardiac Risk', 'Cardiac Risk'],
    'Cholesterol_Level': ['Normal', 'Above Normal', 'Well Above Normal']
}

# ------------------------------
# Recommendations for Each Risk Level
# ------------------------------
recommendations = {
    'Diabetes_Risk': {
        0: "Maintain current lifestyle, eat balanced diet, regular exercise.",
        1: "You're at risk of diabetes. Reduce sugar intake, increase activity, monitor glucose.",
        2: "You should consult a doctor. Follow diabetic-friendly diet and medication if advised."
    },
    'Hypertension_Risk': {
        0: "Blood pressure is in check. Limit salt, keep exercising.",
        1: "High BP detected. Reduce sodium, avoid stress, check regularly."
    },
    'Cardio_Risk': {
        0: "Heart health looks good. Continue healthy eating and exercise.",
        1: "Risk of heart issues. Avoid smoking, fatty foods. Get regular checkups."
    },
    'Cholesterol_Level': {
        0: "Your cholesterol level is normal. Maintain a fiber-rich diet.",
        1: "Slightly elevated cholesterol. Avoid fried foods, add oats, flaxseed.",
        2: "High cholesterol. Consider medications and serious dietary changes."
    }
}

# ------------------------------
# Streamlit UI
# ------------------------------
st.set_page_config(page_title="Chronic Disease Risk Predictor", layout="centered")
st.title("🩺 Chronic Disease Risk Predictor")
st.write("Answer the questions below to assess your health risk for chronic diseases.")

# Collect user input
age = st.number_input("📅 Age", 0, 120)
bmi = st.number_input("⚖️ BMI (Body Mass Index)", 0.0, 60.0)
glucose = st.number_input("🩸 Fasting Blood Glucose (mg/dL)", 50.0, 300.0)
sys_bp = st.number_input("💓 Systolic BP (Upper number)", 80, 200)
dia_bp = st.number_input("💓 Diastolic BP (Lower number)", 50, 150)
smoke = st.radio("🚬 Do you smoke?", ['No', 'Yes']) == 'Yes'
alcohol = st.radio("🍷 Do you consume alcohol?", ['No', 'Yes']) == 'Yes'
activity = st.selectbox("🏃 How often do you exercise per week?", ['Rarely', 'Sometimes', 'Regularly'])
income = st.selectbox("💸 What is your household spending ability?", ['Low', 'Medium', 'High'])

# Process user input
user_data = {
    "Age": age,
    "BMI": bmi,
    "Smoking": int(smoke),
    "Alcohol": int(alcohol),
    "Physical_Activity": {"Rarely": 0, "Sometimes": 1, "Regularly": 2}[activity],
    "Systolic_BP": sys_bp,
    "Diastolic_BP": dia_bp,
    "Fasting_Glucose": glucose,
    "Income": {"Low": 1, "Medium": 2, "High": 3}[income]
}
features = ['Age', 'BMI', 'Smoking', 'Alcohol', 'Physical_Activity', 
            'Systolic_BP', 'Diastolic_BP', 'Fasting_Glucose', 'Income']

# Create DataFrame and reorder columns to match training
user_input = pd.DataFrame([user_data])[features]


# ------------------------------
# Prediction and Output
# ------------------------------
if st.button("🔍 Predict My Risks"):
    st.subheader("🧠 Model Predictions & Suggestions")

    for disease, model in models.items():
        pred = model.predict(user_input)[0]
        label = risk_labels[disease][int(pred)]
        advice = recommendations[disease].get(int(pred), "No specific recommendation.")
        
        st.markdown(f"### 📌 {disease.replace('_', ' ')}")
        st.write(f"**Prediction:** {label}")
        st.info(f"💡 Recommendation: {advice}")
