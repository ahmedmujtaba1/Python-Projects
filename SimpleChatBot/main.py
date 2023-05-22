import random

# Define a list of predefined responses
responses = {
    "hello": ["Hello!", "Hi there!", "Greetings!"],
    "how are you": ["I'm good, thanks!", "I'm doing well!", "All is well!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "default": ["I'm sorry, I don't understand.", "Could you please rephrase that?", "I'm still learning!"]
}

# Function to return a response based on the user's input
def get_response(message):
    # Convert user's input to lowercase
    message = message.lower()

    # Check if the user's input matches any predefined responses
    for key in responses:
        if key in message:
            return random.choice(responses[key])

    # If no match is found, return a default response
    return random.choice(responses["default"])

# Main program loop
while True:
    # Get user's input
    user_input = input("User: ")

    # Get bot's response
    bot_response = get_response(user_input)

    # Print bot's response
    print("Bot:", bot_response)

    # Exit the loop if user says "bye"
    if "bye" in user_input.lower():
        break
