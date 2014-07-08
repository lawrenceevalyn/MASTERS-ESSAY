# Steps to be applied to all book files to ameliorate, as much as possible, the horrid OCR.

1. Delete disclaimer at top of each file.
    - "Disclaimer: This file is generated from OCR (optical character recognition), which is a technology that converts images of text into text. While the technology is good at deciphering legible text, there are limitations and some text may not have been extracted correctly."
2. Find "¬ " and replace with nothing.
3. Find "- " and replace with nothing.
4. For the digits 0 to 9, find "# " and replace with nothing.
5. For the digits 0 to 9, find "#" and replace with nothing.
6. For the following symbols, find and replace with nothing.
    - *
    - •
    - ■
    - ^
    - >
    - <
    - ~
    - %
    - \
    - /
7. Find "vv" and replace with "w".

# Steps to consider?
- Maybe remove the word "chapter"? And "vol"/"volume"?
- Maybe remove punctuation marks? Or put spaces in front of them, so if there are words affiliated with exclamation marks/ other interesting punctuation marks, that can count.
- *Is there a way to remove line breaks systematically?*
- Is there a way to remove roman numerals? (Probably not without ruining some words...)
- *Is there a way to just say 'remove everything that isn't a letter'?* If so, run it **after** steps 1 and 2, for which the removal of the space is important.
- Do I want to remove hyphens that don't have spaces after them? If so, probably replace with a space?