### Topic Modeling Notes
#### Works Read
[Topic Modeling and Network Analysis](http://www.scottbot.net/HIAL/?p=221) by Scott Weingart.
* Explains LSA and LDA.
* Gives examples of topic models from networks, and networks from topic models.

[LSA is a marvellous tool, but literary historians may want to customize it for their own discipline.](http://tedunderwood.com/2011/10/16/lsa-is-a-marvellous-tool-but-humanists-may-no-use-it-the-way-computer-scientists-do/) by Ted Underwood.
* Value of LSA is not its ability to identify synonyms (which is what information retrieval (i.e., mom) uses it for)
* avoid SVD because it compresses the matrix too much/in the wrong way, to find transitive kinds of association. --> highlights semantic relationships at the cost of slightly blurring other kinds of association
* if you’re interested in “topics” that are strictly semantic, you might want to use an algorithm that reduces dimensionality with SVD. If you’re interested in discourses, sociolects, genres, or types of diction, you might use LSA without dimensionality reduction.
* Ways of weighting:
    - For the normal LSA algorithm that uses dimensionality reduction, the consensus is that “log-entropy weighting” works well. You take the log of each frequency, and multiply the whole term vector by the entropy of the vector. I have found that this also works well for humanistic purposes.
    - For LSA without dimensionality reduction, I would recommend weighting cells by subtracting the expected frequency from the observed frequency. This formula “evens the playing field” between common and uncommon words — and it does so, vitally, in a way that gives a word’s absence from a long document more weight than its absence from a short one. (Not something I care about with plot summaries, because they're all basically the same length.)
    
[Tech note](http://tedunderwood.com/tech-notes/) by Ted Underwood.
* Vector space model works better than simple Pearson’s correlation, because the “cosine similarity” measure used in a vector space model automatically gives more weight to longer documents, and to documents where a term is very strongly represented. (I don't care about document length at the plot-summary stage. Do I care about documents where a term is very strongly represented? Will I want to give longer documents more weight later?)
* INSTEAD OF TF-IDF, because we're not interested in the rarest words but just the words themselves, assess frequency as the difference between the expected occurrence of a term and the actual number of occurrences in the document. -->  this formula: occurrences of X in Y – ((Y length/corpus length) * total occurrences of X in corpus)
* This means that some components of the vector are negative, which is actually important. Otherwise the fact that a word doesn’t occur in a book of 100,000 words would have the same weight as the fact that it doesn’t occur in a play of 15,000 words, because they would both “bottom out” at zero. (Definitely something that matters when I get to full texts.)
* Of course, the “topic trees” produced by this measure are only as good as the lists of words you feed into them. (Wait, at what stage did we feed in a list of words???????)
* It may be controversial whether or not to call this “topic modeling.” If you want to describe the internal structure of a literary work, this technique of course won’t do the job directly, because it doesn’t divide works into parts. But I think it does a pretty good job of identifying the implicit thematic structure of eighteenth-century discourse as a whole, and I wouldn’t be surprised if it turned out that the internal structure of individual works is defined in large part by the way these corpus-level topics weave in and out of them.
* I actually think I... don't want to weight novels by length? Since I don't think length influences the importance of the story to readers...? Udolpho and The Veiled Picture are both just 'a reading experience'? Or does Udolpho have a bigger impact...? I think I need to be very careful about what question I'm asking.

[Document Similarity Based on Concept Tree Distance](http://citeseer.uark.edu/projects/citeseerX/papers/HT2008_short_paper.pdf), by Susan Gauch.
* Concept tree distance is an alternative to vector space models
* Traditional vector space models (i.e. LSA?) turn keyword vectors into concept vectors (i.e. collapse columns??) to reduce semantic ambiguity. However, this ignores the parent-child relationships that the keywords have inside those concept vectors.
* In this study, we introduce a novel technique to construct concept trees representing documents and we apply the tree edit distance algorithm to calculate document similarity.
* Looks like a better way to identify whether documents are related to each other. Not useful if I want to find out what concepts my corpus is mostly about, potentially useful if I want to map a network of their relationships.

[Topic Modeling With the JAVA GUI + Gephi](http://electricarchaeology.ca/2011/11/11/topic-modeling-with-the-java-gui-gephi/) - Prepare your corpus of text, get topics with MALLET, prune the CSV, make a network, visualize it!
* Not actually a tutorial.

[Visualizing Structure in Topic Models](http://www.r-bloggers.com/visualising-structure-in-topic-models/)
* Argues that network maps aren't appropriate, points to a lot of other articles.

[The Digital Humanities Contribution to Topic Modeling](http://journalofdigitalhumanities.org/2-1/dh-contribution-to-topic-modeling/)
* Describes what's gonna be in the journal... looks less focused on specific research case uses than I'd hoped, but still handy.

[Topic Modeling and Digital Humanities](http://journalofdigitalhumanities.org/2-1/topic-modeling-and-digital-humanities-by-david-m-blei/) by David M. Blei
* "Formally, a topic is a probability distribution over terms. In each topic, different sets of terms have high probability, and we typically visualize the topics by listing those sets (again, see Figure 1). As I have mentioned, topic models find the sets of terms that tend to occur together in the texts.[2] They look like “topics” because terms that frequently occur together tend to be about the same subject."
* "Traditionally, statistics and machine learning gives a “cookbook” of methods, and users of these tools are required to match their specific problems to general solutions. In probabilistic modeling, we provide a language for expressing assumptions about data and generic methods for computing with those assumptions."
* "In particular, LDA is a type of probabilistic model with hidden variables. Viewed in this context, LDA specifies a generative process, an imaginary probabilistic recipe that produces both the hidden topic structure and the observed words of the texts. ...Given a collection of texts, they reverse the imaginary generative process to answer the question “What is the likely hidden topical structure that generated my observed documents?”"
* "Probabilistic models beyond LDA posit more complicated hidden structures and generative processes of the texts. As examples, we have developed topic models that include syntax, topic hierarchies, document networks, topics drifting through time, readers’ libraries, and the influence of past articles on future articles." --> mom can point me towards a handy suite?
* "Here is the rosy vision. A humanist imagines the kind of hidden structure that she wants to discover and embeds it in a model that generates her archive. The form of the structure is influenced by her theories and knowledge — time and geography, linguistic theory, literary theory, gender, author, politics, culture, history. With the model and the archive in place, she then runs an algorithm to estimate how the imagined hidden structure is realized in actual texts. Finally, she uses those estimates in subsequent study, trying to confirm her theories, forming new theories, and using the discovered structure as a lens for exploration. She discovers that her model falls short in several ways. She revises and repeats." --> What hidden structure am I looking for...?
* *"A model of texts, built with a particular theory in mind, cannot provide evidence for the theory. (After all, the theory is built into the assumptions of the model.) Rather, the hope is that the model helps point us to such evidence."*
* "The goal is for scholars and scientists to creatively design models with an intuitive language of components, and then for computer programs to derive and execute the corresponding inference algorithms with real data. ...Probabilistic models promise to give scholars a powerful language to articulate assumptions about their data and fast algorithms to compute with those assumptions on large archives." --> So if I'm gonna get mom involved I need to start with a specific hypothesis, and model in a way that allows that hypothesis to be tested. I sort of already knew that, but I'll need to really focus on it.

[Topic Modeling and Figurative Language](http://journalofdigitalhumanities.org/2-1/topic-modeling-and-figurative-language-by-lisa-m-rhody/) by LISA M. RHODY
* "LDA assumes that documents are like your neighbors’ baskets, and your neighbors are like authors who select from a limited number of available types of words in order to produce documents — in this case poems. Each author chooses to varying degrees how much of each kind of topic they use for each document; however, the number of total available topics, just like the total number of kinds of produce remains constant. While this constraint, the assumption that all the words in a corpus could be derived from a limited set of topics, strikes the human reader as an artificial limitation, it is a necessary constraint in order for LDA to work." --> Rhody chooses a genre of poetry which is assumed to be based on a small set of conventions, well suited to LDA; the Gothic is seen much the same way, also well-suited to LDA?
* **Should I use my Gothic 'canon' as training texts to identify the topics?** Or will this make it impossible to identify when books diverge interestingly from that canon?
* "Topic models (and LDA is one kind of topic modeling algorithm) are generative, unsupervised methods of discovering latent patterns in large collections of natural language text"
* "As Ian H. Witten, Eibe Frank, and Mark A. Hall remind us in Data Mining: Practical Machine Learning Tools and Techniques, the guiding factors for text mining generally and topic modeling specifically are to generate *actionable* and *comprehensible* results (9.5)."
* "methods for measuring the “interpretability of a topic model” (2). The authors present two human evaluation tests meant to discern the accuracy of models by using the keyword distributions ...and the topic to document probabilities ... — called word intrusion and topic intrusion tests respectively" --> referencing [this CS paper](http://www.umiacs.umd.edu/~jbg/docs/nips2009-rtl.pdf); not relevant
* "For the purposes of modeling poetry data, word intrusion would not be as effective a method for determining a model’s accuracy at categorizing documents or detecting latent patterns unless the specific changes that happen to the nature of topic distributions for poetic corpora are adjusted for. “Intruders” as individual words does not work for LDA topics of poetry because poems purposefully access and repurpose language in unexpected ways. In other words, topics from the models in my project were not easily interpreted by keywords alone, and yet the results are still useful."
* "My research confirms, to a degree, Ted Underwood’s suspicion that topics in literary studies are better understood as a representation of “discourse” (language as it is used and as it participates in recognized social forms) rather than a thematic string of coherent terms."
* "Topic models of poetry do not reflect the anecdotal evidence that LDA frequently leads to semantically meaningful word distributions. Instead, topic models of the Revising Ekphrasis dataset created four consistently recurring types of topics." --> 1, OCR and other language or dialect distinctive features; 2, Large “chunk” topics (Longer poems pull one or more topics toward language specific to them); 3, Semantically evident topics (but the illusion of thematic comprehensibility obscures what is actually being captured by the topic model; more accurate to say that Topics 32 and 54 participate in discourses surrounding “night” and “natural landscapes”); 4, Semantically opaque topics (her example didn't look opaque to me, but I'll accept the framing of "discourses of elegy" rather than "topic of death")
* Conclusion... isn't about ekphrasis at all. So, not a model I can take for what my own final project should try to look like-- but still a useful read overall, and something it could be useful to quote from.

#### Works To-Read?
http://www.scottbot.net/HIAL/?p=39600
http://tedunderwood.com/2012/11/11/visualizing-topic-models/
http://sappingattention.blogspot.ca/

**[Journal of Digital Humanities](http://journalofdigitalhumanities.org/2-1/dh-contribution-to-topic-modeling/)

[Getting Started with Mallet and Topic Modeling](http://electricarchaeology.ca/2011/08/30/getting-started-with-mallet-and-topic-modeling/) Links to sequel below

[EXTREMELY specific walkthrough of using mallet](http://programminghistorian.org/lessons/topic-modeling-and-mallet)

explain how the extensibility of LDA makes it quite a different kind of beast (relative to LSA): Learning author-topic models from text corpora. M Rosen-Zvi, C Chemudugunta, T Griffiths, P Smyth, M Steyvers, ACM Transactions on Information Systems (TOIS), ACM, 2010. http://www.datalab.uci.edu/papers/AT_tois.pdf

Closing out my to-read tabs:
http://tedunderwood.com/2011/03/17/a-selection-of-the-language-really-spoken-by-men/
http://tedunderwood.com/category/18c/
http://tedunderwood.com/category/methodology/
http://sappingattention.blogspot.ca/2011/01/clustering-from-search.html
http://www.matthewjockers.net/2011/09/29/the-lda-buffet-is-now-open-or-latent-dirichlet-allocation-for-english-majors/
https://ariddell.org/simple-topic-model.html
http://www.scottbot.net/HIAL/?p=19113