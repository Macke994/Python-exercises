def make_album(artist, title, songs=None):
    """Return information about an album"""
    album = {
        "artist": artist,
        "title": title
    }

    if songs is not None:
        album["songs"] = songs

    return album


print("Enter album information.")
print("Type 'quit' at any time to stop.\n")

while True:
    artist = input("Artist name: ")
    if artist.lower() == "quit":
        break

    title = input("Album title: ")
    if title.lower() == "quit":
        break

    album = make_album(artist, title)
    print("Album created:", album)
    print()
