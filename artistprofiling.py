import csv;
import math;
import operator;

'''VARIABLE DECLARATIONS'''

'''Text variables'''
text_list = []
lyrics_list =[]
text_lp_id = 3

'''Artist varibales'''
artist_list = []
artist_lp_id = 0

'''Song variables'''
song_list = []
song_lp_id = 1


'''Complete list of songs words'''
all_Songs = []
dictList = []
tfList = []
idfList = []
tfIdfFinal = []


'''FUNCTION DEFINITION'''

# This function takes in a list of dictionaries{word:wordCount} and a list of words
# It then determines the frequency of  a word in a dictionary (wordCount/ ttlWords)
# Creates a new dictionary list with key being word and value being Frequency of word


def computeTF(wordDict,docWords):
    tfDict = {}
    docCount = len(docWords)
    for word,count in wordDict.items():
        tfDict[word] = count/float(docCount)
    return tfDict


# This function take in a list of dictionary {word:wordCount} and determines inverse frequency across all songs
def computeIDF(songList):
    tfDictList = []
    listLen = len(songList)

    # For every song identify unique words
    for song in songList:
        idfDict = dict.fromkeys(song.keys(), 0)
        # Identify if the word occurs across  all song lyrics
        for lyrics in songList:
            for word, val in lyrics.items():
                # Conditional statement to ensure that word exists in present song evaluated
                if val>0 and word in idfDict:
                    idfDict[word] = idfDict[word] + 1

        for word,val in idfDict.items():
            # Apply the formula for idf
            idfDict[word] = math.log10(listLen/float(val))
        tfDictList.append(idfDict)
    return tfDictList


def computeTFIDF(tfDocWords,idfs):
    tfidf = {}
    for word,val in tfDocWords.items():
        tfidf[word] = val * idfs[word]
    return tfidf


''' <<<<<<<<<<<<<<<<<<< MAIN FUNCTION >>>>>>>>>>>>>>>>>> '''

# OPEN CSV FILE
with open('samplesongdata.csv','r') as csv_file:
    songs = csv.reader(csv_file,delimiter=',')
    # Skip the header of the csv
    next(songs,None)

    for row in songs:
        # NOTE A COMPLETE  LIST OF STOP WORDS MUST BE MADE RATHER THAN HAVING MULTIPLE REPLACE STATEMENTS
        # STOP WORDS LIST TO BE REFINED
        line = row[text_lp_id].replace('\n','')
        line = line.replace(',','')
        line = line.replace('?','')
        line = line.replace('[','')
        line = line.replace(']','')
        line = line.replace('(','')
        line = line.replace(')','')
        line = line.replace('\t','')
        # Consider changing all words to their  lowercase equivalent
        text_list.append(line)

        # Extract the artist and song title of of each song from the csv file
        artist_list.append(row[artist_lp_id])
        song_list.append(row[song_lp_id])

    # Parse each document in the text list by word
    for lyrics in text_list:
        lWords = lyrics.split()
        all_Songs.append(lWords)
    # Convert the list of words to a set of words to eliminate duplicates
    for lyricWords in all_Songs:
        lyricsSet = set(lyricWords)
        lyricsSet = sorted(lyricsSet)
        # Create a dictionary of unique words and their respective word count
        wordDict = dict.fromkeys(lyricsSet,0)

        # Iterative counter identifier for occurrences of a single word
        for word in lyricWords:
            wordDict[word]= wordDict[word] + 1
        # Append dictionary pairing(word,wordCount) to list
        dictList.append(wordDict.copy())
        wordDict.clear()

    # WARNING UTILIZING ZIP FOR ITERATING THROUGH LISTS SIMULTANEOUSLY IS NOT FEASIBLE FOR SCALABILITY

    # Determine the total frequency score of each dictionary pairing in the list
    for tupleList,wordsSong in zip(dictList,all_Songs):
        tempTF = computeTF(tupleList,wordsSong)

        tfList.append(tempTF)

    # Determine IDF across all songs of a given word
    idfList = computeIDF(dictList)

    # Determine final Results (tf-idf) for each song
    for idf,tf in zip(idfList,tfList):
        idfList.append(computeTFIDF(tf,idf))

    # VARIABLES FOR FORMATTING
    sortTfIdf = []
    top = 100

    # FORMAT SPECIFICATIONS

    for listing in idfList:
        orderedByTfIdf = dict()
        orderedByTfIdf = sorted(listing.items(), key=operator.itemgetter(1), reverse=True)[:top];
        sortTfIdf.append(orderedByTfIdf)

    # CREATION OF ARTIST PROFILE

    # Variables for formatting of artist profile
    artistSong = []
    artistProfile = []
    songTopWords = []
    # Create a list of artist and song names to act as a key
    for artist,name in zip(artist_list,song_list):
        artistSong.append(artist + '_' + name)

    # NOTE TO SELF CONSIDER EXTRACTING WORDS FROM SORTED TF-IDF LIST BY ROW
    # APPEND SOLELY THE WORDS TO NAME_SONG PAIRING IDEALLY AND EXCLUDE TF-IDF RANKING

    # Create a dictionary, artistSong acts as a unique key and value set to a list of songs
    artistProfile = zip(artistSong,sortTfIdf)

    for profile in artistProfile:
        print(profile)










