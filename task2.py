import re
import datetime


knowledge_base = {
    "what is python": "Python is a high-level, interpreted programming language known for simplicity.",
    "what is ai": "Artificial Intelligence (AI) is the simulation of human intelligence in machines.",
    "what is machine learning": "Machine Learning is a subset of AI that allows systems to learn from data.",
    "who developed python": "Python was developed by Guido van Rossum in 1991."
}



patterns = {
    "greeting": r"\b(hi|hello|hey|good morning|good evening)\b",
    "help": r"\b(help|assist|support)\b",
    "smalltalk": r"\b(how are you|what's up|how is it going)\b",
    "exit": r"\b(exit|bye|quit)\b"
}


responses = {
    "greeting": "Hello! How can I help you today?",
    "help": "You can ask me about Python, AI, or Machine Learning.",
    "smalltalk": "I'm just a bot, but I'm doing great! ",
    "unknown": "Sorry, I don't understand that. Can you rephrase?"
}


def log_conversation(user_input, bot_response):
    with open("chat_log.txt", "a") as file:
        time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{time_stamp}] User: {user_input}\n")
        file.write(f"[{time_stamp}] Bot: {bot_response}\n\n")

def detect_intent(user_input):
    for intent, pattern in patterns.items():
        if re.search(pattern, user_input.lower()):
            return intent
    return None

def get_knowledge_response(user_input):
    user_input = user_input.lower()
    for question in knowledge_base:
        if question in user_input:
            return knowledge_base[question]
    return None



def chatbot():
    print("Bot: Hello! Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        # Detect Exit
        if detect_intent(user_input) == "exit":
            print("Bot: Goodbye! Have a nice day.")
            log_conversation(user_input, "Goodbye! Have a nice day.")
            break

        # Knowledge Base Check
        kb_response = get_knowledge_response(user_input)
        if kb_response:
            print("Bot:", kb_response)
            log_conversation(user_input, kb_response)
            continue

        # Intent Check
        intent = detect_intent(user_input)
        if intent:
            bot_response = responses[intent]
        else:
            bot_response = responses["unknown"]

        print("Bot:", bot_response)
        log_conversation(user_input, bot_response)



if __name__ == "__main__":
    chatbot()