sandwich_orders = ["Tuna" , "Pastrami" , "Chicken" , "Pastrami" , "Ham" , "Salami" , "Pastrami"]
finished_sandwiches = []

print("Sorry, the deli has run out of pastrami \n")

while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")
    
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"Making sandwich: {current_sandwich.title()}")
    finished_sandwiches.append(current_sandwich)

print("\nI have made your sandwich")
for sandwich in finished_sandwiches:
    print(sandwich.title())
