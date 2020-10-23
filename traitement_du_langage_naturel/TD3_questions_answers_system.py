# Hugo BERANGER - M2 MIAGE IA

import xml.etree.ElementTree as ET
import nltk
import re
from SPARQLWrapper import SPARQLWrapper
from difflib import SequenceMatcher

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

to_iterate = [[]]
to_iterate_group = []
#print(len(questions))
for x in range(len(questions)):
    for a in range(len(questions_verbs[x])):
        to_iterate_group.append(questions_verbs[x])
    for c in range(len(questions_nouns[x])):
        to_iterate_group.append(questions_nouns[x])
    #print("KEK : ",to_iterate_group)
    to_iterate.append(to_iterate_group)

#print(len(to_iterate))
    
# Saving which word is the closest from our relation word
closest_relation = [[]]
for verbs in questions_verbs:
    #print("===========") 
    file = open('relations.txt', "r")
    lines = file.readlines()
    closest_duo = []
    closest_word = ""
    similarity = 0
    aword = ""
    for verb in verbs:
        aword = verb
        #print("verb        :",verb)
        for line in lines:
            word= ""
            word = line.replace("dbo:","")
            word = word.replace("dbp:","")
            word = word.strip()
            if(SequenceMatcher(None,verb,word).ratio() >= similarity):
                similarity = SequenceMatcher(None,verb,word).ratio()
                closest_word = word

    closest_duo.append(aword)
    closest_duo.append(closest_word)
    closest_relation.append(closest_duo)
    #print("closest word : ",closest_word)
    #print("closest duo  : ",closest_duo)
    #print("===========")    
    file.close()
closest_relation.pop(0)


# Creating requests
queries = []
sparql = SPARQLWrapper("https://wiki.dbpedia.org/")
for i in range(len(questions)):
    query = "PREFIX dbo: <http://dbpedia.org/ontology/>PREFIX res: <http://dbpedia.org/resource/> SELECT DISTINCT ?uri WHERE {res:"
    query += questions_nouns[i+1][0]
    query += " dbo:"
    query += closest_relation[i+1][1]
    query += " ?uri .}"
    #print(questions[i])
    #print(query)
    queries.append(query)


# Showing what's understood
def show():
    for i in range(len(questions)):
        print(questions[i])
        print("Quetion type   : ",questions_type[i])
        print("Question nouns : ",questions_nouns[i+1])
        print("Question verbs : ",questions_verbs[i+1])
        print("Closest duo    : ",closest_relation[i+1])
        print("Response type  : ",responses_type[i])
        print("Query          : ",queries[i])
        print("===================================================")

show()

nb_fail = 0
nb_success = 0
for x in range(len(queries)):
    query = queries[x]
    #print(query)
    sparql.setQuery(query)

    try :
        ret = sparql.query()
        print("QUERY SUCCESS")
        print(ret)
        nb_success += 1
    except :
        print("QUERY FAILED")
        nb_fail += 1

# Test query, doesn't work
query = "PREFIX dbo: <http://dbpedia.org/ontology/>PREFIX res: <http://dbpedia.org/resource/>SELECT DISTINCT ?uri WHERE {res:Wikipedia dbo:author ?uri .}"

sparql.setQuery(query)
try :
    ret = sparql.query()
    print("QUERY SUCCESS")
    print(ret)
except :
    print("QUERY FAILED")

print("Number of successful requests : ",nb_success)
print("Number of failed requests     : ",nb_fail)
