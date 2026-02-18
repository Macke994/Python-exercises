prompt = "\nPlease choose what type of topping you want on your pizza:"
prompt += "\nWhen you are done please enter 'quit'."

message = ""
while message != "quit":
    message = input(prompt)

    if message != "quit":
        print("I will add that topping.")       