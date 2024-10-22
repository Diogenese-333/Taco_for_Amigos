#protein 0.8 per weight
#fibers 25-30 per day
#โปรแกรมหลิว คำนวณโปรตีนทั้งหมดที่ร่างกายต้องการต่อวัน fiber_need , protein_need
#โปรแกรมของกวางคำนวณว่าในทาโก้หนึ่งชิ้นมีปริมาณโปรตีนอยู่เท่าไหร่ tacos_fiber , tacos_protein
import streamlit as st
from tacobar import *
def Protein_Sufficiency(tacos_protein, protein_need):
    # Ensure inputs are not None
    if tacos_protein is None:
        tacos_protein = 0.0  # Default to 0 if None
    if tacos_protein > protein_need:
        recommend_protein = tacos_protein - protein_need
        st.write(f"You overeat MEAT like {recommend_protein:.2f}! , seriously you need more Fiber.")
    elif tacos_protein < protein_need:
        recommend_protein = protein_need - tacos_protein 
        st.write(f"You overeat MEAT like {recommend_protein:.2f}! , seriously you need more Fiber.")
    # else:
    #     st.write("Bon Appétit!!!")
    #     # return 0  # No recommendation needed

    # return recommend_protein

def Fiber_Sufficiency(tacos_fiber, fiber_need):
    # Ensure inputs are not None
    if tacos_fiber is None:
        tacos_fiber = 0.0  # Default to 0 if None
    
    if tacos_fiber > fiber_need:
        recommend_fiber = tacos_fiber - fiber_need
        st.write(f"You overeat Veggies like {recommend_fiber:.2f} , seriously you need more MEAT.")
    elif tacos_fiber < fiber_need:
        recommend_fiber = fiber_need - tacos_fiber
        st.write(f"You need more {recommend_fiber:.2f} grams of fiber.")
    # else:
    #     st.write("Bon Appétit!!!")
        # return 0  # No recommendation needed

    # return recommend_fiber

# def Calculate():
#     SEX = st.radio("What's your SEX", ('Female', 'Male','Child'))
#     st.write("You selected:", SEX)
#     protein_needs= None
#     if SEX == 'Female':
#           weight1 = st.number_input("Weight (in kg)", min_value=1,max_value=400,value=None)
#           Height1 = st.number_input ("Height (in CM )",min_value=50,max_value=220,value=None)
#           Age1=st.number_input ("Age",min_value=13,max_value=120,value=None)
#           if weight1 is not None and Height1 and Age1:
#             BMRfemale = 66.0 + (13.7*weight1) + (5.0 * Height1) - (6.8 * Age1) 
#             Fiber_needs = None
#             Activitylevel = st.radio("Activity level",('Select your activity level', 'Little/no exercise', 'Exercise often'))
#             if Activitylevel == 'Little/no exercise':
#                 protein_needs = weight1 * 0.8  # Example value for sedentary females
#                 Fiber_needs =(BMRfemale*1.2)/1000*14  # Example value for sedentary females
             
#             elif Activitylevel =='Exercise often':
#                   protein_needs = weight1 * 1.0  # Example value for active females
#                   Fiber_needs = (BMRfemale*1.7)/1000*14 # Example value for active females
#             if protein_needs  is not None:
#                 if  Activitylevel != 'Little/no exercise''Exercise often':
#                     st.write('You need approximately', round(protein_needs, 2), 'grams of protein per day.')
#             if Fiber_needs is not None:
#                if  Activitylevel != 'Little/no exercise''Exercise often':
#                  st.write('You need approximately', round(Fiber_needs, 2), 'grams of fiber per day.')
#     if SEX == 'Male': 
#         Height1 = st.number_input ("Height (in CM )",min_value=50,max_value=280,value=None)
#         weight1 = st.number_input("Weight (in kg)",min_value=1,max_value=400,value=None)
#         Age1=st.number_input ("Age",min_value=13,max_value=120,value=None)
#         if weight1 is not None and Height1 and Age1:
#             BMRmale = 665 + (9.6 * weight1) + (1.8 * Height1) - (4.7 * Age1)   
#             Fiber_needs = None
#             Activitylevel = st.radio("Activity level",('Select your activity level', 'Little/no exercise', 'Exercise often'))
#             if Activitylevel == 'Little/no exercise':
#                  protein_needs = weight1 * 0.9  # Example value for sedentary males
#                  Fiber_needs = (BMRmale*1.2)/1000*14  # Example value for sedentary males
            
#             elif Activitylevel =='Exercise often':
#                  protein_needs = weight1 * 1.2 # Example value for active males
#                  Fiber_needs = (BMRmale*1.7)/1000*14  # Example value for active males
#             if   protein_needs  is not None:
#                  if  Activitylevel != 'Little/no exercise''Exercise often':
#                   st.write('You need approximately', round(protein_needs, 2), 'grams of protein per day.')
#             if Fiber_needs is not None:
#                if  Activitylevel != 'Little/no exercise''Exercise often':
#                  st.write('You need approximately', round(Fiber_needs, 2), 'grams of fiber per day.')
                        
#     if SEX == 'Child':
#         Height1 = st.number_input ("Height (in CM )",min_value=1,max_value=150,value=None)
#         weight1 = st.number_input("Weight (in kg)", min_value=1,max_value=100,value=None)
#         Age1 = st.number_input("Age for child (6-12)", min_value=6, max_value=None)
#         if Height1 and weight1 and Age1:
#             Fiber_needs=Age1+5
#             st.write('You need approximately',Fiber_needs, 'gram of  Fiber today.')
#     return protein_needs,Fiber_needs
    