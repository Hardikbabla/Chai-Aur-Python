chai_type = "Ginger chai"
customer_name = "kirat"
print(f"Order for {customer_name} : {chai_type} please !")

chai_description = "Aromatic and Bold"

print(f"First word: {chai_description[0:7]}") 
print(f"First word: {chai_description[0:8]}") 
print(f"First word: {chai_description[:8]}") 
print(f"First word: {chai_description[0:8:2]}") 
print(f"Last word: {chai_description[13:]}") 

print(f"Reversed word: {chai_description[::-1]}")

label_text = "ハルディク"
print(f"Non Encoded text : {label_text}")
encoded_text = label_text.encode("utf-8")
print(f"Encoded text : {encoded_text}")
decoded_text = encoded_text.decode("utf-8")
print(f"Decoded text : {decoded_text}")