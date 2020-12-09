# Hugo BERANGER - M2 MIAGE IA

# install nltk and SPARQLWrapper
import xml.etree.ElementTree as ET
import nltk
import re
from SPARQLWrapper import SPARQLWrapper
from difflib import SequenceMatcher
import nltk
from termcolor import colored
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

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

"""
# Extracting nouns
questions_nouns = [[]]
for question in questions_tagged:
    dbo = []
    for tags in question:
        if tags[1] == "NNP" or tags[1] == "NN" or tags[1] == "NNPS" or tags[1] == "NNS":
            dbo.append(tags[0].lower())
    questions_nouns.append(dbo)
"""

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

"""
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
"""
"""
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
"""

# Saving which word is the closest from our relation word
closest_relation = [[]]
for verbs in questions_verbs:
    file = open('relations.txt', "r")
    lines = file.readlines()
    closest_duo = []
    closest_word = ""
    similarity = 0
    aword = ""
    for verb in verbs:
        aword = verb
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
    file.close()
closest_relation.pop(0)
closest_relation.pop(0)


# Adapting dbo and res according to question types
questions_dbo = []
questions_res = []
for x in range(len(questions_type)):
    dbo = ""
    res = ""
    if questions_type[x] == "who":
        for i in range(len(questions_tagged[x])):
            if(questions_tagged[x][i][1]) == "NNP":
                dbo += questions_tagged[x][i][0] + "_"
        dbo = dbo[:-1]
        res = closest_relation[x][1] + " ?uri"
    if questions_type[x] == "when":
        for i in range(len(questions_tagged[x])):
            if(questions_tagged[x][i][1]) == "NNP":
                dbo += questions_tagged[x][i][0] + "_of_"
        res = "date"
        dbo = res[:-4]  + " ?date"
    if questions_type[x] == "which":
        for i in range(len(questions_tagged[x])):
            if(questions_tagged[x][i][1]) == "NN" or (questions_tagged[x][i][1]) == "NNS" or (questions_tagged[x][i][1]) == "VBG":
                res += questions_tagged[x][i][0] + "_"
            if(questions_tagged[x][i][1]) == "NNP":
                dbo += questions_tagged[x][i][0] + "_"
        dbo = dbo[:-1]
        res = res[:-1] + " ?uri"
    if questions_type[x] == "what":
        for i in range(len(questions_tagged[x])):
            if(questions_tagged[x][i][1]) == "NN" or (questions_tagged[x][i][1]) == "JJ" or (questions_tagged[x][i][1]) == "JJS" or (questions_tagged[x][i][1]) == "NNS":
                res += questions_tagged[x][i][0] + "_"
            if(questions_tagged[x][i][1]) == "NNP" or (questions_tagged[x][i][1]) == "NNPS":
                dbo += questions_tagged[x][i][0] + "_"
        dbo = dbo[:-1] 
        res = res[:-1] + " ?uri"
    if questions_type[x] == "many" or questions_type[x] == "much":
        for i in range(len(questions_tagged[x])):
            if(questions_tagged[x][i][1]) == "NNP":
                dbo += questions_tagged[x][i][0] + "_"
            if(questions_tagged[x][i][1]) == "NNS":
                res += "numberOf" + questions_tagged[x][i][0] + "_"
        dbo = dbo[:-1]
        res = res[:-1] + " ?number"
    if questions_type[x] == "give":
        for i in range(len(questions_tagged[x])):
            if(questions_tagged[x][i][1]) == "NN" or (questions_tagged[x][i][1]) == "JJ" or (questions_tagged[x][i][1]) == "JJS" or (questions_tagged[x][i][1]) == "NNS" or (questions_tagged[x][i][1]) == "VBG":
                dbo += questions_tagged[x][i][0] + "_"
            if(questions_tagged[x][i][1]) == "NNP" or (questions_tagged[x][i][1]) == "NNPS":
                res += questions_tagged[x][i][0] + "_"
        dbo = dbo[:-1]
        res = res[:-1] + " ?string"
    #print("res : {} | dbo : {}".format(res,dbo))
    questions_res.append(res)
    questions_dbo.append(dbo)

# Creating requests
queries = []
sparql = SPARQLWrapper("https://wiki.dbpedia.org/")
for i in range(len(questions)):
    query = "PREFIX dbo: <http://dbpedia.org/ontology/>PREFIX res: <http://dbpedia.org/resource/> SELECT DISTINCT ?uri WHERE {res:"
    # query += questions_nouns[i+1][0]
    query += questions_dbo[i]
    query += " dbo:"
    # query += closest_relation[i+1][1]
    query += questions_res[i]
    # query += " ?uri .}"
    query += " .}"
    # print(questions[i])
    # print(query)
    queries.append(query)


# Writing our queries into a file
f = open("queries.txt", "w")
for query in queries:
    f.write(query + "\n")
f.close()


# Comparing queries
with open('queries.txt') as f:
    ourQueries = list(f)

with open('queries_test.txt') as f:
    testQueries = list(f)

successCount = 0
for x in range(len(queries)):
    print("Question   : ",questions[x])
    print("myQuery    : ",ourQueries[x],end='')
    print("realQuery  : ",testQueries[x],end='')
    string1 = ourQueries[x].split()
    string2 = testQueries[x].split()
    if(string1 == string2):
        successCount += 1
    while(len(string1)) < (len(string2)):
        string1.append("")
    print("Difference :  ",end='')
    for z in range(len(string2)):
        if(string1[z] == string2[z]):
            print(colored(string1[z] + " " ,"green"),end='')
        else:
            print(colored(string1[z] + " " ,"red"),end='')
    print('\n')
    print("========================================================================================================================================================================")
print("Successful queries   : ",successCount)
print("Unsuccessful queries : ",26 - successCount)


nb_fail = 0
nb_success = 0
for x in range(len(queries)):
    query = queries[x]
    #print(query)
    sparql.setQuery(query)

    try :
        ret = sparql.query()
        # print("QUERY SUCCESS")
        print(ret)
        nb_success += 1
    except :
        # print("QUERY FAILED")
        nb_fail += 1


# Test query, doesn't work when it should
print("========================================================================================================================================================================")
query = "PREFIX dbo: <http://dbpedia.org/ontology/>PREFIX res: <http://dbpedia.org/resource/>SELECT DISTINCT ?uri WHERE {res:Wikipedia dbo:author ?uri .}"

sparql.setQuery(query)
try :
    ret = sparql.query()
    print("QUERY TEST SUCCESS")
    print(ret)
except :
    print("QUERY TEST FAILED")

print("Number of successful requests : ",nb_success)
print("Number of failed requests     : ",nb_fail)
