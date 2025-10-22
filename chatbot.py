import random

def chatbot_reply(user_input):
    user_input = user_input.lower().strip()

    # Keyword-based matching
    if any(word in user_input for word in ["hello", "hi", "hey"]):
        return random.choice(["Hi!", "Hello there!", "Hey!", "Nice to see you!", "Hi friend 👋"])
    
    elif "how are" in user_input:
        return random.choice([
            "I'm fine, thanks!", 
            "Doing great, how about you?", 
            "All good!", 
            "I’m always happy to chat 😊",
            "Better now that you’re here!"
        ])

    elif any(word in user_input for word in ["name", "who are you"]):
        return random.choice([
            "I'm ChatBot 🤖", 
            "You can call me Bot!", 
            "I’m your friendly chatbot.", 
            "I don’t have a fancy name, just Bot!"
        ])

    elif any(word in user_input for word in ["bye", "goodbye", "see you", "exit"]):
        return random.choice([
            "Goodbye!", 
            "See you soon!", 
            "Bye! Take care.", 
            "Talk to you later!", 
            "Have a great day!"
        ])

    elif any(word in user_input for word in ["thanks", "thank"]):
        return random.choice([
            "You're welcome!", 
            "No problem!", 
            "Glad to help!", 
            "Anytime 😊"
        ])

    elif "weather" in user_input:
        return random.choice([
            "I can’t check the weather right now, but I hope it’s sunny 🌞",
            "Looks like a great day to smile 😊",
            "It might rain happiness today 🌧️✨"
        ])

    elif "joke" in user_input:
        return random.choice([
            "Why don’t programmers like nature? Too many bugs 🐞😂",
            "What do you call a fake noodle? An Impasta 🍝",
            "Why did the computer go to the doctor? Because it caught a virus 💻🤒",
            "I told my code a joke… but it didn’t execute 😅"
        ])

    else:
        return "Sorry, I don't understand that."

def main():
    print("Welcome to Smarter Chatbot! (Type 'bye' to exit)")
    
    while True:
        user_message = input("You: ")
        reply = chatbot_reply(user_message)
        print("Bot:", reply)
        
        if "bye" in user_message.lower() or "exit" in user_message.lower():
            break

if __name__ == "__main__":
    main()
