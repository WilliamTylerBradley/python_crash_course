def make_album(artist, album, number_of_songs=None):
    if number_of_songs:
        return {'artist':artist, 'album':album, 'number_of_songs':number_of_songs}
    else:
        return {'artist':artist, 'album':album}
    
a1 = make_album('Taylor Swift', '1984')
print(a1)
a1 = make_album('Beyonce', 'Renaissance', 16)
print(a1)
a1 = make_album('Beyonce', 'Lemonade')
print(a1)