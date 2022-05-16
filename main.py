import random

# Adding a do-while loop
play_again = 'n'
while True:
    # All variables declared
    guess_num = random.randint(0, 100)
    hearts = ""
    user_heart_count = int(1)

    # Making a difficulty selector
    print("HI!, Select a difficulty: \n1)Hard - 3 hearts\n2)Normal - 5 hearts\n3)Easy 10 hearts")
    selector = int(input("The choices are ---> \n1 - hard\n2 - normal\n3 - easy\nMake a selection: "))
    if selector == 1:
        hearts = int(3)
    elif selector == 2:
        hearts = int(5)
    elif selector == 3:
        hearts = int(10)
    else:
        # Exiting the program if the user selects beside 1 2 or 3
        print("Error, This is not a choice.\nThe choices are ---> \n1 - hard\n2 - normal\n3 - easy")
        exit()

    # Gives the user numbers to guess between ( hint )
    print("Enter a number between 0 and 100")

    # Code for guessing game
    user_guess = int(input("Guess a number: "))
    while user_guess != guess_num and user_heart_count <= hearts:
        print("Guess again")
        print("Your hearts are at " + str(user_heart_count))
        user_guess = int(input("Enter a number: "))
        user_heart_count += 1
        if user_guess < guess_num:
            print("Too low, guess higher!")
        elif user_guess > guess_num:
            print("Too high, guess lower!")

    if user_guess == guess_num:
        print("You win \nThe number is " + str(guess_num))
    else:
        print("You lose :(\nThe number was " + str(guess_num))
    user_answer = input("Would you like to play again(please type 'y' to play again or 'n' to stop: ")

    if user_answer == play_again:
        break


print("\nThanks for playing!")
