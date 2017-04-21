# this is a function that takes in gothicTypes.csv and outputs gothicTags.csv
# it creates a column for each word that appears in the Gothic Type column
# and for each row tallies the words that appear in that row's Gothic Type


# import libraries
import csv

# stuff to hold things in
allwordsdict = dict() # using dicts first to collect unique types and words
alltypesdict = dict() # then they get made into lists
infileName = "gothicTypes.csv"
outfileName = "gothicTagsNew.csv"

# find all the unique types + tags and put them in dicts
with open(infileName, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[5] == "Frank": # if it's the first row (can check any row[#])
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

allwords.append("LASTWORD")
alltypes.append("LASTTYPE")

print "words found:"
print  numwords

print "types found:"
print numtypes

#something after this point doesn't work

# make the output file with rows for gender and Frank, then rows for each tag
outfile = open(outfileName, 'wb')
outcsv = csv.writer(outfile)

with open(outfileName, 'wb'):
    outcsv.writerow(["gender"] + ["Frank"] + allwords)
    # this actually writes all the columns!

# but adding this next section turns the first row into                  
# populate the tag rows
with open(infileName, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        FrankNo = row[5] # find the book's Frank number
        gender = row[1]
        with open(outfileName, 'wb'):
            outcsv.writerow([gender] + [FrankNo])

#        if row[5] == "Frank":
#            pass # ignore the first row
#        else:
#            rowWords = row[6].split() # gives me a list of strings
#            rowList = []
#            for word in allwords:
#                if word in rowWords:
#                    rowList.append(word)
#                else:
#                    rowList.append("")
#            with open(outfileName, 'wb'):
#                outcsv.writerow([gender] + [FrankNo] + rowList)


#            outrow = [gender] + [FrankNo] + [None]*numwords + ["made it to the end"]
            # this doesn't work; doesn't make enough rows
#            words = row[6].split() # gives me a list of strings
#            for word in words:
#                cellnumber = allwords.index(word)
#                outrow[cellnumber+2] = word
#            outcsv.writerow(outrow)