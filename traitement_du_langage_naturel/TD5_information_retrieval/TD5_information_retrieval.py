# Hugo BERANGER - M2 MIAGE IA

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer 
from collections import OrderedDict 
#nltk.download('stopwords')
from math import *

# STEP 1 / STEP 2 TASK 1 - get the texts
tokens = []
for x in range (10):
    with open('texts/'+str(x)+'.txt','r') as file:
    #with open('texts_test/'+str(x)+'.txt','r') as file: 
        doc = [] 
        for line in file:
            token = nltk.word_tokenize(line)   
            for word in token:          
                doc.append(word)
        tokens.append(doc)
#print(tokens)

# STEP 2 TASK 2 - delete stop words and punctuation
filtered_tokens = []
filtered_doc = []
stop_words = set(stopwords.words('english'))
#stop_words = set(stopwords.words('french'))
for doc in tokens:
    for token in doc:
        if token not in stop_words and token != "." and token != "!" and token != "?" and token != "-" and token != "(" and token != ")" and token != "—" and token != "," and token != ";" and token != ":":
            filtered_doc.append(token)
    filtered_tokens.append(filtered_doc)
    filtered_doc = []
tokens = filtered_tokens
#print(tokens)

# STEP 2 TASK 3 - lemmatize the tokens
porter = PorterStemmer()
for x in range(len(tokens)):
    for y in range(len(tokens[x])):
        tokens[x][y] = porter.stem(tokens[x][y])
#print(tokens)

# STEP 2 TASK 4 - create a general dictionnary
dict_all = dict()
for doc in tokens:
    for token in doc:
        if token in dict_all:
            dict_all[token] += 1
        else:
            dict_all[token] = 1
#print(dict_all)

# STEP 2 TASK 5 - create a dictionary for documents
dict_doc = []
dictionnary = dict()
for doc in tokens:
    for token in doc:
        if token in dictionnary:
            dictionnary[token] += 1
        else:
            dictionnary[token] = 1
    dict_doc.append(dictionnary)
    dictionnary = dict()
#print(dict_doc)

# STEP 3 - create an inverted dictionnary
dict_inv = dict()
doc_inv = []
for token in dict_all:
    for x in range(len(dict_doc)):
        if token in dict_doc[x]:
            doc_inv.append(x)
    dict_inv[token] = doc_inv
    doc_inv = []
#print(dict_inv)

# STEP 4 TASK 0 - get the number of occurrences of a word per document
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return ceil(n * multiplier) / multiplier

def get_occurences(word):
    docs = dict()
    docs_sorted = dict()
    for token in dict_inv:
        if token == word:
            for doc in dict_inv[token]:
                docs[doc] = round_up(dict_doc[doc][token]/len(dict_doc[doc]),5)
                #docs[doc] = dict_doc[doc][token] # other way to calculate the number of occurrences

    sorted_keys = sorted(docs, key=docs.get, reverse=True)
    for w in sorted_keys:
        docs_sorted[w] = docs[w]

    #print(docs_sorted)
    return docs_sorted


# STEP 4 TASK 1 - processes requests
def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

