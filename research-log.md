## 30 July 2015

Research ideas jotted on sticky notes in my room:
* Why is there so little cannibalism in the Gothic?
* Could find average chapter length of each book by skipping to the end, seeing what number the last chapter was, and dividing the page numbers by that
    - add no. of pages & no. of chapters to spreadsheet
* Can find all character names by extracting all capitalized words, discarding duplicates, manually discarding non-names.
    - What about two-word name combos? i.e., Lord O'Sinister. Just discard titles & work with, e.g., O'Sinister?

## 27 July 2015

Decided that, if full texts are available as pdfs from sources other than NCCO (i.e., if pdfs of halfway adequate quality are available), I should snag those and run my own ocr on them. Asked mum for ocr recommendations.

## 26 July 2015

Started tracking down full texts of Tracy's novels:
- If multiple e-texts are available, choose the one with the best OCR that still appears to follow the original text. Then manually delete any paratextual information that would not have been included in the original.
- Paratextual information that *was* in the original-- including running titles/chapter headings, indexes, notes, etc-- shall remain.

(Huh, it would be super interesting to algorithmically extract just the poems, quotes, and epigraphs in all these works... but probably easier to do it as a human.)

**Should I use my Gothic 'canon' as training texts to identify the topics?** Or will this make it impossible to identify when books diverge interestingly from that canon?

## 22 July 2015

Right now entering only setting information that is unambiguous, based on mentions of dates or places.

Most info is less certain, however. Perhaps add era categories of 'the past' and 'the present'? And place categories of 'Italian' when going based on names?

Decided to mark time periods based on the main tale, rather than the frame narrative, where such frames exist.

## 20 July 2015

Suggestions from mom:
- use ls* and redirect to filenames.text to get names for program to run
- if I can write the program so I say 'run program.py on file.txt' then I can write a shell script that can just call that program through every file (a shell script is just a file of shell commands-- )

## 15 July 2015

Starting poking around with topic modeling.
- model-2 is now 100 topics, 15 topic words, 600 iterations.
- model-3 is now 50 topics, 15 topic words, 600 iterations.
- model-4 is now 15 topics, 15 topic words, 600 iterations.

Tried to make network maps of any of these with Gephi, had no idea what I was doing, accumulated more readings to-do.

## 10 July 2014
correctOCR.py now executes all seven cleanup steps listed below. To-do list updated with next goal: scale program to multiple files.

Right now multi-volume works have a txt file per volume. Is that what I want? If not, it's probably not worth writing a program to merge them, can just do it with Automator.

## 7 July 2014
### Experimenting with cleaning OCR of full texts
Tried these out manually, started poking with python to do it.

#### Steps to be applied to all book files to ameliorate, as much as possible, the horrid OCR.

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

#### Steps to consider?
- Maybe remove the word "chapter"? And "vol"/"volume"?
- Maybe remove punctuation marks? Or put spaces in front of them, so if there are words affiliated with exclamation marks/ other interesting punctuation marks, that can count.
- *Is there a way to remove line breaks systematically?*
- Is there a way to remove roman numerals? (Probably not without ruining some words...)
- *Is there a way to just say 'remove everything that isn't a letter'?* If so, run it **after** steps 1 and 2, for which the removal of the space is important.
- Do I want to remove hyphens that don't have spaces after them? If so, probably replace with a space?

## 29 June 2014
FULL TEXTS! FULL TEXTS!! FULL TEXTS!!!
This changes everything! Eventually. The OCR is... horrid.
So, the plan is still to read up on topic modelling while running tests on the plot summaries, and *then* forming a plan regarding which full texts (and how many) to clean up. (Prooobably time to check in with Dr. Miles, too.)

## 24 June 2014
Running it with exactly two topics is *extremely* exciting at first glance, usually dividing them immediately into "mother" and "father" topics. Slightly perplexing that this is not universal, though, and that the rest of the topics are often a bit mystifying.
* model-1 is two topics, 20 words per topic, 500 iterations