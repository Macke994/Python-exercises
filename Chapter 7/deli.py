sandwich_orders = ["Tuna" , "Chicken" , "Ham" , "Salami"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"Making sandwich: {current_sandwich.title()}")
    finished_sandwiches.append(current_sandwich)

print("\nI have made your sandwich")
for sandwich in finished_sandwiches:
    print(sandwich.title())
