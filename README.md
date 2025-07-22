# Heart-Disease-Risk-Assessment-Model

# ❤️ Heart Disease Prediction with Machine Learning
---
# 📊 Project Overview
---
Heart disease is the leading cause of death globally. Early identification of patients at risk allows for timely interventions, lifestyle adjustments, and improved patient outcomes. This project builds a machine learning pipeline to predict the likelihood of heart disease based on clinical indicators.

Using a cleaned dataset of 602 patients and 14 clinical features, several models were built and evaluated. The Random Forest Classifier demonstrated the best performance and was deployed as the final model.
---
# 🌐 Features Used

**Feature :**

**Description**

**age :**

* Age of patient

* Risk increases with age due to arterial stiffness and heart strain

**sex :**

* 1 = male, 0 = female

* Males are generally at higher risk before menopause

**cp :**

* Chest pain type (0-3)

* Asymptomatic and typical angina are stronger indicators of risk

**trestbps :**

* Resting blood pressure

* >130 mmHg indicates elevated risk

**chol :**

* Cholesterol in mg/dl

* >240 mg/dl is a red flag

**fbs :**

* Fasting blood sugar >120 mg/dl (1 = true, 0 = false)

* Indicates diabetes, a major risk factor

**restecg :**

* Resting ECG results (0-2)

* Abnormalities suggest past or ongoing cardiac issues

**thalachh :**

* Max heart rate achieved

* Low values may signal heart weakness

**exang :**

* Exercise-induced angina (1 = yes, 0 = no)

* Positive result indicates ischemia

**oldpeak :**

* ST depression

* Higher values reflect more heart strain

**slope :**

* Slope of ST segment

* Downsloping/flat curves are concerning

**ca :**

* Major vessels colored (0-4)

* More vessels affected indicates higher risk

**thal :**

* Thalassemia result (1-3)

* Fixed or reversible defects indicate serious problems

**target :**

* 1 = heart disease, 0 = no disease

* The outcome variable
---
# 📊 Exploratory Data Insights

* Age & Gender: Older males had significantly higher risk

* Chest Pain (cp): Asymptomatic and typical angina types were most correlated with heart disease

* Exercise Angina (exang): Presence of angina during exercise often signaled positive diagnosis

* Cholesterol & BP: Moderate predictive power, especially when combined with others

Number of vessels colored (ca): Strongest individual predictor
---
# 🏃‍♂️ Modeling and Evaluation

**Several models were built:**

# 1. Logistic Regression

* Accuracy: 0.68

* Precision: 0.66

* Recall: 0.72

* F1 Score: 0.69

# 2. Decision Tree

* Accuracy: 0.74

* ROC AUC: 0.74

* Precision: 0.73

* Recall: 0.73

* F1 Score: 0.73

# 3. XGBoost Classifier

* Accuracy: 0.73

* ROC AUC: 0.73

* Precision: 0.70

* Recall: 0.78

F1 Score: 0.74
---
# ⭐ 4. Random Forest (Final Model)

* Train Accuracy: 0.89

* Test Accuracy: 0.76

* Precision: 0.75

* Recall: 0.78

* F1 Score: 0.76

* ROC AUC: 0.76

* Chosen for its balance of performance and generalization, especially after hyperparameter tuning
---
# 🚀 Deployment

* A Streamlit web app was created that allows:

* Manual prediction by filling in patient values

* Batch prediction via CSV/Excel upload

* Feature explanations and risk guidelines

* Probability output of heart disease risk
---
# 💼 Business Recommendations
---
* Clinical Decision Support: This model can assist doctors in screening patients, especially in rural or resource-limited settings.

* Early Detection: Individuals at moderate risk can be flagged early and monitored more closely.

* Public Health Strategy: Use demographic and medical patterns to inform national-level prevention campaigns.

* Insurance & Underwriting: Helps insurers better assess cardiac risk and offer more accurate premium pricing.

* Integrate with EHR Systems: Automatically flag at-risk patients in hospital systems using real-time lab input.
---
# 🎓 Acknowledgments

* Dataset was sourced and cleaned from public medical repositories

* Libraries used: pandas, numpy, scikit-learn, xgboost, matplotlib, seaborn, streamlit
