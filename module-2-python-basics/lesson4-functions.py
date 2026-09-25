"""
Module 2 — Lesson 4: Functions
Student: Galvez, Mitchie
Date: September 26, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
A function in programming is like a small set of 
instructions that tells a computer how to do a specific task. 
You give the function some information, it performs the task, and it can give you a result. 
Functions can be used again and again, which makes programs easier to organize, understand, and maintain.
For example, you run a karinderya and you often need to calculate the total price of a meal based on:
The price of ingredients
The number of styro box needed  
A fixed tax rate
Instead of writing the calculation multiple times, you can create a function to do it.
============================================
KEY VOCABULARY
============================================
- Function – 
- Function Name –
- Parameter – 
- Argument – 
- Input -

============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

def calculate_total(ingredient_price, styro_boxes, tax_rate):
    styro_price = 5
    box_cost = styro_boxes * styro_price

    subtotal = ingredient_price + box_cost
    tax = subtotal * tax_rate
    total = subtotal + tax

    return total

ingredient_price = 100
styro_boxes = 2
tax_rate = 0.12

total_price = calculate_total(ingredient_price, styro_boxes, tax_rate)

print("Total price: ₱", total_price)

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
