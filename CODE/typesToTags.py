# take in a CSV with one column of info
# for each row in that column,
    # split the string at spaces, put the words in a list
    # for each word in that list,
        # if there is a column whose header matches that word,
            # put a 1 in that column for the row
        # else
            # create a column whose name is the word
            # put a 1 in that column for the row