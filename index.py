import random

# function: to talk to user
# elements used: input, if/else

def main():
    chat_response = [
        "That is amazing to hear. Tell me more.",
        "Great news! What made your day great?", 
        "Wonderful, would you like to share more?"
    ]
    print('\nGreetings. What would you like to talk about?')
    print('1. Your day')
    print('2. Your hobby')
    print('3. Your pet')
    prompt = input(f"Enter choice here: ")

    if prompt == '1':
        userInput = input('How is your day going? ')
        if userInput.lower() == 'great':
            random_response = random.choice(chat_response)
            print(random_response)


if __name__ == __name__:
    main()

