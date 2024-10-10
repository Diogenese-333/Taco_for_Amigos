import streamlit as st

def Fiber():
    SEX1 = st.radio("What's your SEX", ('Female', 'Male', 'Child'))
    st.write("You selected:", SEX1)
    initial_value = 0
    if SEX1 == 'Female':
        Height1 = st.number_input ("Height (in CM )",min_value=50,max_value=220,value=None)
        weight1 = st.number_input("Weight (in kg)", min_value=1,max_value=400,value=None)
        Age1=st.number_input ("Age",min_value=13,max_value=120,value=None)

        if Height1 and weight1 and Age1:
            BMRfemale = 66.0 + (13.7*weight1) + (5.0 * Height1) - (6.8 * Age1) 
            Fiber_needs = None
            Activitylevel1 = st.radio("Activity level", 
            ('Select your activity level', 'Little/no exercise', 'Exercise often'))
            st.write("You selected:", Activitylevel1)
            if Activitylevel1 == 'Little/no exercise':
              Fiber_needs =(BMRfemale*1.2)/1000*14  # Example value for sedentary females
             
            elif Activitylevel1 == 'Exercise often':
                Fiber_needs = (BMRfemale*1.7)/1000*14 # Example value for active females
                
            if Fiber_needs is not None:
               if  Activitylevel1 != 'Little/no exercise''Exercise often':
                 st.write('You need approximately', round(Fiber_needs, 2), 'grams of fiber per day.')
               
               
               
    if SEX1 == 'Male':
        Height1 = st.number_input ("Height (in CM )",min_value=50,max_value=280,value=None)
        weight1 = st.number_input("Weight (in kg)",min_value=1,max_value=400,value=None)
        Age1=st.number_input ("Age",min_value=13,max_value=120,value=None)
        if Height1 and weight1 and Age1:
            BMRmale = 665 + (9.6 * weight1) + (1.8 * Height1) - (4.7 * Age1)   
            Fiber_needs = None
            Activitylevel1 = st.radio("Activity level", 
            ('Select your activity level', 'Little/no exercise', 'Exercise often'))
            if Activitylevel1 == 'Little/no exercise':
             Fiber_needs = (BMRmale*1.2)/1000*14  # Example value for sedentary males
             
            elif Activitylevel1 == 'Exercise often':
             Fiber_needs = (BMRmale*1.7)/1000*14  # Example value for active males
             
            if Fiber_needs is not None:
               if  Activitylevel1 != 'Little/no exercise''Exercise often':
                 st.write('You need approximately', round(Fiber_needs, 2), 'grams of fiber per day.')
               
    if SEX1 == 'Child':
        Height1 = st.number_input ("Height (in CM )",min_value=1,max_value=150,value=None)
        weight1 = st.number_input("Weight (in kg)", min_value=1,max_value=100,value=None)
        age = st.number_input("Age for child (6-12)", min_value=6, max_value=None)
        if Height1 and weight1 and Age1:
            Fiber_needs=age+5
            st.write('You need approximately',  Fiber_needs, 'gram of  Fiber today.')

Fiber()       