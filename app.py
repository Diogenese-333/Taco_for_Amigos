import time
import json
import streamlit as st
import requests
from calculate import *
from tacobar import *
from streamlit_lottie import st_lottie 
from streamlit_lottie import st_lottie_spinner
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_file_path = "Animation1.json"
lottie_loading_path = "Loading Animation.json"
lottie_json = load_lottiefile(lottie_file_path)
lottie_json1 = load_lottiefile(lottie_loading_path)
st_lottie(lottie_json, key="lottie")
def main():
        # Initialize session state variables
    # Initialize Session State keys if they do not exist
    if "meat_price" not in st.session_state:
        st.session_state.meat_price = 0
    if "ingredient_price" not in st.session_state:
        st.session_state.ingredient_price = 0
    if "vegetable_price" not in st.session_state:
        st.session_state.vegetable_price = 0
    if "sauce_price" not in st.session_state:
        st.session_state.sauce_price = 0
    if "total_price" not in st.session_state:
        st.session_state.total_price = 0
    if "total_weight" not in st.session_state:
        st.session_state.total_weight = 0
    if "total_protein_weight" not in st.session_state:
        st.session_state.total_protein_weight = 0
    if "total_fiber_weight" not in st.session_state:
        st.session_state.total_fiber_weight = 0
    st.session_state.show_radio = False
    global total_protein_weight,total_fiber_weight
    # รูปแบบแอป Streamlit
    st.title(":rainbow[Tacos For Amigos]")
    hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)
    st.toast("Hola Amigo",icon="😃")
    # Select meat type
    meat_type = st.selectbox("Select Meat Type", list(meat_per_taco.keys()))

    # Select other ingredients
    selected_ingredients = st.multiselect("Select Other Ingredients", list(ingredients.keys()))

    # Select vegetables
    selected_vegetables = st.multiselect("Select Vegetables", list(vegetable_prices.keys()))

    # Select sauces
    selected_sauces = st.multiselect("Select Sauces", list(sauce_prices.keys()))

    # Calculate and display results
    if st.button("Calculate"):
        st.session_state.meat_price = calculate_meat_price(meat_type)
        st.session_state.ingredient_price = calculate_ingredient_price(selected_ingredients)
        st.session_state.vegetable_price = calculate_vegetable_price(selected_vegetables)
        st.session_state.sauce_price = calculate_sauce_price(selected_sauces)
        st.session_state.total_price = (st.session_state.meat_price + 
                                        st.session_state.ingredient_price + 
                                        st.session_state.vegetable_price + 
                                        st.session_state.sauce_price)

        st.session_state.total_weight = calculate_total_weight(meat_type, selected_ingredients, selected_vegetables, selected_sauces)
        # Store calculated values in session state
        st.session_state.total_protein_weight = calculate_total_protein_weight(meat_type, selected_ingredients)
        st.session_state.total_fiber_weight = calculate_total_fiber_weight(selected_vegetables)
        # Display results
        st.write(f"Total price for your tacos is {st.session_state.total_price:.2f} THB.")
        st.write(f"Total weight for your tacos is {st.session_state.total_weight:.2f} g.")
        st.write(f"Total protein for this tacos is {st.session_state.total_protein_weight:.2f} g.")
        st.write(f"Total fiber for this tacos is {st.session_state.total_fiber_weight:.2f} g.")
        with st_lottie_spinner(lottie_json1, key="download"):
            time.sleep(5)
            st.session_state.show_radio = True
        st.balloons()
        # Set the flag to show the radio button
        
#คำนวณ สารอาหาร   
    if st.session_state.show_radio:
        SEX = st.radio("What's your SEX", ('Female', 'Male','Child'))
        st.write("You selected:", SEX)
        # Initialize Fiber_needs to None
        Fiber_needs = None
        protein_needs = None
        if SEX == 'Female':
            weight1 = st.number_input("Weight (in kg)", min_value=1,max_value=400,value=None)
            Height1 = st.number_input ("Height (in CM )",min_value=50,max_value=220,value=None)
            Age1=st.number_input ("Age",min_value=13,max_value=120,value=None)
            if weight1 is not None and Height1 and Age1:
                BMRfemale = 66.0 + (13.7*weight1) + (5.0 * Height1) - (6.8 * Age1) 
                Fiber_needs = None
                Activitylevel = st.radio("Activity level",('Select your activity level', 'Little/no exercise', 'Exercise often'))
                if Activitylevel == 'Little/no exercise':
                    protein_needs = weight1 * 0.8  # Example value for sedentary females
                    Fiber_needs =(BMRfemale*1.2)/1000*14  # Example value for sedentary females
                        
                elif Activitylevel =='Exercise often':
                    protein_needs = weight1 * 1.0  # Example value for active females
                    Fiber_needs = (BMRfemale*1.7)/1000*14 # Example value for active females
                if protein_needs  is not None:
                    if  Activitylevel != 'Little/no exercise''Exercise often':
                        st.write('You need approximately', round(protein_needs, 2), 'grams of protein per day.')
                if Fiber_needs is not None:
                    if  Activitylevel != 'Little/no exercise''Exercise often':
                        st.write('You need approximately', round(Fiber_needs, 2), 'grams of fiber per day.')
        if SEX == 'Male': 
            Height1 = st.number_input ("Height (in CM )",min_value=50,max_value=280,value=None)
            weight1 = st.number_input("Weight (in kg)",min_value=1,max_value=400,value=None)
            Age1=st.number_input ("Age",min_value=13,max_value=120,value=None)
            if weight1 is not None and Height1 and Age1:
                BMRmale = 665 + (9.6 * weight1) + (1.8 * Height1) - (4.7 * Age1)   
                Fiber_needs = None
                Activitylevel = st.radio("Activity level",('Select your activity level', 'Little/no exercise', 'Exercise often'))
                if Activitylevel == 'Little/no exercise':
                    protein_needs = weight1 * 0.9  # Example value for sedentary males
                    Fiber_needs = (BMRmale*1.2)/1000*14  # Example value for sedentary males
                        
                elif Activitylevel =='Exercise often':
                    protein_needs = weight1 * 1.2 # Example value for active males
                    Fiber_needs = (BMRmale*1.7)/1000*14  # Example value for active males
                if  protein_needs  is not None:
                    if  Activitylevel != 'Little/no exercise''Exercise often':
                        st.write('You need approximately', round(protein_needs, 2), 'grams of protein per day.')
                if Fiber_needs is not None:
                    if  Activitylevel != 'Little/no exercise''Exercise often':
                        st.write('You need approximately', round(Fiber_needs, 2), 'grams of fiber per day.')
                                    
        if SEX == 'Child': #for a child
            Height1 = st.number_input ("Height (in CM )",min_value=1,max_value=150,value=None)
            weight1 = st.number_input("Weight (in kg)", min_value=1,max_value=100,value=None)
            Age1 = st.number_input("Age for child (6-12)", min_value=6, max_value=None)
            if Height1 and weight1 and Age1:
                Fiber_needs=Age1+5
                st.write('You need approximately',Fiber_needs, 'gram of  Fiber today.')
                    
                # Calculate sufficiency based on the results from the nutritional needs calculation
        if protein_needs is not None:
            Protein_Sufficiency(st.session_state.total_protein_weight, protein_needs)
        if Fiber_needs is not None:
            Fiber_Sufficiency(st.session_state.total_fiber_weight, Fiber_needs)
    

if __name__ == '__main__':
    main()
    