pizzas = ('margherita', 'salami', 'tex mex')
for pizza in pizzas:
    print(f"I enjoy {pizza.title()}, a lot\n")
print("I really do like pizza")

pizzas = ['margherita', 'salami', 'tex mex']

friend_pizzas = pizzas[:]  

pizzas.append('hawaiian')

friend_pizzas.append('bbq chicken')

print("Original pizzas list:", pizzas)
print("Friend's pizzas list:", friend_pizzas)
print("\nPrinting friend's pizzas individually:")

for pizza in friend_pizzas:
    print(f"I enjoy {pizza.title()}, a lot")
