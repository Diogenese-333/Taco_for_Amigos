import streamlit as st
from calculate import *
from tacobar import taco_bar_calculator

def main():
    # รูปแบบแอป Streamlit
    st.title(":blue[Tacos For Amigos]")
    st.toast("Hola Amigo",icon="😃")
    # เลือกประเภทเนื้อ
    meat_type = st.selectbox("เลือกประเภทเนื้อของคุณ:", options=["ground beef", "shrimp", "hamburger", "chicken", "pork"])

    # เลือกtopping
    ingredients_option = ["cheddar cheese","monterey cheese","guacamole"]
    selected_ingredients = st.multiselect("เลือก TOPPING ",options=ingredients_option) 
        
    # เลือกผัก
    vegetable_options = ["lettuce", "onions", "beans", "refried beans", "tomatoes", "olives", "bell pepper"]
    selected_vegetables = st.multiselect("เลือกผักของคุณ:", options=vegetable_options)

    # เลือกซอส
    sauce_options = ["taco sauce", "hot sauce", "salsa", "guacamole sauce","sour cream"]
    selected_sauces = st.multiselect("เลือกซอสของคุณ:", options=sauce_options)

    # ปุ่มคำนวณ
    if st.button("คำนวณ"):
        results = taco_bar_calculator(meat_type, selected_vegetables, selected_sauces,selected_ingredients)

        # แสดงผลลัพธ์
        st.subheader("ผลลัพธ์")
        st.write(f"น้ำหนักรวมของทาโก้หนึ่งชิ้น: {results['total_weight']:.1f} g")
        st.write(f"ราคารวมสำหรับทาโก้หนึ่งชิ้น: ${results['total_price']:.2f}")
        st.write(f"น้ำหนักรวมของโปรตีนทั้งหมด: {results['total_protein_weight']:.2f} g")
        st.write(f"น้ำหนักรวมของไฟเบอร์ทั้งหมด: {results['total_fiber_weight']} g")
        tacos_protein = float(results['total_protein_weight'])
        tacos_fiber = float(results['total_fiber_weight'])
        #คำนวณ สารอาหาร
        SEX = st.radio("What's your SEX", ('Female', 'Male','Child'))
        st.write("You selected:", SEX)
        protein_needs= None
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
                if   protein_needs  is not None:
                    if  Activitylevel != 'Little/no exercise''Exercise often':
                        st.write('You need approximately', round(protein_needs, 2), 'grams of protein per day.')
                if Fiber_needs is not None:
                    if  Activitylevel != 'Little/no exercise''Exercise often':
                        st.write('You need approximately', round(Fiber_needs, 2), 'grams of fiber per day.')
                            
        if SEX == 'Child':
            Height1 = st.number_input ("Height (in CM )",min_value=1,max_value=150,value=None)
            weight1 = st.number_input("Weight (in kg)", min_value=1,max_value=100,value=None)
            Age1 = st.number_input("Age for child (6-12)", min_value=6, max_value=None)
            if Height1 and weight1 and Age1:
                Fiber_needs=Age1+5
                st.write('You need approximately',Fiber_needs, 'gram of  Fiber today.')

        Protein_Sufficiancy(tacos_protein,protein_needs)
        Fiber_Sufficiancy(tacos_fiber,Fiber_needs)
        
if __name__ == '__main__':
    main()