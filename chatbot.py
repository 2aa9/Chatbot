import random

responses = {
    "hi": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "how are you": ["I'm good, thanks!", "Doing well, and you?"],
    "bye": ["Goodbye!", "See you later!", "Bye!"]
}

def get_response(message):
    message = message.lower()
    for key in responses:
        if key in message:
            return random.choice(responses[key])
    return "I'm not sure how to respond to that."

if __name__ == "__main__":
    print("🤖 Chatbot (type 'bye' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        print("Chatbot:", get_response(user_input))
