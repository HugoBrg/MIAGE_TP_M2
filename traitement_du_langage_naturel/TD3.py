import xml.etree.ElementTree as ET
import nltk

tree = ET.parse('questions.xml')
root = tree.getroot()

questions_answers = [[]]
answers = []

dataset = root.findall('.//question')

for question in dataset:
    questions_answers.append(question.find('string').text)
    #print(question.find('string').text)

    answers = root.findall('.//answers')
    for answer in answers:
        
        answerTypes = root.findall('.//answer')
        for answerType in answerTypes:
            answer = answerType.find("*").text
            #print(answer)

for item in questions_answers:
    print(item[0])
    #text = nltk.word_tokenize(item[0])
    