# Topicing Models
Following the principle that one doesn't understand anything one can't teach to another, I am going to explain topic modelling to myself until I know what the hell I'm doing.
Warning: I'll be blatantly copy-pasting without attribution to piece these ideas together. Internal use only. 

## My Big Explanation

### What Do?

#### Don't Know Categories

In the beginning, there is a corpus. You don't know anything about the categories/topics it contains.

Perhaps you make a vector-space model of this corpus. If so, you describe the vector space with a matrix.

The simplest vector-space model assigns each word a weight based on its term frequency (tf) in each document. Or, there are a lot of more complicated formulae to weight words, including probabilistic methods and tf*idf.

This vector-space model is then presented in a matrix with a column for each word and a row for each document. At the intersection of each word and document is the word's weight for that document. In this matrix, each document (row) is an N-dimensional vector, with N equal to the number of words (columns). The matrix itself only has two dimensions (rows and columns) but nonetheless describes an N-dimensional vector space.

N is too many dimensions, so you use algorithms to merge similar dimensions/columns. LSA, LSI, SVD, and PCA are all different algorithms that use linear algebra to collapse columns together.

Once you've collapsed several words/columns together, your new columns are mathematical constructs that share some similarities with categories. You don't know anything.

To find out what the categories are, what you want to do to discover categories is called "Clustering" or, to AI folks "Unsupervised Learning".  Basically, the raw vectors are compared to each other using some similarity metric (in vector space:  cosine similarity metric; in probability model, some probabilistic similarity metric). You group the most similar documents into clumps using one of many, many clustering algorithms (k-means is most popular).  These groups/clusters are now your categories.

Topics are not defined by the words; the topics/concepts/classes/categories are abstract ideas. They are represented by words.

#### Do Know Categories

In the beginning, there is a corpus, and an ontology. Your corpus documents belong to X number of ontology categories. You know what all these categories are, but don't know where they are in which documents. You need to instantiate your categories, by filling them up with words.

Perhaps you make a vector-space model of this corpus. If so, you describe the vector space with a matrix. This is still the same as if you didn't know the categories.

N is still too many dimensions. You want to reduce N to the X, number of predefined known categories. A human reads a small number of documents and categorizes them. An algorithm, such as SVM or (preferably) KNN, uses these sample documents to learn how to tell the categories apart. Then you can use it to categorize the rest of the documents.

Now you know how much of each document comes from each category. Your categories are more useful than the categories generated via method 1, because you picked them out yourself.

### Topic Modeling and Networks

####Inferring topic models from networks.
* McCallum et al. (2005). Author-Recipient-Topic (ART) Model. In ART, it is assumed that topics of letters, e-mails or direct messages between people can be inferred from knowledge of both the author and the recipient. Thus, ART takes into account the social structure of a communication network in order to generate topics.
* Dietz et al. (2007) created a model that looks at citation networks, where documents are generated by topical innovation and topical inheritance via citations.
* Nallapati et al. (2008) similarly creates a model that finds topical similarity in citing and cited documents, with the added ability of being able to predict citations that are not present.
* Blei himself joined the fray in 2009, creating the Relational Topic Model (RTM) with Jonathan Chang, which itself could summarize a network of documents, predict links between them, and predict words within them.
* Wang et al. (2011) created a model that allows for “the joint analysis of text and links between [people] in a time-evolving social network.” Their model is able to handle situations where links exist even when there is no similarity between the associated texts.

####Inferring networks from topic models.
(Using networks to visualize how documents or topics relate to one another)

Some models have been made that infer networks from non-networked text.
* Broniatowski and Magee (2010 & 2011) extended the Author-Topic Model, building a model that would infer social networks from meeting transcripts. They later added temporal information, which allowed them to infer status hierarchies and individual influence within those social networks.

