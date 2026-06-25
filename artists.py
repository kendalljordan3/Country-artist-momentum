artists = [
    {"name": "Megan Moroney", "streams": 2030000, "is_trending": True},
    {"name": "Zach Bryan", "streams": 8500000, "is_trending": True},
    {"name": "Morgan Wallen", "streams": 12000000, "is_trending": False},
    {"name": "Lainey Wilson", "streams": 5400000, "is_trending": True}
]

def get_trending(artists):
    for artist in artists:
        if artist["is_trending"] == True:
            print(artist["name"] + " is trending!")

get_trending(artists)