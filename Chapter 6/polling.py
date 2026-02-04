favorite_languages = {
    "jen" : "python" ,
    "sarah" : "c" ,
    "edward" : "rust" ,
    "phil" : "python" ,
    }

people = [
    "jen",
    "sarah",
    "edward",
    "phil",
    "linus",
    "stefan",
    "hannes",
    ]

  
for name in people:
    if name in favorite_languages:
        print(f"Thank you, {name.title()}, for taking the poll!")
    else:
        print(f"{name.title()}, please take our language poll!")