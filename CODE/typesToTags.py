# this is a function that takes in gothicTypes.csv and outputs gothicTags.csv
# it creates a column for each word that appears in the Gothic Type column
# and for each row tallies the words that appear in that row's Gothic Type


# import libraries
import csv

# stuff to hold things in
allwordsdict = dict()

# find all the unique tags and put them in the dict allwords
with open('gothicTypes.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[5] == "Frank":
            pass # ignore the first row
        else:
            words = row[6].split() # gives me a list of strings
            for word in words:
                if word not in allwordsdict:
                    allwordsdict.update({word:1})
                    # it will all appear as {'Parody':1, 'Gothic':1, etc}


# convert allwords dict to list
allwords = list(allwordsdict.keys())
numwords = len(allwords)

print allwords # all the words ARE correct at this point
print numwords

#something after this point doesn't work

# make the output file with a column for Frank, then columns for each tag
outfile = open('gothicTags.csv', 'wb')
outcsv = csv.writer(outfile, quoting=csv.QUOTE_ALL)
outcsv.writerow(["gender"] + ["Frank"] + allwords)

# populate the tag columns
with open('gothicTypes.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[5] == "Frank":
            pass # ignore the first row
        else:
            FrankNo = row[5] # find the book's Frank number
            gender = row[1]
            outrow = [gender] + [FrankNo] + [None] + [None]*numwords
            words = row[6].split() # gives me a list of strings
            for word in words:
                cellnumber = allwords.index(word)
                outrow[cellnumber+2] = word
            outcsv.writerow(outrow)


# scan again to populate all the columns