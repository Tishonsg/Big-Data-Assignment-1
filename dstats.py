import csv;
from collections import Counter;

'''VARIABLE DECLARATIONS'''

'''Artist variables'''
artist_set = set()
artist_list = []
# Loop id to identify location of artist after each iteration
art_lp_id = 0;

'''Song varibales'''
song_list = []
song_set = set()
song_lp_id = 1;

'''Link variables'''
link_set = set()

'''Text variables'''
text_set = set()

'''FINAL RESULTS'''
numOfArtist = 0;
numOfSongs = 0;
avgNumOfSongs = 0;
avgNumOfWords = 0;


# OPEN CSV FILE
with open('songdata.csv','r') as csv_file:
    songs = csv.reader(csv_file,delimiter=',')
    # Row contains: artist, song, link and text

    for row in songs:
            # Extract artist entries into an array
            artist_list.append(row[art_lp_id])
            # Extract song entries into an array
            song_list.append(row[song_lp_id])

    # Utilize a set to eliminate duplicate entries
    for artist in artist_list:
        artist_set.add(artist)

    # Determining number of Artist
    # Assignment of number of Artist
    numOfArtist = len(artist_set)

    # Determining number of Songs
    # Assignment of number of Songs
    numOfSongs = len(song_list)

    # Determining the average number of songs per artist
    # Counter returns a key value pair of the number of occurences of duplicates in a list
    songsOfArtist = Counter(artist_list);
    avgNumOfSongs = (numOfSongs // numOfArtist)

    # Determining the average number of words per song





