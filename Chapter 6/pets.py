pets = [
    {
        "Owner" : "Linus" ,
        "Pet" : "Cat" ,
        "Pet fact" : "Talks alot"
    },
    {
        "Owner" : "Sten" ,
        "Pet" : "Lizard" ,
        "Pet fact" : "Loves to sun" 
    },
    {
        "Owner" : "Siv" ,
        "Pet" : "Dog" ,
        "Pet fact" : "Is a bit silly"
    }
]

for pet in pets:
    print(f"{pet['Owner']} has a {pet['Pet']}.")
    print(f"Fun fact: {pet['Pet fact']}")
    print()  # blank line between pets
