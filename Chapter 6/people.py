people = [
    {
        "first_name": "Linus",
        "last_name": "Hansson",
        "age": 27,
        "city": "Gällivare",
        "fun_fact": "can probably survive extreme cold like a Viking"
    },
    {
        "first_name": "Hannes",
        "last_name": "Landström",
        "age": 29,
        "city": "Gällivare",
        "fun_fact": "never skips leg day"
    },
    {
        "first_name": "Stefan",
        "last_name": "Hansson",
        "age": 54,
        "city": "Gällivare",
        "fun_fact": "makes dangerously good coffee"
    }
]

for person in people:
    print(
        f"{person['first_name']} {person['last_name']} "
        f"is {person['age']} years old, lives in {person['city']}, "
        f"and {person['fun_fact']}."
    )
