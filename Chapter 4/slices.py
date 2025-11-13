pizzas = ('margherita', 'salami', 'tex mex', 'mexicana', 'cacciatore')
for pizza in pizzas:
    print(f"I enjoy {pizza.title()}, a lot\n")
print("I really do like pizza")

print(f"The first three items in the list are:")
print(pizzas[0:3])

print(f"Three items from the middle of the list are:")
print(pizzas[1:4])

print("The last three items in the list are:")
print(pizzas[-3:])
