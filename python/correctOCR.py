import re
book = open('badOCR.txt').read()
new_book = re.sub('[^a-zA-Z\n\.]', ' ', book)
open('fixedOCR.txt', 'w').write(new_book)