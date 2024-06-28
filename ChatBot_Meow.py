def chatbot():
    print("Hello! I am a simple chatbot.")
    while True:
        user = input("You: ").strip().lower()
        
        if user in ["hi", "hello", "hey"]:
            print("Chatbot: Hello! How can I help you today?")
            
        elif user in ["how are you", "how are you doing"]:
            print("Chatbot: I'm a digital chatbot here to help you with your needs. I'm doing great! How about you?")
            
        elif user in ["what is your name", "who are you"]:
            print("Chatbot: I am a simple chatbot created to chat with you.")
            
        elif user in ["i am fine","i am good"]:
            print("Chatbot: Sounds good!")
         
        elif user in["Okay","ok","yes"]:
            print("Chatbot: Feel free to ask anything else :) ")
            
        elif user in ["bye", "goodbye", "exit"]:
            print("Chatbot: Okay. Goodbye! Have a great day!")
            break
            
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you ask something else?")


chatbot()
