import random

responses = {
    "hello": [
        "Hello! How can I help you?",
        "Hi! Nice to meet you.",
        "Hey! How are you?"
    ],
    "how are you": [
        "I'm doing great! Thanks for asking.",
        "I'm fine and ready to chat!"
    ],
    "name": [
        "I'm a Basic AI Chatbot.",
        "You can call me ChatBot."
    ],
    "bye": [
        "Goodbye! Have a great day!",
        "Bye! See you again!"
    ]
}

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return random.choice(responses["hello"])

    elif "how are you" in user_input:
        return random.choice(responses["how are you"])

    elif "your name" in user_input or "who are you" in user_input:
        return random.choice(responses["name"])

    elif "bye" in user_input or "exit" in user_input:
        return random.choice(responses["bye"])

    else:
        return "Sorry, I don't understand that yet."


print("================================")
print("       BASIC AI CHATBOT")
print("================================")
print("Type 'bye' or 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    response = chatbot_response(user_input)
    print("Bot:", response)

    if "bye" in user_input.lower() or "exit" in user_input.lower():
        break