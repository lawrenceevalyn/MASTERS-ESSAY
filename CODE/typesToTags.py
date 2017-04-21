# this is a function that takes in gothicTypes.csv and outputs gothicTags.csv
# it creates a column for each word that appears in the Gothic Type column
# and for each row tallies the words that appear in that row's Gothic Type


# import libraries
import csv
from shutil import copyfile


# things to store stuff in


# get all the columns of the csv as a list of lists
f = csv.reader(open('testGothicTypes.csv'))
column_tuples = zip(*f) # gets a list of tuples
    # http://ask.metafilter.com/142871/Columnoriented-CSV-in-Python
    # can determine number of columns with len(columns)
    # can get a tuple of all gothic types with columns[6]

columns = [list(elem) for elem in column_tuples] # converts to list of lists
    # http://stackoverflow.com/questions/14831830/convert-a-list-of-tuples-to-a-list-of-lists


# this function will make sure there is a column for each tag,
# and tally the use of that tag in the rows
def tagcounter(tag): # takes in a string
#    if tag == "Type":
#        print "skipping the tag 'Type'"
#    else:
        print "now running " + tag + " through the tagcounter:"
        # if there is a column whose header matches the tag,
        # add the tag to the end of the column
        for column in columns:
            if column[0] == tag: # is the problem here?????
                print tag + " matches " + column[0]
                column.append(tag)
                print "now the column is:"
                print column
        # in all the other columns, add a blank space
            else:
                print tag + " doesn't match " + column[0]
                column.append('')
        # if the tag didn't find a column, make one
        # create a column whose name is the word
        # put a 1 in that column for the row


# actually run the program to do the thing
for type in columns[6]: # for each string in the "Types" list
    print type
    tags = type.split() # split the string at spaces to make the tags
    print tags
    for tag in tags:
        print tag
        tagcounter(tag)


# output the new csv
#    copyfile('testGothicTypes.csv', 'testGothicTags.csv')
#    with open('testGothicTags.csv', 'rt') as f:
#        writer = csv.writer(f)
#        for row in writer: