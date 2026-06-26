# Building a Chai Price Calculator
# =====================================================================
"""
A tea stall offers different prices for different cup sizes.
Write a program that calculates the price based on size.
Task:
    - Input: "small", "medium", "large"
    - Small -> ₹10, Medium -> ₹15, Large -> ₹20
    - if Invalid : show "Unknown cup size"
"""
# =====================================================================

cup = input("Choose Cup Size (small/medium/large) : ").lower()

if cup == "small":
    print("Price is ₹10")
elif cup == "medium":
    print("Price is ₹15")
elif cup == "large":
    print("Price is ₹20")
else:
    print("Unknown cup size")