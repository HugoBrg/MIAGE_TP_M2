# Hugo BERANGER - M2 MIAGE IA

import random
import re
import numpy as np

# Define variables
name = "Greg"
weather = "cloudy"

# Create templates
bot_template = "BOT : {0}"
user_template = "USER : {0}"

# Mental state level
previous_mental_state_level = 0
mental_state_level = 0

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

mental_state_keywords = {
        'suicide':
            ["I'm here for you",
            "Are you all right?",
            "How can I help you?",
            "You can talk to me about anything!"],
        'murder':
            ["You're starting to scare me",
            "You're going to need more sessions",
            "This is really concerning"],
        'death':
            ["I'm here for you",
            "Are you all right?",
            "How can I help you?",
            "You can talk to me about anything!"],
        'alone':
            ["I'm here for you",
            "Are you all right?",
            "How can I help you?",
            "You can talk to me about anything!"],
        'kill': 
            ["You're starting to scare me",
            "Are you all right?"],
        "default": 
            ["No matter what's going through your mind I'll be there",
            "You sure you want to change the subject",
            "I'm still concerned about what you said !"]
}


# Define respond()
def respond(keywords, message):
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
    global previous_mental_state_level
    global mental_state_level
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    print("Current mental state  : ",mental_state_level)
    if mental_state(message) > 20:
        print("~~ the patient is not in a good state ~~")
        response = respond(mental_state_keywords, message) 
        previous_mental_state_level = mental_state_level
    else:
        response = respond(rules, message)
    
    if previous_mental_state_level == mental_state_level and mental_state_level != 0:
        mental_state_level -= 10
        previous_mental_state_level = mental_state_level
        
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


# Check mental state
def mental_state(message):
    global mental_state_level
    for keyword in mental_state_keywords:
        if keyword in message:
            mental_state_level += 10
    return mental_state_level

# Allow user to discuss with the bot
def user_input():
    while(1):
        user_input = input("")
        send_message(user_input)

# Rule test
send_message("Hello")
send_message("what's your name?") 
send_message("what's today's weather?")
send_message("do you remember your last birthday")              
send_message("do you think humans should be worried about AI") 
send_message("I want a robot friend")
send_message("what if you could be anything you wanted")

# Declining mental status
send_message("I'm about to kill myself")
send_message("I want to murder someone!")
send_message("Maybe I will die alone")
send_message("I will suicide")

# The patient is stable again
send_message("goodbye")
send_message("I said goodbye")

# To test some questions
user_input()