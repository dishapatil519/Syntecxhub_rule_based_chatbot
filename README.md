# Syntecxhub_rule_based_chatbot
🤖 Rule-Based Conversational Chatbot

A simple console-based chatbot built using Python and pattern matching (Regular Expressions).
The bot supports basic intents, rule-based responses, a small knowledge base, and logs conversation history.

📌 Features

Intent detection (Greeting, Help, Small Talk, Exit)
Rule-based responses
Small domain knowledge base
Interactive console chat
Conversation history logging with timestamps
Lightweight and beginner-friendly

🧠 How It Works

The chatbot follows a simple rule-based NLP pipeline:
User enters input
Text is converted to lowercase
Intent is detected using Regular Expressions
Knowledge base is checked for domain-specific questions
Bot generates response
Conversation is saved to a log file

📂 Project Structure
chatbot-project/
│
├── task2.py
├── chat_log.txt
└── README.md
🚀 Installation

Make sure Python 3.x is installed.

No external libraries required (only built-in modules used):
re
datetime
Run the chatbot:
python task2.py
💬 Example Interaction
Bot: Hello! Type 'exit' to quit.

You: hi
Bot: Hello! How can I help you today?

You: what is python
Bot: Python is a high-level programming language.

You: how are you
Bot: I'm just a bot, but I'm doing great!

You: exit
Bot: Goodbye! Have a nice day.
📘 Supported Intents
Intent	Example Input
Greeting	hi, hello, hey
Help	help, assist
Small Talk	how are you
Exit	bye, exit, quit
📚 Knowledge Base

The chatbot can answer basic domain questions like:
What is Python?
What is AI?
What is Machine Learning?
Who developed Python?
You can easily expand the knowledge base by editing the dictionary in the code.

📝 Conversation Logging

All conversations are stored in:
chat_log.txt

Each message is saved with a timestamp for tracking and analysis.
Example log entry:

[2026-03-04 18:45:12] User: hi
[2026-03-04 18:45:12] Bot: Hello! How can I help you today?

🎓 Learning Objectives
This project demonstrates:
Basic Natural Language Processing (NLP)
Pattern matching using Regular Expressions
Rule-based chatbot design
File handling in Python
Intent classification logic

🔮 Future Improvements

Add GUI using Tkinter
Deploy using Flask (Web version)
Add Machine Learning-based intent classification
Store chat history in a database
Expand knowledge base

👨‍💻 Author
Disha Patil
