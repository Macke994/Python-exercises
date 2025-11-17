# 1. Animals
canines = ("wolf", "coyote", "golden jackal")

for canine in canines:
    print(f"A {canine.title()} would not be a good pet")

print("These are wild and possibly untameable animals\n")


# 2. Odd numbers 
odd_numbers = list(range(1, 21, 2))
print("Odd numbers from 1 to 20:")
print(odd_numbers, "\n")


# 3. Slices
pizzas = ("margherita", "salami", "tex mex", "mexicana", "cacciatore")

for pizza in pizzas:
    print(f"I enjoy {pizza.title()}, a lot")

print("I really do like pizza\n")

print("The first three items in the list are:")
print(pizzas[:3])

print("Three items from the middle of the list are:")
print(pizzas[1:4])

print("The last three items in the list are:")
print(pizzas[-3:])
