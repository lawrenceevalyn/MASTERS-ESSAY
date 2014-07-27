# -*- coding: utf-8 -*-
		# declare that this file uses Unicode literals (?)

import re
		# import regular expressions

book = open('bad01.txt').read()
		# read bad01.txt and hold it in the string book

book = re.sub('- ', '', book)
		# delete hyphen-space combos

book = re.sub('¬ ','', book)
		# delete ¬-space combos

book = re.sub('-\n','', book)
		# delete hyphen-newline combos
		
book = re.sub('\n',' ', book)
		# replace newlines with space
		
book = re.sub('[^a-zA-Z\.]', ' ', book)
		# substitute a space for everything that isn't a letter or period
		# (this means it would delete newlines)

book = re.sub('vv', 'w', book)
		# change 'vv' to 'w'
		
book = re.sub('Disclaimer: This file is generated from OCR (optical character recognition), which is a technology that converts images of text into text. While the technology is good at deciphering legible text, there are limitations and some text may not have been extracted correctly.','', book)
		# delete Corvey disclaimer text
		
open('fixed01.txt', 'w').write(book) 
		# write fixed01.txt with book