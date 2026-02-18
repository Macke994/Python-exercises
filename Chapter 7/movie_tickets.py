prompt = "\nWhat is your age?"
prompt += "\nType 'quit' to end the program"

while True:
    age = input(prompt)

    if age.lower() == "quit":
        print("Goodbye!")
        break

    age = int(age)

    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15
    
    print(f"Your ticket price is ${price}.")
    