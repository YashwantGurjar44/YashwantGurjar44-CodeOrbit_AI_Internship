def get_chatbot_response(user_input: str) -> str:
    normalized_input = user_input.lower().strip()
    
    intent_greetings = ["hello", "hi", "hey", "greetings"]
    intent_farewells = ["bye", "goodbye", "see you", "exit", "quit"]
    intent_help = ["help", "support", "assist"]
    intent_internship = ["internship", "codeorbit", "certificate", "task"]
    
    if any(word in normalized_input for word in intent_farewells):
        return "Goodbye! Have a great day ahead and happy coding!"
        
    elif any(word in normalized_input for word in intent_greetings):
        return "Hello! Welcome to the CodeOrbit Tech AI Assistant. How can I help you today?"
        
    elif any(word in normalized_input for word in intent_help):
        return "I can assist you with information regarding CodeOrbit Tech AI Internship tasks and guidelines."
                
    elif any(word in normalized_input for word in intent_internship):
        return "The CodeOrbit AI internship consists of 3 hands-on tasks: a Rule-based Chatbot, a Tic-Tac-Toe AI, and Image Classification."

    # Fallback response for unknown input
    else:
        return "I'm sorry, I didn't quite understand that. Could you please ask about greetings, help, or internship details?"

def chat_loop():
    print("=" * 50)
    print("CodeOrbit Tech Chatbot Initialized. Type 'quit' to exit.")
    print("=" * 50)
    
    while True:
        user_message = input("\nYou: ")
        if not user_message.strip():
            continue
            
        bot_response = get_chatbot_response(user_message)
        print(f"Bot: {bot_response}")
        
        if "Goodbye!" in bot_response:
            break

if __name__ == "__main__":
    chat_loop()
