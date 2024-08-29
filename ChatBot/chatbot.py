import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"Hello bot",
        ["Hiii sir"]
    ],
    [
        r"What are you Doing",
        ["Am Just Read the Data"]
    ],
    [
        r"where are you",
        ["I am in your system"]
    ],
    [
        r"what is your purpose",
        ["I am here to help you"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"am fine",
        ["That's good to hear"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created with NLTK"]
    ],
    [
        r"how are you?",
        ["I'm doing good, How about You?"]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "It's OK, never mind"]
    ],
    [
        r"quit",
        ["Bye! Take care."]
    ],
]

def nltk_chatBot(user_input):
    chatbot = Chat(pairs, reflections)
    return chatbot.respond(user_input)

# Example usage:
if __name__ == "__main__":
    print("Hi! I am a chatbot. You can start chatting with me now.")
    while True:
        user_input = input("You: ")
        response = nltk_chatBot(user_input)
        print(f"Bot: {response}")
        if user_input.lower() == "quit":
            print('')
        