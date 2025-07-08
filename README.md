# Chronic-Disease-Prevention-Tracker
Chronic Disease Prevention Tracker


An early-warning system to monitor and predict the risk of chronic diseases like **diabetes**, **hypertension**, **cardiovascular conditions**, and **high cholesterol** — while also providing **personalized intervention suggestions**.


🔗 **Live Demo:** [Streamlit App](https://chronic-disease-prevention-tracker-mygmwgckcin2uhjqdyhiip.streamlit.app/)  
📦 **GitHub Repo:** [Chronic Disease Prevention Tracker](https://github.com/ujwala-rapalli/Chronic-Disease-Prevention-Tracker)

---

## 🧠 Problem Statement

Create a system that continuously monitors lifestyle and health indicators to:
- Detect early signs of **chronic diseases** (Diabetes, Hypertension, etc.)
- Analyze risk progression over time
- Recommend timely, preventive **interventions**

---

## 💡 Key Features

- ✅ **Multi-Disease Risk Prediction:** Predicts 4 chronic conditions individually using ML models.
- ✅ **Personalized Input:** Simple, friendly interface to collect health habits and biomarker data.
- ✅ **Custom Recommendations:** Each output is mapped to lifestyle-based suggestions.
- ✅ **Fully Deployed Solution:** End-to-end pipeline — from data preprocessing to live app.
- ✅ **Modular Codebase:** Easily extendable for new diseases or metrics.

---

## 🛠️ Technologies & Architecture

| Layer               | Tools / Approach |
|--------------------|------------------|
| Frontend           | Streamlit (UI/UX for user input and results) |
| Backend Logic      | Python, Pandas, NumPy |
| Machine Learning   | XGBoost, scikit-learn, Joblib |
| Model Deployment   | Streamlit Cloud |
| Data Management    | Manual preprocessing, encoding, balancing |

### 🧩 Modular Structure
- `Monitoring Engine:` Collects user metrics via UI
- `ML Models:` Predict disease risk using health & lifestyle data
- `Recommendations Engine:` Provides guidance per condition
- `Tracking Component:` Can be extended to monitor risk over time

---

## 🧪 Input Features Used

| Feature                | Description                        |
|------------------------|------------------------------------|
| Age                    | User's age                         |
| BMI                    | Body Mass Index                    |
| Fasting_Glucose        | Blood sugar level (mg/dL)          |
| Systolic_BP / Diastolic_BP | Blood pressure readings        |
| Smoking / Alcohol      | Lifestyle habits (encoded)         |
| Physical_Activity      | Activity level (encoded)           |
| Spending Ability       | Mapped from "income" (low/med/high)|

---

## 📊 Output Risk Categories

| Model                | Classes                            |
|----------------------|------------------------------------|
| Diabetes_Risk        | No Diabetes, Prediabetes, Diabetes |
| Hypertension_Risk    | No Hypertension, Hypertension      |
| Cardio_Risk          | No Risk, At Risk                   |
| Cholesterol_Level    | Normal, Above Normal, High         |

Each prediction is mapped to an actionable **health recommendation**.

---

## 🧠 Skills Demonstrated

### ✅ **AI/ML Expertise**
- Trained **XGBoost classifiers** per disease with class balancing
- Encoded and cleaned health data using real-world mappings
- Evaluated using accuracy, F1-score, and confusion matrices

### ✅ **Critical Thinking**
- Modeled **gradual progression** of diseases
- Factored **multiple correlated inputs** (e.g., BP + BMI + glucose)
- Considered cost-effectiveness of preventive interventions

### ✅ **Software Architecture**
- Separated **input → prediction → recommendation** stages
- Designed for scalability (can plug in more diseases or features)
- Uses **Streamlit** for rapid UI with minimal backend load

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/ujwala-rapalli/Chronic-Disease-Prevention-Tracker.git
cd Chronic-Disease-Prevention-Tracker

pip install -r requirements.txt
streamlit run app.py
