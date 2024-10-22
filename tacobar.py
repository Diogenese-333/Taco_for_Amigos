import streamlit as st

# Define the meat options and their prices
meat_per_taco = {
    "ground beef": (92.0, 3.5),  # เนื้อบด (กรัม, ราคาเป็นปอนด์)
    "shrimp": (60.0, 6.0),       # กุ้ง 100 = กุ้ง5ตัว
    "hamburger": (71.0, 4.0),    # เนื้อแฮมเบอร์เกอร์
    "chicken": (78.0, 3.0),      # ไก่
    "pork": (99.0, 5.0),         # หมู (Carnitas)
    "vegan meat": (110.0, 5.585),  # Plant-based meat for vegan
}

# Define other ingredients and their prices per taco
ingredients = {
    "cheddar cheese": (35.4, 2.5),  # (กรัม, ราคาเป็นปอนด์)
    "monterey cheese": (21.3, 3.0),
    "sour cream": (56.7, 1.5),
    "guacamole": (51.0, 4.0),
}

# Define vegetable prices per taco
vegetable_prices = {
    "lettuce": (36.9, 1.0),         # (กรัม, ราคาเป็นปอนด์)
    "onions": (25.5, 0.8),
    "beans": (31.2, 1.2),
    "refried beans": (62.4, 1.5),
    "tomatoes": (51.0, 1.0),
    "olives": (22.7, 2.0),
    "bell pepper": (56.7, 1.5)
}

# Define sauce prices per taco
sauce_prices = {
    "taco sauce": (30.0, 2.0),     # (กรัม, ราคาเป็นปอนด์)
    "hot sauce": (15.0, 2.5),
    "salsa": (25.0, 3.0),
    "guacamole sauce": (20.0, 4.0),
    "sour cream": (56.7, 1.5),
}

# อัตราแลกเปลี่ยน 1 ปอนด์ = 40 บาท
exchange_rate = 40

def calculate_meat_price(meat_type):
    if meat_type not in meat_per_taco:
        return 0
    meat_weight, meat_price_per_lb = meat_per_taco[meat_type]
    # คำนวณราคาต่อกรัม
    meat_price_per_gram = (meat_price_per_lb / 453.592) * exchange_rate
    return meat_weight * meat_price_per_gram

def calculate_ingredient_price(selected_ingredients):
    total_price = 0
    for ingredient in selected_ingredients:
        if ingredient in ingredients:
            weight, price_per_lb = ingredients[ingredient]
            # คำนวณราคาต่อกรัม
            price_per_gram = (price_per_lb / 453.592) * exchange_rate
            total_price += weight * price_per_gram
    return total_price

def calculate_vegetable_price(selected_vegetables):
    total_price = 0
    for vegetable in selected_vegetables:
        if vegetable in vegetable_prices:
            weight, price_per_lb = vegetable_prices[vegetable]
            # คำนวณราคาต่อกรัม
            price_per_gram = (price_per_lb / 453.592) * exchange_rate
            total_price += weight * price_per_gram
    return total_price

def calculate_sauce_price(selected_sauces):
    total_price = 0
    for sauce in selected_sauces:
        if sauce in sauce_prices:
            weight, price_per_lb = sauce_prices[sauce]
            # คำนวณราคาต่อกรัม
            price_per_gram = (price_per_lb / 453.592) * exchange_rate
            total_price += weight * price_per_gram
    return total_price

def calculate_total_weight(meat_type, selected_ingredients, selected_vegetables, selected_sauces):
    total_weight = 0
    if meat_type in meat_per_taco:
        total_weight += meat_per_taco[meat_type][0]
    for ingredient in selected_ingredients:
        if ingredient in ingredients:
            total_weight += ingredients[ingredient][0]
    for vegetable in selected_vegetables:
        if vegetable in vegetable_prices:
            total_weight += vegetable_prices[vegetable][0]
    for sauce in selected_sauces:
        if sauce in sauce_prices:
            total_weight += sauce_prices[sauce][0]
    return total_weight

def calculate_total_protein_weight(meat_type, selected_ingredients):
    total_protein_weight = 0
    if meat_type in meat_per_taco:
        total_protein_weight += meat_per_taco[meat_type][0]
    for ingredient in selected_ingredients:
        if ingredient in ingredients:
            total_protein_weight += ingredients[ingredient][0]
    return total_protein_weight

def calculate_total_fiber_weight(selected_vegetables):
    total_fiber_weight = 0
    for vegetable in selected_vegetables:
        if vegetable in vegetable_prices:
            total_fiber_weight += vegetable_prices[vegetable][0]
    return total_fiber_weight




    
   