# Hugo BERANGER - M2 MIAGE IA

import xml.etree.ElementTree as ET
import nltk
import re
from SPARQLWrapper import SPARQLWrapper
from nltk.corpus import wordnet as wn

tree = ET.parse('questions.xml')
root = tree.getroot()

# Extracting questions and tokenizing them
questions = []
questions_tokenized = []
questions_tagged = []

dataset = root.findall('.//question')
for element in dataset:
    question = element.find('string').text
    questions.append(question)

    token = nltk.word_tokenize(question)
    questions_tokenized.append(token)

    tag = nltk.pos_tag(token)
    questions_tagged.append(tag)

    # print(question)
    # print(token)
    # print(tag)

# Extracting nouns
questions_nouns = [[]]
for question in questions_tagged:
    nouns = []
    for tags in question:
        if tags[1] == "NNP" or tags[1] == "NN" or tags[1] == "NNPS" or tags[1] == "NNS":
            nouns.append(tags[0].lower())
    questions_nouns.append(nouns)

# Extracting verbs
questions_verbs = [[]]
for question in questions_tagged:
    verbs = []
    for tags in question:
        if tags[1] == "VBZ" or tags[1] == "VBD" or tags[1] == "VBG" or tags[1] == "VBP" or tags[1] == "VB":
            verbs.append(tags[0].lower())
    questions_verbs.append(verbs)


# Extracting types
questions_type = []
for question in questions_tagged:
    qtype = ""
    for tags in question:
        word = re.search(
            "(\"|Who|What|Where|Which|Give|Many|Much|When|\")", tags[0], re.IGNORECASE)
        if word:
            qtype = tags[0].lower()
    questions_type.append(qtype)

# Analyzing the reponses that the user is looking for
responses_type = []
for qtypes in questions_type:
    rtype = ""
    if(qtypes == "who"):
        rtype = "person"
    elif(qtypes == "what" or qtypes == "give" or qtypes == "which"):
        rtype = "something"
    elif(qtypes == "where"):
        rtype = "place"
    elif(qtypes == "many" or qtypes == "much"):
        rtype = "value"
    elif(qtypes == "when"):
        rtype = "time/date"
    responses_type.append(rtype)

# Saving which word is the closest from our relation word
closest_relation = [[]]
for verbs in questions_verbs:
    for verb in verbs:
        file = open('relations.txt', "r")
        print("===========")
        print(verb)
        closest_word = ""
        highest_num = 0
        lines = file.readlines()
        for line in lines:
            word=""
            word = line.replace("dbo:","")
            word = word.replace("dbp:","")
            word = word.strip()
            word1 = wn.synsets(verb+'.n.01')
            print(wn.synsets(verb)[0])
            if(len(wn.synsets(word)) > 0):
                word2 = wn.synsets(word)[0]
                print(word1.path_similarity(word2))
                if (word1.path_similarity(word2) > highest_num):
                    highest_num = word1.path_similarity(word2)
                    closest_word = word
        print(closest_word)
        print(highest_num)
        file.close()
        print("===========")

# Showing what's understood
def show():
    for i in range(len(questions)):
        print(questions[i])
        print("Quetion type   : {}".format(questions_type[i]))
        print("Question nouns : {}".format(questions_nouns[i+1]))
        print("Question verbs : {}".format(questions_verbs[i+1]))
        print("Response type  : {}".format(responses_type[i]))
        print("===================================================")


#show()

# Creating requests
queries = []
for i in range(len(questions)):
    t = ""
    query = "SELECT "
    query += responses_type[i]
    query += " FROM "
    query += " "
    #print(questions[i])
    #print(query)


queryString = "PREFIX space: <http://purl.org/net/schemas/space/>SELECT ?craft {?craft a space:Spacecraft} LIMIT 50" 
sparql = SPARQLWrapper("https://wiki.dbpedia.org/")

sparql.setQuery(queryString)

try :
   ret = sparql.query()
   print(ret)
   # ret is a stream with the results in XML, see <http://www.w3.org/TR/rdf-sparql-XMLres/>
except :
   print("QUERY FAILED")

