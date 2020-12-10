# Hugo BERANGER - M2 MIAGE IA

import random
import re
import numpy as np
import pandas as pd
from termcolor import colored, cprint

# Define variables
name = "Greg"
weather = "cloudy"

# Create templates
bot_template = "BOT : {0}"
user_template = "USER : {0}"

# Load CSV
data = pd.read_csv('SentiWordNet_3.0.0.txt', sep="\t", header=None, engine='python')

# Parry's current mood
parry_mood = 0

# Define the rules
rules = {'do you think (.*)': 
            ['if {0}? Absolutely.', 
            'No chance'],
        'do you remember (.*)': 
            ['Did you think I would forget {0}',
            "Why haven't you been able to forget {0}",
            'What about {0}', 'Yes .. and?'], 
        'I want (.*)': 
            ['What would it mean if you got {0}',
            'Why do you want {0}',
            "What's stopping you from getting {0}"], 
        'if (.*)': 
            ["Do you really think it's likely that {0}",
            'Do you wish that {0}',
            'What do you think about {0}',
            'Really--if {0}'],
        "what's your name?": 
            ["my name is {0}".format(name),
            "they call me {0}".format(name),
            "I go by {0}".format(name)],
        "what's today's weather?": 
            ["the weather is {0}".format(weather),
            "it's {0} today".format(weather)],
        'hello': 
            ['hello', 
            'hi', 
            'hey'], 
        'goodbye': 
            ['bye', 
            'farewell'], 
        'thank you': 
            ['thank', 
            'thx'],
        "default": 
            ["Ok"]
}

# Read SentiWord database
def senti_word():
    global data
    del data[0]
    del data[1]
    del data[5]
    for x in range(len(data)):
        data.at[x,4] = re.sub('#\d', '', data.at[x,4])  
        if data.at[x,2] > data.at[x,3]:
            data.at[x,2] = 1 
        elif data.at[x,2] == data.at[x,3]:
            data.at[x,2] = 0
        else:
            data.at[x,2] = -1
    del data[3]

# Define respond()
def respond(keywords, message):
    if parry_mood > 0:
        print("Parry's current mood is : ",end='')
        text = colored('Positive', 'green')
        print(text)
    elif parry_mood < 0:
        print("Parry's current mood is : ",end='')
        text = colored('Negative', 'red')
        print(text)
    else:
        print("Parry's current mood is : ",end='')
        text = colored('Neutral', 'blue')
        print(text)
    # Call match_rule
    response, phrase = match_rule(keywords,message)
    if '{0}' in response:
        # Replace the pronouns in the phrase
        phrase = replace_pronouns(phrase)
        # Include the phrase in the response
        response = response.format(phrase)
    return response

# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    message_tendency(message)
    # Get the bot's response to the message
    response = respond(rules, message)      
    # Print the bot template including the bot's response.
    print(bot_template.format(response))


# Define match_rule()
def match_rule(rules, message):
    response, phrase = "default", None
    # Iterate over the rules dictionary
    for pattern, responses in rules.items():
        # Create a match object
        match = re.search(pattern,message)
        if match is not None:
            # Choose a random response
            response = random.choice(responses)
            if '{0}' in response:
                phrase = match.group(1)
    # Return the response and phrase
    if response.format(phrase) == "default":
        response = random.choice(responses)

    return response.format(phrase), message


# Define replace_pronouns()
def replace_pronouns(message):
    message = message.lower()
    if 'me' in message:
        # Replace 'me' with 'you'
        return re.sub('me', 'you',message)
    if 'my' in message:
        # Replace 'my' with 'your'
        return re.sub('my','your',message)
    if 'your' in message:
        # Replace 'your' with 'my'
        return re.sub('your','my',message)
    if 'you' in message:
        # Replace 'you' with 'me'
        return re.sub('you','me',message)
    return message

def message_tendency(message):
    global data
    global parry_mood
    tendency = 0
    for x in range(len(data)):
        if data.at[x,4] in message:
            if data.at[x,2] == 1:
                parry_mood += 1
                tendency += 1
            elif data.at[x,2] == -1:
                parry_mood -=1
                tendency -= 1

    if tendency > 0:
        text = colored('^^^Positive message^^^', 'green')
        print(text)
    elif tendency < 0:
        text = colored('^^^Negative message^^^', 'red')
        print(text)
    else:
        text = colored('^^^Neutral message^^^', 'blue')
        print(text)

# Allow user to discuss with the bot
def user_input():
    while(1):
        user_input = input("")
        send_message(user_input)

senti_word()

# Rule test
send_message("hello")
send_message("what's your name?") 
send_message("what's today's weather?")
send_message("do you remember your last birthday")              
send_message("do you think humans should be worried about AI") 
send_message("I want a robot friend")
send_message("what if you could be anything you wanted")


# To test some questions
user_input()