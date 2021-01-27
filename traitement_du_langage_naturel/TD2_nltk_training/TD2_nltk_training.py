# Hugo BERANGER - M2 MIAGE IA

import nltk
from nltk.corpus import brown
from nltk.corpus import treebank
import nltk.draw
from nltk.draw.tree import draw_trees
import tkinter
from tkinter import IntVar, Menu, Tk

nltk.download('treebank')

"""
text = nltk.word_tokenize("Now we are having a Linguistics class")
print(nltk.pos_tag(text))
"""

"""
brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
print(tag_fd.most_common())
"""

"""
text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
text.similar('woman')
text.similar('bought')
text.similar('over')
text.similar('the')
"""

"""
print(nltk.corpus.treebank.parsed_sents('wsj_0001.mrg')[1])
print(nltk.corpus.treebank.parsed_sents('wsj_0001.mrg')[1].draw())
"""

"""
grammar1 = nltk.CFG.fromstring(""S -> NP VP VP -> V NP | V NP PP PP -> P NP V -> "saw" | "ate" | "walked" NP -> "John" | "Mary" | "Bob" | Det N | Det N PP Det -> "a" | "an" | "the" | "my" N -> "man" | "dog" | "cat" | "telescope" | "park" P -> "in" | "on" | "by" | "with" "")
sent = "Mary saw Bob".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
    print(tree)
"""
