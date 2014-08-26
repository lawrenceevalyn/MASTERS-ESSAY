## 26 August 2014

Realised that University of Illinois has some great digitized texts that I have access to despite their not appearing in UVic's catalogue; at book 147, started searching it, too. http://quest.library.illinois.edu/illinoisharvest/

## 21 August 2014

Really, I'm interested in how Radcliffe's rationalizing conclusions compare to her imitators. Are other explanations more plausible, more detailed? Less? How many forgo the explanation altogether?

Maybe I could read just the last chapters of a wide range of books, to see what kinds of explanations they offer. Or I think Tracy usually specifies if things are explained in the end?

## 17 August 2014

Started gathering less-concrete setting data in addition-- so, now 'Place' and 'Year' include all locations and centuries definitively indicated by Tracy; 'Area' is an adjective based on the 'feel' of the story and especially the characters' names; and 'Era' is either 'past' (potentially with some elaboration) or 'contemporary', based on the plot structure and especially the presence of noble castle-owners.

## 14 August 2014

JUST found out about the Oxford Text Archive (!!!) - knew I should have been doing more reading of other work to this point! But it looks like it's only going to have a very few texts, alas.

## 12 August 2014

Should have noted yesterday -- in fine Academic Spouse tradition, Ennis will be taking over the acquisition of OCR full texts, following the procedure described Aug 7 (minus acquisition of PDFs), for $1.50 per book. The relief from burnout is *incredible*. If things resolve satisfactorily for both, may hire zir to re-OCR from PDFs? But first will see what results can be extracted from the corpus as it exists.

## 7 August 2014

Just a note on how I'm sourcing books now-- I copy-paste the title from my spreadsheet into UVic's search system, and into a books.google.com search that only shows 'full view' results. I download the NCCO OCR (if it exists) and any PDF versions UVic provides that look like they're better scans than the Corvey microfilm. I make a note of all google editions, in case I want to rip them later. It goes pretty quickly!

So far it looks like accessibility skews firmly in favour of novels, and away from weird-man chapbooks.

## 4 August 2014

Realizing that google OCR is much, much better than NCCO, probably due to quality of PDFs? Definitely thinking that re-OCR-ing from pdfs is going to be my best bet. Not sure about copyright status of google books? Have to research whether I can extract PDFs (or, please, heaven, please!) txt files *without* breaking DRM.

It does look like, with NCCO Corvey as a back up, a lot more of these are available than I thought. I expect I'll have 150 to 200 in the end!

## 3 August 2014

Very annoyed to discover that #101, TALES OF TERROR, is in *verse*! **Verse!!** Not a novel at all! And this on top of, apparently, not really being written by Matthew Lewis.

Unsure how to proceed-- wish I could just strike through the text; maybe hide the row?

## 30 July 2014

Research ideas jotted on sticky notes in my room:
* Why is there so little cannibalism in the Gothic?
* Could find average chapter length of each book by skipping to the end, seeing what number the last chapter was, and dividing the page numbers by that
    - add no. of pages & no. of chapters to spreadsheet
* Can find all character names by extracting all capitalized words, discarding duplicates, manually discarding non-names.
    - What about two-word name combos? i.e., Lord O'Sinister. Just discard titles & work with, e.g., O'Sinister?

## 27 July 2014

Decided that, if full texts are available as pdfs from sources other than NCCO (i.e., if pdfs of halfway adequate quality are available), I should snag those and run my own ocr on them. Asked mum for ocr recommendations.

## 26 July 2014

Started tracking down full texts of Tracy's novels:
- If multiple e-texts are available, choose the one with the best OCR that still appears to follow the original text. Then manually delete any paratextual information that would not have been included in the original.
- Paratextual information that *was* in the original-- including running titles/chapter headings, indexes, notes, etc-- shall remain.

(Huh, it would be super interesting to algorithmically extract just the poems, quotes, and epigraphs in all these works... but probably easier to do it as a human.)

**Should I use my Gothic 'canon' as training texts to identify the topics?** Or will this make it impossible to identify when books diverge interestingly from that canon?

## 22 July 2014

Right now entering only setting information that is unambiguous, based on mentions of dates or places.

Most info is less certain, however. Perhaps add era categories of 'the past' and 'the present'? And place categories of 'Italian' when going based on names?

Decided to mark time periods based on the main tale, rather than the frame narrative, where such frames exist.

## 20 July 2014

Suggestions from mom:
- use ls* and redirect to filenames.text to get names for program to run
- if I can write the program so I say 'run program.py on file.txt' then I can write a shell script that can just call that program through every file (a shell script is just a file of shell commands-- )

## 15 July 2014

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