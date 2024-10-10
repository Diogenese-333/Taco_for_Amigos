import streamlit as st

def protein():
   
    SEX = st.radio("What's your SEX", ('Female', 'Male'))
    st.write("You selected:", SEX)
    #Height = st.number_input ("Height (in CM )",min_value=0)
    protein_needs= None

    
    if SEX == 'Female':
          weight = st.number_input("Weight (in kg)", min_value=1,max_value=400,value=None)
          if weight is not None:
             Activitylevel = st.radio("Activity level", 
             ('Select your activity level', 'Little/no exercise', 'Exercise often'))
             if Activitylevel == 'Little/no exercise':
                protein_needs = weight * 0.8  # Example value for sedentary females
             
             elif Activitylevel =='Exercise often':
                  protein_needs = weight * 1.0  # Example value for active females
             if    protein_needs  is not None:
                 if  Activitylevel != 'Little/no exercise''Exercise often':
                   st.write('You need approximately', round(protein_needs, 2), 'grams of protein per day.')
    if SEX == 'Male': 
        weight = st.number_input("Weight (in kg)", min_value=1,max_value=400,value=None)
        if weight is not None:
             Activitylevel = st.radio("Activity level", 
             ('Select your activity level', 'Little/no exercise', 'Exercise often'))
             if Activitylevel == 'Little/no exercise':
                 protein_needs = weight * 0.9  # Example value for sedentary males
            
             elif Activitylevel =='Exercise often':
                 protein_needs = weight * 1.2 # Example value for active females
             if    protein_needs  is not None:
                 if  Activitylevel != 'Little/no exercise''Exercise often':
                  st.write('You need approximately', round(protein_needs, 2), 'grams of protein per day.')
    return protein_needs

protein()
