import  streamlit as st


SEX = st.radio(
     "SEX",
     ('Female', 'Male'))

st.write(f"You selected {SEX}")