favorite_places = [
    {
        "Name" : "Linus" ,
        "Favorite place" : "Home" ,
        "Second favorite" : "The night club"
    },
    {
        "Name" : "Hannes" ,
        "Favorite place" : "Markitta" ,
        "Second favorite" : "Home" ,
        "Third favorite" : "The gym" ,
    },
    {
        "Name" : "Stefan" ,
        "Favorite place" : "Workshop"
    }
]

for person in favorite_places:
    print(person["Name"])

    for key, value in person.items():
        if key != "Name":
            print(f" - {key}: {value}")

    print()
