ingredients = ["water", "milk", "tea leaves"]
ingredients.append("sugar")
print(f"Ingredients are : {ingredients}")
ingredients.remove("water")
print(f"Ingredients are : {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"Chai Ingredients are : {chai_ingredients}")
chai_ingredients.insert(2, "black tea")
print(f"Chai Ingredients are : {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"{last_added}")
print(f"{chai_ingredients}")
chai_ingredients.reverse()
print(f"{chai_ingredients}")
chai_ingredients.sort()
print(f"{chai_ingredients}")

sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum Sugar level is : {max(sugar_levels)}")
print(f"Minimum Sugar level is : {min(sugar_levels)}")

base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]
full_liquid_mix = base_liquid + extra_flavor
print(f"Liquid Mix : {full_liquid_mix}")

strong_brew = ["black tea", "water"] * 3
print(f"Strong brew : {strong_brew}")

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes : {raw_spice_data}")