import re
		#imports regular expressions
book = open('bad01.txt').read()
		#makes book open and read badOCR.txt. what is book? is it... a function?
# Need to insert something here that replaces "- " and "¬ " with nothing.
new_book = re.sub('[^a-zA-Z\n\.]', ' ', book)
		# makes new_book substitute nothingness for everything in book that isn't a letter
open('fixed01.txt', 'w').write(new_book) 
		# writes a new file with the results of new_book