# this is a function that takes in gothicTypes.csv and outputs gothicTags.csv
# it creates a column for each word that appears in the Gothic Type column
# and for each row tallies the words that appear in that row's Gothic Type


# import libraries
import collections # I think I need this so I can use a counter
import csv


# things to store stuff in
tagsCounter = collections.Counter() # a counter object hash table (?)
    # using this so I don't have to know the tags before I count them

# define the file-opener function
    # take in the gothicTypes.csv and look at the right column

# define the word-getter function
    # take in a string (Type)
    # for each string, split at spaces
    # output an array of strings


# define the type-column-counter function
    # take in a string (word) (and the name of the csv?)
    # if there is a column whose header matches that word,
        # put a 1 in that column for the row
    # else
        # create a column whose name is the word
        # put a 1 in that column for the row


# actually run the program to do the thing

# this prints all the Gothic Types
with open('testGothicTypes.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print row[6]

# for each row in the right column,
    # use word-getter function to split up the string, put words in an array
    # for each word in that array,
        # use the type-column-counter
# output the new csv