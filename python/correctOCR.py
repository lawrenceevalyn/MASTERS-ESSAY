import re
book = open('badOCR.txt').read()
new_book = re.sub('[^a-zA-Z0-9\n\.]', ' ', book)
open('fixedOCR.txt', 'w').write(new_book)