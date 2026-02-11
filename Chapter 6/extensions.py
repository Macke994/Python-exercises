aliens = [
    {"type": "normal", "color": "green",  "points": 5},
    {"type": "normal", "color": "yellow", "points": 10},
    {"type": "normal", "color": "red",    "points": 15},
    {"type": "boss",   "color": "purple", "points": 100}
]

for alien in aliens:
    if alien["type"] == "boss":
        print(f"🔥 Boss defeated! +{alien['points']} points!")
    else:
        print(f"Alien defeated! +{alien['points']} points.")
        #added a little bit of flair to the first example of the chapter