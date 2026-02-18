prompt = "\nPlease choose what type of topping you want on your pizza:"
prompt += "\nWhen you are done please enter 'quit': "

active = True

while active:
    message = input(prompt)

    if message == "quit":
        active = False
    else:
        print("I will add that topping.")
