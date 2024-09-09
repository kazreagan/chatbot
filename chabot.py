import random
#create a dictionary to hold the possible responses of the bot

resp = {
    "hello": "Hello there! How may I help you today?",
    "hi": "Hi there! What can I do for you today?",
    "hey": "Hey, How is going?",
    "bye": "Goodbye! Have a nice time.",
    "how are you": "I'm just a program, but I am doing well.",
    "who created you": "I was created by a developer called Reagan who has mad love for Python.",
    "what is your name": "My name is Raah.",
    "what can you do": "I can chat, answer simple questions, try asking me something.",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "thank you": "You're welcome! I'm here if you need any assistance.",
    "what is your purpose": "My purpose is to assist you and make your day a little brighter!",
    "what's the weather": "I'm not equipped with weather data yet, but you can always check your local forecast!",
    "where are you from": "I'm from the digital realm, created to live in the cloud.",
    "what's your favorite color": "As a bot, I don't see colors, but I think blue is quite popular!",
    "tell me something interesting": "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!",
    "how old are you": "Age is just a number, but I'm as young as the code that created me!",
    "default": "Sorry, I didn't understand that."
}

#create an input function

def get_response(user_input):
    user_input = user_input.lower().strip()
    return resp.get(user_input, resp["default"])

#create a loop to interact with the user

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Raah: Goodbye!")
        break
    print(f"Raah: {get_response(user_input)}")