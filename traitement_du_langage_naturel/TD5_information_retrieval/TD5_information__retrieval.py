# Hugo BERANGER - M2 MIAGE IA

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer 
from collections import OrderedDict 
#nltk.download('stopwords')

# STEP 2 TASK 1
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

# STEP 2 TASK 2
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

# STEP 2 TASK 3
test = []
test.append("program")      # test
test.append("programming")  # test
tokens.append(test)

porter = PorterStemmer()
for x in range(len(tokens)):
    for y in range(len(tokens[x])):
        tokens[x][y] = porter.stem(tokens[x][y])
#print(tokens)

# STEP 2 TASK 4
dict_all = dict()
for doc in tokens:
    for token in doc:
        if token in dict_all:
            dict_all[token] += 1
        else:
            dict_all[token] = 1
#print(dict_all)

# STEP 2 TASK 5
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

# STEP 3
dict_inv = dict()
doc_inv = []
for token in dict_all:
    for x in range(len(dict_doc)):
        if token in dict_doc[x]:
            doc_inv.append(x)
    dict_inv[token] = doc_inv
    doc_inv = []
#print(dict_inv)

# STEP 4 TASK 0
def get_occurences(word):
    docs = dict()
    docs_sorted = dict()
    for token in dict_inv:
        if token == word:
            for doc in dict_inv[token]:
                #docs[doc] = dict_doc[doc][token]/len(dict_doc[doc])
                docs[doc] = dict_doc[doc][token]

    sorted_keys = sorted(docs, key=docs.get, reverse=True)
    for w in sorted_keys:
        docs_sorted[w] = docs[w]

    #print(docs_sorted)
    return docs_sorted


# STEP 4 TASK 1
def boolean_request(request):
    docs = dict()
    docs_sorted = dict()

    processed = []
    for x in range(10):
        docs[x] = 0

    request = request.split() 

    for x in range(len(request)):
        if request[x] == "NOT":
            processed.append(request[x+1])
            negation = request[x-1]
            negation_occ = get_occurences(porter.stem(negation))
            #print("negation : "+str(negation)+" - "+str(negation_occ))
            if (len(negation_occ) > 0):
                for y in range(len(docs)):
                    if y in negation_occ:
                        docs[y] -= negation_occ[y] 

        if request[x] == "AND":
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
            if request[x-1] not in processed:
                processed.append(request[x-1])
                first = request[x-1]
                first_occ = get_occurences(porter.stem(first))
                print("first : "+str(first)+" - "+str(first_occ))
            processed.append(request[x+1])
            second = request[x+1]
            second_occ = get_occurences(porter.stem(second))
            print("second : "+str(second)+" - "+str(second_occ))

            if (len(second_occ) > 0):
                if (len(first_occ) > 0):
                    if next(iter(first_occ.values())) > next(iter(second_occ.values())):
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
                    if next(iter(second_occ.values())) > next(iter(first_occ.values())):
                        for y in range(len(docs)):
                                if docs[y] < second_occ[y]:
                                    docs[y] = second_occ[y]
                else:
                    for y in range(len(docs)):
                        if y in first_occ:
                            if docs[y] < first_occ[y]:
                                docs[y] = first_occ[y]

       
    sorted_keys = sorted(docs, key=docs.get, reverse=True)
    for w in sorted_keys:
        docs_sorted[w] = docs[w]
    docs = docs_sorted
    print("docs : "+str(docs))
    
    keys = list(docs)
    key = keys[0]

    return key

#print(boolean_request("desease AND severe AND pneumonia"))
#print(boolean_request("NOT plasma AND risk of infection AND restrictions"))
#print(boolean_request("NOT covid-19"))
#print(boolean_request("covid-19 OR France"))
#print(boolean_request("covid-19 OR xxxx"))
#print(boolean_request("antimalarial drugs OR antiviral agents OR immunomodulators OR covid-19"))