# Hugo BERANGER - M2 MIAGE IA

import random
import re
import numpy as np

bot_template = "BOT : {0}"
user_template = "USER : {0}"

# Define variables
name = "Greg"
weather = "cloudy"

# Define a dictionary containing a list of responses for each message
responses = {'greet': 'Hello you! :)', 'goodbye': 'goodbye for now', 'thankyou': 'you are very welcome', 'default': 'default message', 'love' : 'I love you', 'angry': 'fuck you'}

rules = {'do you think (.*)': ['if {0}? Absolutely.', 'No chance'], 'do you remember (.*)': ['Did you think I would forget {0}', "Why haven't you been able to forget {0}", 'What about {0}', 'Yes .. and?'], 'I want (.*)': [
    'What would it mean if you got {0}', 'Why do you want {0}', "What's stopping you from getting {0}"], 'if (.*)': ["Do you really think it's likely that {0}", 'Do you wish that {0}', 'What do you think about {0}', 'Really--if {0}']}

keywords = {'greet': ['hello', 'hi', 'hey'], 'goodbye': ['bye', 'farewell'], 'thankyou': ['thank', 'thx']}

love_words = {"love": ["<3", " that's really kind", "you're full of kindness", "take care", "ily", "I love you", "that's so sweet", "I love you"]}
angry_words = {"angry": ["fuck","murder","mafia","kill","murderer"]}
love = 0
angry = 0

with open('numbers.txt', 'w') as handle:
    for n in np.arange(1, 100, 10):
        handle.write('{}\n'.format(n))

# Define a dictionary of patterns
patterns = {}
love_words_patterns = {}
angry_words_patterns = {}

# Iterate over the keywords dictionary
for intent, keys in keywords.items():
    # Create regular expressions and compile them into pattern objects
    patterns[intent] = re.compile('|'.join(keys))
    
# Iterate over the keywords dictionary
for intent, keys in love_words.items():
    # Create regular expressions and compile them into pattern objects
    love_words_patterns[intent] = re.compile('|'.join(keys))

# Iterate over the keywords dictionary
for intent, keys in angry_words.items():
    # Create regular expressions and compile them into pattern objects
    angry_words_patterns[intent] = re.compile('|'.join(keys))

def match_rule(rules, message):
    response, phrase = "default", None
    # Iterate over the rules dictionary
    for pattern, responses in rules.items():
        # Create a match object
        match = re.search(pattern, message)
        if match is not None:
            # Choose a random response
            response = random.choice(responses)
            if '{0}' in response:
                phrase = match.group(1)
    # Return the response and phrase
    return response.format(phrase)

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

# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))

def user_input():
    while(1):
        user_input = input("")
        print(user_template.format(user_input))
        response = respond(user_input)
        print(bot_template.format(response))

# Define find_name()
def find_name(message):
    name = None
    # Create a pattern for checking if the keywords occur
    name_keyword = re.compile('name|call')
    # Create a pattern for finding capitalized words
    name_pattern = re.compile('[A-Z]{1}[a-z]*')
    if name_keyword.search(message):
        # Get the matching words in the string
        name_words = name_pattern.findall(message)
        if len(name_words) > 0:
            # Return the name if the keywords are present
            name = ' '.join(name_words)
    return name

# Define a respond function
def respond(message):
    global love
    global angry
    # Call the match_intent function
    intent = match_intent(message)
    # Fall back to the default response
    key = "default"
    if intent == "love":
        love += 10
        angry -= 10
        print("love :",love)
        print("angry :",angry)
    elif intent == "angry":
        angry += 10
        love -= 10
        print("love :",love)
        print("angry :",angry)
    elif intent in responses:
        key = intent
    return responses[key]

# Send messages
# send_message("my name is David Copperfield")
# send_message("call me Ishmael")
# send_message("People call me Cassandra")

# Define a function to find the intent of a message
def match_intent(message):
    matched_intent = None
    
    for intent, pattern in patterns.items():
        # Check if the pattern occurs in the message 
        if pattern.search(message):
            matched_intent = intent
    
    for intent, pattern in love_words_patterns.items():
        # Check if the pattern occurs in the message 
        if pattern.search(message):
            matched_intent = intent
    
    for intent, pattern in angry_words_patterns.items():
        # Check if the pattern occurs in the message 
        if pattern.search(message):
            matched_intent = intent

    return matched_intent

# Test match_rule
# print(match_rule(rules, "do you remember your last birthday"))

user_input()