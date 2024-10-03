import streamlit as st
def protein():
    st.title("Protein calculater");
    SEX=st.radio("What is your gender?",('Female','Male'))
    st.write(f"Thankyou{SEX}")