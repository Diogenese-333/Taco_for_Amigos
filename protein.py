import  streamlit as st

def Protein():
    SEX = st.radio("What's your SEX",
     ['Female', 'Male'],)

    st.write("You selected",SEX)
    #weight = st.number_input("Weight")
    #x=weight*0.8


