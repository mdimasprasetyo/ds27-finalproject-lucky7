import streamlit as st
import numpy as np

#load ML package
import joblib
import os

gen = {'Female': 1, 'Male': 2}
smo = {'current': 1, 'non-smoker': 2, 'past_smoker': 3}
hyp = {'Yes':1, 'No':0}
hd = {'Yes':1, 'No':0}

attribute_info = """
                 - Gender : Male, Female
                 - Age : 0-200
                 - BMI : 0-100
                 - HbA1c Level : 0-10
                 - Blood Glucose : 0-500
                 - Hypertension : Yes, No
                 - Heart Disease : Yes, No
                 - Smoking History : current, non-smoker, past_smoker
                 """

def get_value(val,my_dict):
    for key, value in my_dict.items():
        if val == key:
            return value
        
@st.cache
def load_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file),'rb'))
    return loaded_model

def run_ml_app():
    st.subheader("ML section")

    with st.expander("Attribute Info"):
        st.markdown(attribute_info)

    st.subheader("Input Your Data")
    age = st.number_input("Age",0,200)
    bmi = st.number_input("BMI",0,100)
    hba1c = st.number_input("HbA1c Level",0,10)
    blood_gluc = st.number_input("Blood Glucose",0,500)
    gender = st.radio('Gender', ['Male','Female'])
    hypertension = st.radio('Hypertension', ['Yes','No'])
    heart_disease = st.radio('Heart Disease', ['Yes','No'])
    smoking_history = st.radio("Smoking History", ['current', 'non-smoker', 'past_smoker'])
    

    with st.expander("Your Selected Options"):
        result = {
            'Age':age,
            'BMI':bmi,
            'HbA1c Level':hba1c,
            'Blood Glucose':blood_gluc,
            'Gender':gender,
            'Hypertension':hypertension,
            'Heart Disease':heart_disease,
            'Smoking History': smoking_history
        }
    
    encoded_result = []
    for i in result.values():
        if type(i) == int:
            encoded_result.append(i)
        elif i in ['Male','Female']:
            res = get_value(i, gen)
            encoded_result.append(res)
        elif i in ['Yes','No']:
            res = get_value(i, hyp)
            encoded_result.append(res)
        elif i in ['Yes','No']:
            res = get_value(i, hd)
            encoded_result.append(res)
        elif i in ['current', 'non-smoker', 'past_smoker']:
            res = get_value(i, smo)
            encoded_result.append(res)
    
    ## prediction section
    st.subheader('Prediction Result')
    single_sample = np.array(encoded_result).reshape(1,-1)

    model = load_model("diabetes_model.pkl")

    prediction = model.predict(single_sample)
    pred_proba = model.predict_proba(single_sample)
    # st.write(prediction)
    # st.write(pred_proba)

    pred_probability_score = {'Risk of Diabetes':round(pred_proba[0][1]*100,4)}
                            # 'Negative Diabetes':round(pred_proba[0][0]*100,4)}

    if prediction == 1:
        st.success("Don't Give Up!!")
        
        st.write(pred_probability_score)
    else:
        st.warning("Stay Healthy, Cheers :))")
        st.write(pred_probability_score)