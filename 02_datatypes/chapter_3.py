# Integer

tea_packets_in_stock = 100
tea_packets_sold = 25

remaining_packets = tea_packets_in_stock - tea_packets_sold
print(f"Remaining tea packets: {remaining_packets}")

new_stock = 40
updated_stock = remaining_packets + new_stock
print(f"Updated tea packet stock: {updated_stock}")


milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings
print(f"Milk per serving is {milk_per_serving}")


total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"While tea bags per pot : {bags_per_pot}")


total_cadamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cadamom_pods % pods_per_cup
print(f"Leftover Cardamom pods is {leftover_pods}")


base_flavor_strength = 2
scale_factor = 3
powerful_flavor = base_flavor_strength ** scale_factor
print(f"Scaled flavor strength is {powerful_flavor}")


total_tea_leaves_harvested = 1_000_00
print(f"Total tea leaves harvested : {total_tea_leaves_harvested}")