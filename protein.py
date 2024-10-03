import  streamlit as st

def Protein():
    SEX = st.radio(
     "SEX",
     ('Female', 'Male'))

    st.write(f"You selected {SEX}")
    weight = st.number_input("Weight")
    x=weight*0.8

