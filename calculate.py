#protein 0.8 per weight
#fibers 25-30 per day
#โปรแกรมหลิว คำนวณโปรตีนทั้งหมดที่ร่างกายต้องการต่อวัน fiber_need , protein_need
#โปรแกรมของกวางคำนวณว่าในทาโก้หนึ่งชิ้นมีปริมาณโปรตีนอยู่เท่าไหร่ tacos_fiber , tacos_protein
import streamlit as st
from fiber import Fiber
from tacobar import *
def Protein_Sufficiancy(tacos_protein , protein_need):
    if tacos_protein > protein_need:
        st.write(f"You overeat MEAT , you need more Fiber") 
    elif protein_need < tacos_protein:
        recommend_protein = protein_need - tacos_protein
        st.write(f"You need more {recommend_protein} grams of protein") 
    else:
        st.write("Bon' Appettito!!!")

def Fiber_Sufficiancy(tacos_fiber , fiber_need):
    if tacos_fiber > fiber_need:
        st.write(f"You overeat Veggies , you need more MEAT") 
    elif tacos_fiber < fiber_need:
        recommend_fiber = fiber_need - tacos_fiber
        st.write(f"You need more {recommend_fiber} grams of protein") 
    else:
        st.write("Bon' Appettito!!!")