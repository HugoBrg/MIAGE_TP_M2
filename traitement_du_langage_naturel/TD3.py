import xml.etree.ElementTree as ET
import nltk
import re

tree = ET.parse('questions.xml')
root = tree.getroot()

#Extracting questions and tokenizing them
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
    
    #print(question)
    #print(token)
    #print(tag)

#Extracting nouns
questions_nouns = [[]]
for question in questions_tagged:
    nouns=[]
    for tags in question:
        if tags[1] == "NNP" or tags[1] == "NN" or tags[1] == "NNPS":
            nouns.append(tags[0].lower())       
    questions_nouns.append(nouns)

#Extracting types
questions_type = []
for question in questions_tagged:
    qtype = ""
    for tags in question:
        x = re.search("(\"|Who|What|Where|Which|Give|Many|Much|When|\")",tags[0],re.IGNORECASE)
        if x:
            qtype = tags[0].lower()
    questions_type.append(qtype)

#Analyzing the reponses that the user is looking for
responses_type = []
for qtypes in questions_type:
    rtype = ""
    for qtype in qtypes:
        if(qtype == "who"):
            rtype = "person"
        elif(qtype == "what" or qtype == "give" or qtype == "which"):
            rtype = "something"
        elif(qtype == "where" ):
            rtype = "place"
        elif(qtype == "many" or qtype == "much"):
            rtype = "value"
        elif(qtype == "when"):
            rtype = "time/date"
    responses_type.append(rtype)

#Showing what's understood
def show():
    for i in range(len(questions)):
        print(questions[i])
        print("Quetion type   : {}".format(questions_type[i]))
        print("Question nouns : {}".format(questions_nouns[i+1]))
        print("Response type  : {}".format(responses_type[i]))
        print("===================================================")
show()

#Creating requests
requests = []
for i in range(len(questions)):
    t =""
    request = "SELECT "
    request += questions_type[i]
    print(questions[i])
    print(request)
