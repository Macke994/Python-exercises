pizzas = ('margherita', 'salami', 'tex mex', 'mexicana', 'cacciatore')

for pizza in pizzas:
    print(f"I enjoy {pizza.title()}, a lot\n")
print("I really do like pizza")

print("The first three items in the list are:")
for pizza in pizzas[:3]:
    print(pizza)

print("\nThree items from the middle of the list are:")
for pizza in pizzas[1:4]:
    print(pizza)

print("\nThe last three items in the list are:")
for pizza in pizzas[-3:]:
    print(pizza)
