prompt = "\nPlease choose what type of topping you want on your pizza:"
prompt += "\nWhen you are done please enter 'quit'."

while True:
    pizza = input(prompt)

    if pizza == "quit":
        break
    else:
        print(f"I will add that topping.")
        