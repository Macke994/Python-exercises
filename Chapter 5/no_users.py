usernames = []  # all usernames removed

if not usernames:
    print("We need to find some users!")
else:
    for user in usernames:
        if user == "admin":
            print("Hello there admin, welcome back.")
        else:
            print(f"Hello {user}.")
