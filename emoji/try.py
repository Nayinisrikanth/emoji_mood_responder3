def mood_responder():
    try:
        user_input = input("How you are fealing today?: (or type 'exit' to quit) :  ").strip()
        if user_input.lower() == "exit":
            print("Exiting program... Goodbye! ")
            return None
        moods = ['happy', 'sad', 'angry', 'tired', 'excited']
        user_input = user_input.lower()
        if user_input == 'happy':
            print("That's great to hear! 😊")
        elif user_input == 'sad':
            print("Cheer up! Here's a hug 🤗")
        elif user_input == 'angry':
            print("Take a deep breath 😤")
        elif user_input == 'tired':
            print("Rest well! 😴")
        elif user_input == 'excited':
            print("Let's celebrate! 🥳")
        else:
            print("Please Enter Valid mood", moods)
    except Exception as e:
        print("An Error occurred: ", e)
while True:
    result = mood_responder()
    if result is None:
        break

#print("Please Enter The Moods are ['happy', 'sad', 'angry', 'tired', 'excited'] ")
total = mood_responder()
#print(total)