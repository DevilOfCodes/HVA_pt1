import json
import random
import pyttsx3

def get_response(user_input):
    # Open the JSON file and load its contents into a dictionary
    with open('intents.json', 'r') as f:
        data = json.load(f)

    # Loop over each dictionary in the intents list and match the user's input with the patterns
    for intent in data['intents']:
        tag = intent['tag']
        patterns = intent['patterns']
        if user_input in patterns:
            # If the user's input matches a pattern, select a random response from the corresponding tag and return it
            responses = intent['responses']
            response = random.choice(responses)
            return response

    # If no pattern is found, return a default message
    return "I'm sorry, I don't understand."

def text_to_voice(text):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()
    eng = pyttsx3.init() #initialize an instance
    voice = eng.getProperty('voices')
    # Get the female voice
    eng.setProperty('voice', voice[1].id)

    # Set the properties for the speech
    engine.setProperty('rate', 150) # Speed of thespeech, in words per minute
    engine.setProperty('volume', 0.7) # Volume of the speech, between 0 and 1

    # Speak the text
    engine.say(text)
    engine.runAndWait()

# Greet the user and keep prompting the user for input until the user says "bye"
starting = 'Hi, how are you?'
text_to_voice(starting)
print("Karma: "+starting)

while True:
    user_input = input("you: ")
    if user_input.lower() == "bye":
        ending = "Happy to serve you"
        print("Karma: " + ending)
        text_to_voice(ending)
        break

    response = get_response(user_input)
    print("Karma: " + response)
    text_to_voice(response)