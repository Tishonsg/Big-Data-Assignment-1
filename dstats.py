import csv;
import matplotlib.pyplot as plt;
import operator;
from collections import Counter;
from collections import OrderedDict;


'''VARIABLE DECLARATIONS'''

'''Artist variables'''
artist_set = set()
artist_list = []
# Loop id to identify location of artist after each iteration
art_lp_id = 0;

'''Song variables'''
song_list = []
song_set = set()
song_lp_id = 1;

'''Link variables'''
link_set = set()

'''Text variables'''
text_list = []
text_set = set()
text_lp_id = 3;


'''FINAL RESULTS'''
numOfArtist = 0;
numOfSongs = 0;
avgNumOfSongs = 0;
avgNumOfWords = 0;
pairsOfArtistAvgNumOfWords = {};


'''FUNCTION DECLARATIONS'''


# Return the number of unique words per song in array list
def unique_words(listOfSongs):
    # Variables
    uniqueWordSet = set();  # Unique words with in a single song
    numOfWords = 0;         # Numerical value of unique words in a song
    wordsPerSong = [];      # Number of words per song

    for songLyrics in listOfSongs:
        for words in songLyrics.split():
            uniqueWordSet.add(words)
        numOfWords = len(uniqueWordSet)
        uniqueWordSet.clear()
        wordsPerSong.append(numOfWords)

    print(wordsPerSong)
    return wordsPerSong


''' <<<<<<<<<<<<<<<<<<< MAIN FUNCTION >>>>>>>>>>>>>>>>>> '''

# OPEN CSV FILE
with open('songdata.csv','r') as csv_file:
    songs = csv.reader(csv_file,delimiter=',')

    # Skip the header of the csv
    next(songs, None)

    # Row contains: artist, song, link and text
    for row in songs:

        # Extract artist entries into an array
        artist_list.append(row[art_lp_id])
        # Extract song entries into an array
        song_list.append(row[song_lp_id])
        # Extract song lyrics
        text_list.append(row[text_lp_id])

    # Utilize a set to eliminate duplicate entries(artist)
    for artist in artist_list:
        artist_set.add(artist)
    artist_set = sorted(artist_set)


    # Determining number of Artist
    # Assignment of number of Artist
    numOfArtist = len(artist_set)



    # Determining number of Songs
    # Assignment of number of Songs
    numOfSongs = len(song_list)


    # Determining the average number of songs per artist
    # Counter returns a key value pair of the number of occurrences of duplicates in a list
    songsOfArtist = Counter(artist_list);
    avgNumOfSongs = (numOfSongs // numOfArtist)

    # Determining the average number of words per song

    ttlNumOfWords = 0;
    # For each collection of song lyrics loop through each word and append to a set to eliminate duplicates
    # Keep a 'static' variable to count words in the set, and after the completion of a song read clear set and repeat
    for lyrics in text_list:
        for word in lyrics.split():
            text_set.add(word)
        ttlNumOfWords = ttlNumOfWords + len(text_set)
        text_set.clear()
    # Assignment of average number of unique words per song
    avgNumOfWords = (ttlNumOfWords // numOfSongs)

    # Determining the average number of unique words per song of an artist (arranged in ascending order of artist)

    # Required Variables
    songsPerArtist = []         # List of songs produced by an artist/band
    wordsPerSongPerArtist = []  # List of words per each song produced by an artist
    artistAvgWords = {}         # Dictionary of artist and the average number of words in their respective songs
    allArtistWords = 0          # Total number of of words in across all songs produced by an artist
    avgWordCount = 0;

    for artist in artist_set:
        print(artist)
        csv_file.seek(0)
        for record in songs:
            if record[art_lp_id] == artist:
                # Create a list of the lyrics of all songs produced by a unique artist
                songsPerArtist.append(record[text_lp_id])
        # Receive an array of the number of unique words in each song produced by an artist
        wordsPerSongPerArtist = unique_words(songsPerArtist)

        # Sum total number of words across all songs produced by an artist
        for wordCount in wordsPerSongPerArtist:
            allArtistWords = allArtistWords + int(wordCount)

        # Determine average word count of a song produced by a artist
        if allArtistWords > 0 and len(songsPerArtist) > 0:
            avgWordCount = (allArtistWords //len(songsPerArtist))
            # Append artist and average word count as tuple to dictionary
            artistAvgWords.update({artist:avgWordCount})

            # Reset variables to default state before iterating on next artist
            songsPerArtist.clear()
            allArtistWords = 0

    # Sorting artistWord by Key
    pairsOfArtistAvgNumOfWords = OrderedDict(sorted(artistAvgWords.items()))

    # Graph Creation
    # Plotting a table utilizing the math library library
    # Where the x-axis represents the artists and the y-axis represents the average number of words.

    '''BAR CHART VARIABLES'''
    top = 10;  # number of permitted table entries in the bar graph
    # Sort pairsOfArtistAvgNumOfWords on the value in descending order(desc -> (reverse=True))
    orderedByValue = dict()
    orderedByValue = sorted(pairsOfArtistAvgNumOfWords.items(), key=operator.itemgetter(1),reverse=True)[:top];

    # x-coordinates(artist)
    topAxis_x = []
    for key in orderedByValue:
       topAxis_x.append(key[0])

    # y-coordinates  (average number of words)
    topAxis_y = []
    for value in orderedByValue:
        topAxis_y.append(value[1])

    # BAR CHART ATTRIBUTE SPECIFICATIONS

    # Labels for bars
    tick_label = topAxis_x
    # Plotting a bar chart
    plt.bar(topAxis_x, topAxis_y, width=0.5, color='green')
    # naming the x-axis
    plt.xlabel('Artist or Band')
    # naming the y-axis
    plt.ylabel('Average Number of Words')
    # plot title
    plt.title('Billboard Top 10')
    # function to show the plot
    plt.show()




