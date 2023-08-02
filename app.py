import streamlit as st
import streamlit.components.v1 as stc

#import our app
from ml_app import run_ml_app

html_temp = """
            <div style="background-color:#3872fb;padding:10px;border-radius:10px">
		    <h1 style="color:white;text-align:center;">Diabetes Prediction App </h1>
		    <h4 style="color:white;text-align:center;">created by: Lucky-7 Team</h4>
		    </div>
            """

desc_temp = """
            ### Diabetes Prediction App
            This application will be used by medical personnel to predict whether someone has the potential to suffer from diabetes or not 
            #### Data Source
            - https://raw.githubusercontent.com/mdimasprasetyo/ds27_deployment/main/diabetes_prediction_dataset.csv
            #### App Content
            - Exploratory Data Analysis
            - Machine Learning Section
            """
about_temp = """
             ### Member of Lucky Seven Team
             - Aldi Damora Siregar
             reach me on: https://www.linkedin.com/in/aldidamora/
             - Atik Apprinda Paramita
             reach me on: https://www.linkedin.com/in/atik-apprinda
             - Muhammad Dimas Saputra
             reach me on: https://www.linkedin.com/in/mdimasprasetyo/
             - Muhammad Luthfi Septiawan
             reach me on: https://www.linkedin.com/in/muhammadluthfiseptiawan/
             - Pingky Kandy
             reach me on: https://www.linkedin.com/in/pingky-kandy/
             """

def main():
    stc.html(html_temp)

    menu = ["Home","Machine Learning", "About Us"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.markdown(desc_temp, unsafe_allow_html=True)
    elif choice == "Machine Learning":
        st.subheader("Machine Learning Section")
        run_ml_app()
    elif choice == "About Us":
        st.markdown(about_temp, unsafe_allow_html=True)
    

if __name__ == '__main__':
    main()