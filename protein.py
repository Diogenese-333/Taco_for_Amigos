import streamlit as st

def protein():
   
    SEX = st.radio("What's your SEX", ('Female', 'Male'))
    st.write("You selected:", SEX)
    #Height = st.number_input ("Height (in CM )",min_value=0)
    weight = st.number_input("Weight (in kg)", min_value=0)

    Activitylevel = st.radio("Activity level", ('Little/no exercise', 'Exercise often'))
    st.write("You selected:", Activitylevel)
    
    if SEX == 'Female':
        if Activitylevel == 'Little/no exercise':
            protein_needs = weight * 0.8  # Example value for sedentary females
            st.write('You need approximately', protein_needs, 'grams of protein today.')
        else:
            protein_needs = weight * 1.0  # Example value for active females
            st.write('You need approximately', protein_needs, 'grams of protein today.')
    if SEX == 'Male': 
        if Activitylevel == 'Little/no exercise':
            protein_needs = weight * 0.9  # Example value for sedentary males
            st.write('You need approximately', protein_needs, 'grams of protein today.')
        else:
            protein_needs = weight * 1.2  # Example value for active males
            st.write('You need approximately', protein_needs, 'grams of protein today.')
    return protein_needs

protein()
