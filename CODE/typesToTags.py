# this is a function that takes in gothicTypes.csv and outputs gothicTags.csv
# it creates a column for each word that appears in the Gothic Type column
# and for each book/row tallies the words that appear in that book's Gothic Type

# also if it seems like this program isn't working, make sure you're opening the
# csv in a program that allows more than 255 columns. Numbers, for example,
# is not one of those programs.

# import libraries
import csv

# stuff to hold things in
allwordsdict = dict()    # using dicts first to collect unique types and words
alltypesdict = dict()    # then they get made into lists later
infileName = "gothicTypes.csv"
outfileName = "gothicTags.csv"

# find all the unique types and tags and put them in dicts
with open(infileName, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[5] == "Frank": # if it's the first row,    (can check any row[#])
            pass # ignore the first row
        else:
            if row[6] not in alltypesdict: # row[6] is the full Type as a string
                alltypesdict.update({row[6]:"here"})
            words = row[6].split() # breaks Type string into list of tag strings
            for word in words:
                if word not in allwordsdict:
                    allwordsdict.update({word:"here"})
                    # will appear as {'Parody':"here", 'Gothic':"here", etc}


# convert dicts to lists
alltypes = list(alltypesdict.keys())
numtypes = len(alltypes)

allwords = list(allwordsdict.keys())
numwords = len(allwords)

#allwords.append("LASTWORD")    # these can be useful for checking things
#alltypes.append("LASTTYPE")    # if everything is broken


# give some feedback so we know the program is running
#print alltypes
print "types found:"
print numtypes

#print allwords
print "words found:"
print  numwords 

# make the output file with columns for gender, Frank, and each tag
with open(outfileName, 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(["gender"] + ["Frank"] + allwords)
    # this actually writes all the columns!


# populate the tag rows
with open(infileName, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:     # for each book in the spreadsheet,
        # get the book's info
        FrankNo = row[5] # find the book's Frank number in the 6th column
        gender = row[1]  # and author gender in 5th column
        rowList = [] # initialize blank

        # list whether this book has each of the tags
        if row[5] == "Frank": # ignore the first row
            FrankNo = ""      # (by just making it blank)
            gender = "" 
        else:
            rowWords = row[6].split() # gives me a list of strings
            for word in allwords:
                if word in rowWords:
                    rowList.append(word)   # I don't care if Brian doesn't want
                else:                      # me to append this stuff to a list;
                    rowList.append("")     # this makes sense to me!!
        
        # append that book's new row!
        with open(outfileName, 'a') as f: # the secret was to open as 'a'!!!
            writer = csv.writer(f)
            writer.writerow([gender] + [FrankNo] + rowList) # ADDS THEM ALL!!!
            # this will also write the first row, with "Frank", but that's fine
            # because I made sure they'll be blank


# a vestigial way of populating columns with info:
#            words = row[6].split() # gives me a list of strings
#            for word in words:
#                cellnumber = allwords.index(word)
#                outrow[cellnumber+2] = word
#            outcsv.writerow(outrow)