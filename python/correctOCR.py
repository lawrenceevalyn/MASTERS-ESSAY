# -*- coding: utf-8 -*-
		# declare that this file uses Unicode literals (?)

import re
		# import regular expressions

book = open('bad01.txt').read()
		# make book open and read badOCR.txt. what is book? is it... a function?

new_book = re.sub('- ', '', book)
		# delete hyphen-space combos
		# note that this one read book and executed changes in new_book
		# future substitutions work just with new_book to build on each other

new_book = re.sub('¬ ','', new_book)
		# delete ¬-space combos
		
new_book = re.sub('[^a-zA-Z\n\.]', ' ', new_book)
		# substitute a space for everything that isn't a letter

new_book = re.sub('vv', 'w', new_book)
		# change 'vv' to 'w'

open('fixed01.txt', 'w').write(new_book) 
		# write fixed01.txt with the results of new_book