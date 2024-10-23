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
    