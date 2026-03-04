def make_album(artist, title, songs=None):
    """Return information about an album"""
    album = {
        "artist": artist,
        "title": title
    }

    if songs is not None:
        album["songs"] = songs

    return album


album1 = make_album("Metallica", "Master of Puppets")
album2 = make_album("Adele", "25")
album3 = make_album("Drake", "Scorpion", 25)

print(album1)
print(album2)
print(album3)
