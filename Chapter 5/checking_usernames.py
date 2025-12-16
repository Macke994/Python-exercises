current_users = [
    "admin",
    "alice",
    "bob",
    "charlie",
    "diana",
    "erik",
    "frank",
    "george",
    "helen",
    "ivan"
]

current_users_lower = [user.lower() for user in current_users]

new_users = ["Alice", "ADMIN", "jack", "karen", "Bob"]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Username '{new_user}' has already been used. Please enter a new username.")
    else:
        print(f"Username '{new_user}' is available.")
