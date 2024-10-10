import streamlit as st

def Fiber():
    SEX1 = st.radio("What's your SEX", ('Female', 'Male', 'Child'))
    st.write("You selected:", SEX1)

    if SEX1 == 'Female':
        Height1 = st.number_input ("Height (in CM )",min_value=50,max_value=220)
        weight1 = st.number_input("Weight (in kg)", min_value=1,max_value=400)
        Age1=st.number_input ("Age",min_value=13,max_value=120)
        BMRfemale = 66 + (13.7 * weight1) + (5 * Height1) - (6.8 * Age1) 
        Activitylevel1 = st.radio("Activity level", ('Little/no exercise', 'Exercise often'))
        st.write("You selected:", Activitylevel1)
        if Activitylevel1 == 'Little/no exercise':
           Fiber_needs = (BMRfemale*1.2)/1000*14  # Example value for sedentary females
           st.write('You need approximately',  Fiber_needs, 'gram of  Fiber today.')
            
        else:
             Fiber_needs = (BMRfemale*1.7)/1000*14 # Example value for active females
             st.write('You need approximately',  Fiber_needs, 'gram of  Fiber today.')
    if SEX1 == 'Male':
        Height1 = st.number_input ("Height (in CM )",min_value=50,max_value=280)
        weight1 = st.number_input("Weight (in kg)", min_value=1,max_value=400)
        Age1=st.number_input ("Age",min_value=13,max_value=120)
        BMRmale = 665 + (9.6 * weight1) + (1.8 * Height1) - (4.7 * Age1)   
        st.write("You selected:", Activitylevel1)
        if Activitylevel1 == 'Little/no exercise':
             Fiber_needs = (BMRmale*1.2)/1000*14  # Example value for sedentary males
             st.write('You need approximately',  Fiber_needs, 'gram of  Fiber today.')
        else:
             Fiber_needs = (BMRmale*1.7)/1000*14  # Example value for active males
             st.write('You need approximately',  Fiber_needs, 'gram of  Fiber today.')
    if SEX1 == 'Child':
        Height1 = st.number_input ("Height (in CM )",min_value=0)
        weight1 = st.number_input("Weight (in kg)", min_value=0)
        age = st.number_input("Age for child (6-12)", min_value=6, max_value=12)
        st.write('You need approximately',  Fiber_needs, 'gram of  Fiber today.')

Fiber()       