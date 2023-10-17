import nltk
from nltk.chat.util import Chat, reflections

patterns = [
    (r'hi|hello|hey', ['Hi there!', 'Hello!', 'Hey!']),
    (r'how are you', ['I am good, thank you.', 'Fine, thanks.']),
    (r'what is your name', ['I am a chatbot. You can call me ChatGPT.']),
]
patterns += [
    (r'good morning|good afternoon|good evening', ['Good morning!', 'Good afternoon!', 'Good evening!']),
    (r'how are you', ['I am doing well, thanks!', "I'm great, how about you?"]),
    (r'what do you do', ["I'm a chatbot here to assist and chat with you."]),
    (r'tell me a joke|say something funny', ['Why don’t scientists trust atoms? Because they make up everything!']),
    (r'who created you', ['I was created by a developer using Python.']),
    (r'what is the time', ["I don't have the ability to tell time."]),
    (r'bye|goodbye', ['Goodbye!', 'See you later!']),
]
Kate=Chat(patterns,reflections)
def start_chat():
    print("Hi, I'm your chatbot, Kate . To exit type 'bye'")
    while True:
        user_input=input("Me: ")
        if user_input.lower()=="bye":
            print("Kate: Goodbye!")
            break
        else:
            respose=Kate.respond(user_input)
            print(f"Kate: {respose}")

if __name__=="__main__":
    start_chat()
