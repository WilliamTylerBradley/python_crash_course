def make_album(artist, album, number_of_songs=None):
    if number_of_songs:
        return {'artist':artist, 'album':album, 'number_of_songs':number_of_songs}
    else:
        return {'artist':artist, 'album':album}
    
while True:
    artist = input('What is the artist\'s name? ')
    if artist == 'quit':
        break

    title = input('What is the album title? ')
    if title == 'quit':
        break

    album = make_album(artist, title)
    print(album)
    print('')