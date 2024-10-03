import streamlit as st

def taco_bar_calculator(meat_type, selected_vegetables, selected_sauces):
    # ส่วนผสมที่ต้องการต่อทาโก้ (กรัม) และราคาต่อหน่วย
    meat_per_taco = {
        "ground beef": (92.0, 3.5),  # เนื้อบด (กรัม, ราคาเป็นปอนด์)
        "shrimp": (92.0, 6.0),       # กุ้ง
        "hamburger": (71.0, 4.0),    # เนื้อแฮมเบอร์เกอร์
        "chicken": (78.0, 3.0),      # ไก่
        "pork": (99.0, 5.0)          # หมู (Carnitas)
    }

    # ตรวจสอบประเภทเนื้อ
    if meat_type not in meat_per_taco:
        return "ประเภทเนื้อไม่ถูกต้อง กรุณาเลือกจาก: ground beef, shrimp, hamburger, chicken, pork"

    # คำนวณน้ำหนักรวมและราคา
    meat_weight, meat_price_per_lb = meat_per_taco[meat_type]
    
    # กำหนดส่วนผสมอื่น ๆ และราคาของพวกเขาต่อทาโก้
    ingredients = {
        "cheddar cheese": (35.4, 2.5),  # (กรัม, ราคาเป็นปอนด์)
        "monterey cheese": (21.3, 3.0),
        "sour cream": (56.7, 1.5),
        "guacamole": (51.0, 4.0),
        
    }

    # กำหนดราคาผักต่อทาโก้
    vegetable_prices = {
        "lettuce": (36.9, 1.0),         # (กรัม, ราคาเป็นปอนด์)
        "onions": (25.5, 0.8),
        "beans": (31.2, 1.2),
        "refried beans": (62.4, 1.5),
        "tomatoes": (51.0, 1.0),
        "olives": (22.7, 2.0),
        "bell pepper": (56.7, 1.5)
    }

    # กำหนดซอสและราคาต่อทาโก้
    sauce_prices = {
        "taco sauce": (30.0, 2.0),     # (กรัม, ราคาเป็นปอนด์)
        "hot sauce": (15.0, 2.5),
        "salsa": (25.0, 3.0),
        "guacamole sauce": (20.0, 4.0),
        "sour cream": (56.7, 1.5),
    }

    # คำนวณราคาสำหรับส่วนผสมอื่น ๆ
    total_price = meat_price_per_lb * (meat_weight / 453.592)  # แปลงกรัมเป็นปอนด์สำหรับเนื้อ
    ingredient_prices = {}

    for ingredient, (weight, price_per_lb) in ingredients.items():
        ingredient_price = price_per_lb * (weight / 453.592)  # แปลงกรัมเป็นปอนด์สำหรับส่วนผสมอื่น ๆ
        ingredient_prices[ingredient] = ingredient_price
        total_price += ingredient_price

    # คำนวณราคาสำหรับผัก
    vegetable_price = price_per_lb * (weight / 453.592) 
    vegetable_prices_total = {}
    
    for vegetable in selected_vegetables:
        if vegetable in vegetable_prices:
            weight, price_per_lb = vegetable_prices[vegetable]
            vegetable_price = price_per_lb * (weight / 453.592)  # แปลงกรัมเป็นปอนด์สำหรับผัก
            vegetable_prices_total[vegetable] = vegetable_price
            total_price += vegetable_price

    # คำนวณราคาสำหรับซอส
    sauce_prices_total = {}
    
    for sauce in selected_sauces:
        if sauce in sauce_prices:
            weight, price_per_lb = sauce_prices[sauce]
            sauce_price = price_per_lb * (weight / 453.592)  # แปลงกรัมเป็นปอนด์สำหรับซอส
            sauce_prices_total[sauce] = sauce_price
            total_price += sauce_price

    return {
        'total_weight': sum([meat_weight] + [vegetable_prices[v][0] for v in selected_vegetables]) + sum([sauce_prices[s][0] for s in selected_sauces]),
        'total_price': total_price,
        'price_per_taco': total_price   # เนื่องจากเราคำนวณสำหรับหนึ่งทาโก้
    }

# รูปแบบแอป Streamlit
st.title("Tacos For Amigos")

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
    results = taco_bar_calculator(meat_type, selected_vegetables, selected_sauces)

    # แสดงผลลัพธ์
    st.subheader("ผลลัพธ์")
    st.write(f"น้ำหนักรวมของทาโก้หนึ่งชิ้น: {results['total_weight']:.1f} g")
    st.write(f"ราคารวมสำหรับทาโก้หนึ่งชิ้น: ${results['total_price']:.2f}")