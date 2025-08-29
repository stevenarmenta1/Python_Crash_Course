def make_album(artistName, albumTitle, numSongs=None):
    """Returns dictionary of artist name and accompanying album title"""
    details = {'artist': artistName, 'album': albumTitle}
    if numSongs:
        details['number of songs'] = numSongs
    return details



while True: 
    print("\nTell me an artist and album and I will store it for you:")
    print("(Enter 'q' to quit at any time :)\n")

    artistName = input("Artist: ")
    if artistName == 'q':
        break

    albumTitle = input("Album title: ")
    if albumTitle == 'q':
        break
    
    pair = make_album(artistName, albumTitle)
    print(pair)