Many times, however, rather than creating new models, researchers create networks out of topic models that have already been run over a set of data. Using networks, we can see how documents relate to one another, how they relate to topics, how topics are related to each other, and how all of those are related to words.
* Newton’s Chymistry project
* Elijah Meeks created a wonderful example combining topic models with networks in [Comprehending the Digital Humanities](https://dhs.stanford.edu/comprehending-the-digital-humanities/). Using fifty texts that discuss humanities computing, Elijah created a topic model of those documents and used networks to show how documents, topics, and words interacted with one another within the context of the digital humanities.
* [TopicNets](http://www.ics.uci.edu/~asuncion/pubs/TIST_11.pdf), a project that combines topic modeling and network analysis in order to create an intuitive and informative navigation interface for documents and topics. This is a great example of an interface that turns topic modeling into a useful scholarly tool, even for those who know little-to-nothing about networks or topic models.

Having a network with every document connected to every other document is scarcely useful, so generally we’ll make our decision such that each document is linked to only a handful of others. This allows for easier visualization and analysis, but it also destroys much of the rich data that went into the topic model to begin with. This information can be more fully preserved using other techniques, such as multidimensional scaling.

## What Have Other People Done?

[Topic Modeling Martha Ballard's Diary](http://historying.org/2010/04/01/topic-modeling-martha-ballards-diary/).
I took a lot of notes, and then accidentally deleted them.

Ted Underwood's 18th century "topic tree": [the tree](http://tedunderwood.com/18c-tree/), and [some explanation](http://tedunderwood.com/2011/04/04/revealing-the-relationships-between-topics-in-a-corpus/).
I took a lot of notes, and then accidentally deleted them.

## What Am I Trying To Do Here?

I have 208 plot summaries of novels. The summaries are roughly 1 to 5 paragraphs each, and stylistically sparse. I know the author gender and publication date for most of these novels.

The expecting topic-modeling-y questions would probably be:

1. What is the Gothic "about"? How do these topics change in prevalence over time? (Could probably be fluffed into a paper on its own if any trends emerge, but would work better in conjunction with something else.)

2. What books are the most "Gothic-y"? Or, for each thing that the Gothic is "about", what books are most representative of that thing? (If any of these are really unexpected, could be a paper on its own, with normal-English discussion of the books in question. If it's basically what people already think, would work better in conjunction with something else.)

So the normal thing to do would be to feed my plot summaries into Mallet, and use its results to answer 1 and 2 and make them a paper together. I have a lot of more complicated questions, though, that I am really interested in. The first three basically boil down to, "What does it look like if I sort everything into the two categories of...?"

3. **Male vs Female**. My preliminary research (just counting the relative prevalence of 70 motifs listed in the index of a bibliography) suggested there are lots of things that are mostly written about by men (torture, corpses, incest) but nothing that is mostly written about by women. Does that still hold? (There are several competing conceptions of the relative prevalence of the Male Gothic vs the Female Gothic, so just fact-checking the two genres' existence could be a paper regardless of the results.)

What does a very 'male' book look like? A very 'female' book? (If these match the ways people typically define the Male and Female Gothics, this would be good for a page or two in a paper arguing something else. If they don't match, this would be a paper all on its own, and a really interesting one.)

I have about six books for which no author information is known; based on the other documents, can I make guesses about them? (I won't be able to confirm this guess, but it will make for a good page or two of discussion either way, in a paper mostly about something else.)

4. **Horror vs. Terror**. These are the two genres of Gothic novel that scholars talk about. I could give you the horror/terror designations of maybe twenty novels (because I've read them) and then we can see if we can guess it for the others! (I can't imagine that these differences would be detectable from the plot summaries; the differences are largely stylistic, so this would probably have to wait until I had a corpus of full texts. It'll make a great paper then, though.)

5. **Novel vs. Chapbook**. Some of these plot summaries are of expensive multi-volume novels, and some are of cheap 72-page chapbooks. (Everything is either a novel or a chapbook.) I wanna ask all my men-vs-women questions again, this time about novels vs. chapbooks: are they different? How are they different? (This would also be a paper all by itself.)

Upon reflection, those might actually be asking "What happens if I sort everything into these two categories, and then map some kind of network?" The next three are definitely just network questions:

6. **Names**. A lot of names get re-used across stories. A lot of names are unlikely to show up in existing lists of names. (My favourite is a woman named Euthanasia. *Mary Shelley* named a character Euthanasia.) Can a program identify which words are names, and put them in a bucket for me? With only 208 books, I can also manually delete all the non-name words from each document, and feed that new corpus to a program to put the names in a bucket and count them. Can a program make me a network map of books that share character names? (This would be a paper by itself, though the more interesting the resulting network is, the better the paper will be.)

7. **Schools**. How well does the Gothic 'canon' match the large body of Gothic texts? Do books cluster in different 'schools'? If so, are these based around the acknowledged canon, or are there schools/influential books that the canon has overlooked? 

8. **Plagiarism**. It is well-accepted that the Gothic was marked by plagiarism, and not just in the creation of cheap abridgments of popular novels. Is it possible to see who was plagiarizing from whom, and how much?

Questions that I can already answer by myself in excel the way I did my paper on motifs:
* Do men or women write more chapbooks vs novels? How do chapbook/novel counts change over time? (A few paragraphs in a paper mostly about something else.)
* How long are most novels? How long are their chapters/ how many chapter do they have? Do these differences in form track to other differences, in author or time or subject matter?
* What time periods are most novels set in? What places? (These are questions a human will have to answer.) For each one, is it written about more by men or by women? How does the popularity of each one change over time? (If I do both time and place, probably a paper.)

It occurs to me, all the places where I say "paper" here, I really mean "chapter of my dissertation." Or "the entirety of my master's essay." 

## Potential Resources
[David Mimno's Topic Modeling Bibliography](http://mimno.infosci.cornell.edu/topics.html)

[Chang’s implementation of LDA and related models in R](http://cran.r-project.org/web/packages/lda/index.html) Code package; currently completely incomprehensible.