def boolean_request(request):
    print("==========================================================")
    print("request      :",request)
    docs = dict()
    docs_sorted = dict()

    processed = ["NOT","AND",'OR']  # contains words that have already been processed
    for x in range(10):
        docs[x] = 0

    request = request.split() 

    for x in range(len(request)):
        if request[x] == "NOT":
            #print("NOT")
            processed.append(request[x+1])
            negation = request[x+1]
            negation_occ = get_occurences(porter.stem(negation))
            #print("negation : "+str(negation)+" - "+str(negation_occ))
            if (len(negation_occ) > 0):
                for y in range(len(docs)):
                    if y in negation_occ:
                        docs[y] -= negation_occ[y] 

        if request[x] == "AND":
            #print("AND")
            if request[x-1] not in processed:
                processed.append(request[x-1])
                first = request[x-1]
                first_occ = get_occurences(porter.stem(first))
                #print("first : "+str(first)+" - "+str(first_occ))
                if (len(first_occ) > 0):
                    for y in range(len(docs)):
                        if y in first_occ:
                            docs[y] += first_occ[y] 
            processed.append(request[x+1])
            second = request[x+1]
            second_occ = get_occurences(porter.stem(second))
            #print("second : "+str(second)+" - "+str(second_occ))
            if (len(second_occ) > 0):
                for y in range(len(docs)):
                    if y in second_occ:
                        docs[y] += second_occ[y]
        
        if request[x] == "OR":
            #print("OR")     
            if request[x-1] not in processed:
                processed.append(request[x-1])
                first = request[x-1]
                first_occ = get_occurences(porter.stem(first))
                #print("first : "+str(first)+" - "+str(first_occ))
            processed.append(request[x+1])
            second = request[x+1]
            second_occ = get_occurences(porter.stem(second))
            #print("second : "+str(second)+" - "+str(second_occ))

            if (len(second_occ) > 0):
                if (len(first_occ) > 0):
                    if next(iter(first_occ.values())) >= next(iter(second_occ.values())):
                        for y in range(len(docs)):
                            if y in first_occ:
                                if docs[y] < first_occ[y]:
                                    docs[y] = first_occ[y]
                else:
                    for y in range(len(docs)):
                        if y in second_occ:
                            if docs[y] < second_occ[y]:
                                docs[y] = second_occ[y]
            
            if (len(first_occ) > 0):
                if (len(second_occ) > 0):
                    if next(iter(second_occ.values())) >= next(iter(first_occ.values())):
                        for y in range(len(docs)):
                                if docs[y] < second_occ[y]:
                                    docs[y] = second_occ[y]
                else:
                    for y in range(len(docs)):
                        if y in first_occ:
                            if docs[y] < first_occ[y]:
                                docs[y] = first_occ[y]

        if len(request) >= x+1: # natural language requests
            if len(request) == x+1:
                if request[x] not in processed:
                    processed.append(request[x])
                    not_processed = request[x-1]
                    not_processed_occ = get_occurences(porter.stem(not_processed))
                    if(len(not_processed_occ) > 0):
                        for y in range(len(docs)):
                            if y in not_processed_occ:
                                docs[y] += not_processed_occ[y]
            elif request[x+1] != "OR" and request[x+1] != "AND":
                if request[x] not in processed:
                    processed.append(request[x])
                    not_processed = request[x-1]
                    not_processed_occ = get_occurences(porter.stem(not_processed))
                    if(len(not_processed_occ) > 0):
                        for y in range(len(docs)):
                            if y in not_processed_occ:
                                docs[y] += not_processed_occ[y]


    sorted_keys = sorted(docs, key=docs.get, reverse=True)  # sort the documents by order
    for w in sorted_keys:
        docs_sorted[w] = docs[w]
    docs = docs_sorted
    
    for k in docs.copy():   # delete document that have no results
        if docs[k] == 0:
            docs.pop(k)
    keys = list(docs)
    
    if(len(keys)==0):    # not words in the documents
        print("error        : no word in the documents")
        return 0
    else:
        key = keys[0]

    tf = abs(docs[key])
    #idf = log(len(docs)/10) # other  way to calculate IDF
    idf = abs(log(1/10))
    res = docs[key]*idf

    print("docs scores  : "+str(docs))
    print("best doc     : "+str(key))
    print("tf           : "+str(round_up(tf,5)))          # TF
    print("idf          : "+str(round_up(idf,5)))         # IDF
    print("tf*idf       : "+str(round_up(res,5)))         # TF * IDF
    print("==========================================================")

    return key,tf,res

# REQUESTS TEST
## boolean requests
boolean_request("desease AND severe AND pneumonia")
boolean_request("antibody AND plasma AND (cells OR receptors)")
boolean_request("antimalarial drugs OR antiviral agents OR immunomodulators")
boolean_request("NOT plasma AND risk of infection AND restrictions")
boolean_request("(older adults AND antibodies) AND NOT (genomes OR variant)")

## natural language requests
boolean_request("antibody treatments")
boolean_request("efficacy and safety of the treatments")
boolean_request("family access to hospitals")
boolean_request("contact tracing results")
boolean_request("genomic analysis of SARS-CoV-2 disease")

boolean_request("hugo")                     # test non-existing word
boolean_request("covid-19")                 # test single word
boolean_request("NOT covid-19")             # test NOT
boolean_request("covid-19 AND covid-19")    # test AND
boolean_request("covid-19 OR covid-19")     # test OR