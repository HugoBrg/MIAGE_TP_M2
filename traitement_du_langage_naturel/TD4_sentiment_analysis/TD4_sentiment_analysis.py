# Hugo BERANGER - M2 MIAGE IA

# install nltk and SPARQLWrapper
import xml.etree.ElementTree as ET
import nltk
import re

tree = ET.parse('Restaurants_Train.xml')
root = tree.getroot()

# Extracting reviews and tokenizing them
reviews_raw = []
reviews_tokenized = []
reviews_tagged = []

dataset = root.findall('.//sentence')
for element in dataset:
    question = element.find('text').text
    reviews_raw.append(question)

    token = nltk.word_tokenize(question)
    reviews_tokenized.append(token)

    tag = nltk.pos_tag(token)
    reviews_tagged.append(tag)

    #print(question)
    #print(token)
    #print(tag)

reviews_manually_tagged = [[[]]]
for x in range(len(reviews_tagged)):
    to_append = [[]]
    for y in range(len(reviews_tagged[x])):
        couple = []
        negation = re.search("(\"|Not\\b|\\w+'t|no\\b|\")", reviews_tagged[x][y][0], re.IGNORECASE)
        if negation:
            #print(reviews_tagged[x][y][0])
            couple.append(reviews_tagged[x][y][0])
            couple.append("NEG")
        else:
            couple.append(reviews_tagged[x][y][0])
            couple.append('') 
        to_append.append(couple)
    reviews_manually_tagged.append(to_append)


        
        