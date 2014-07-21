# -*- coding: utf-8 -*-
		# declare that this file uses Unicode literals (?)

import re
		# import regular expressions

book = open('bad01.txt').read()
		# read bad01.txt and hold it in memory as book

book = re.sub('- ', '', book)
		# delete hyphen-space combos
		# note that this one read book and executed changes in new_book
		# future substitutions work just with new_book to build on each other

book = re.sub('¬ ','', book)
		# delete ¬-space combos
		
book = re.sub('[^a-zA-Z\n\.]', ' ', book)
		# substitute a space for everything that isn't a letter, new line, or period

book = re.sub('vv', 'w', book)
		# change 'vv' to 'w'

open('fixed01.txt', 'w').write(book) 
		# write fixed01.txt with book