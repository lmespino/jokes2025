


# # make this performance task ready for submission
# # To give the user a fun experience hearing knock knock jokes

# joke = input("Do you want to hear a joke? ")
# if joke == "no":
#     print("Okay suit yourself!")
# while joke == "yes":
#     print("Great, Let's Play")
#     question = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
#     if question == "robbers":
#         input("Knock Knock ")
#         input("Calder")
#         print("Calder police - I've been robbed!")
#         joke = input("Do you want to hear another joke or are you finished? ")
#     elif question == "tanks":
#         input("Knock Knock ")
#         input("Tank ")
#         input("You are welcome! ")
#         joke = input("Do you want to hear another joke or are you finished? ")
#     elif question == "pencils":
#         input("Knock Knock ")
#         input("Broken pencil ")
#         input("Nevermind, it's pointless! ")
#         joke = input("Do you want to hear another joke or are you finished? ")
# if joke == "finished":
#     rate = int(input("Please rate our game 1-10! "))
#     final_score = int(rate * 10)
#     print(str(final_score) + " percent satisfaction rate")
#     friend = input("Would you recommend this game to a friend? ")

#     if friend == "yes" or friend == "maybe":
#         print("Thanks, we appreciate it. ")
#     else:
#         print("Sorry you did not enjoy it. ")



# Function to display the satisfaction rate based on user input
def satisfaction_rate(rate):
    final_score = int(rate * 10)
    print(f"{final_score} percent satisfaction rate")

# Function to ask for another joke
def ask_another_joke():
    return input("Do you want to hear another joke or are you finished? ").lower()

# Function to tell a specific joke
def tell_jokes(joke):
    if joke == "robbers":
        input("Knock Knock ")
        input("Calder ")
        print("Calder police - I've been robbed!")
    elif joke == "tanks":
        input("Knock Knock ")
        input("Tank ")
        print("You are welcome!")
    elif joke == "pencils":
        input("Knock Knock ")
        input("Broken pencil ")
        print("Nevermind, it's pointless!")

# Function to start the joke game
def start_joke_game():
    # Initial user input
    joke = input("Do you want to hear a joke? ").lower()
    
    # Ends the game here if user says no
    if joke == "no":
        print("Okay suit yourself!")
        return
    
    # The list of jokes in the game
    all_jokes = ["robbers", "tanks", "pencils"]

    # Iteration for repeating the joke game
    # If the user says yes for jokes, it asks them what joke they would like to hear
    while joke == "yes":
        print("Great, Let's Play")
        question = input(f"Do you want to hear a joke about {', '.join(all_jokes)}? ").lower()

        # Call the function to tell a joke
        tell_jokes(question)

        # Ask if the user wants to hear another joke
        joke = ask_another_joke()

    # After the user has decided to finish the jokes, they can rate it
    if joke == "finished" or joke == "finish":
        rate = int(input("Please rate our game 1-10! "))
        satisfaction_rate(rate)

        friend = input("Would you recommend this game to a friend? ").lower() # Question the user if they would recommend this game to a friend

        if friend == "yes" or friend == "maybe":
            print("Thanks, we appreciate it.")
        else:                                    # The yes/no results to recommending
            print("Sorry you did not enjoy it.")

# Call to start the jokes function
start_joke_game()