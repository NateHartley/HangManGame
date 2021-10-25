word = str(input("Enter a word for the other player to guess: "))
print("\n"
      "\n"
      "\n"
      "\n"
      "\n"
      "\n"
      "\n"
      "\n"
      "\n"
      "\n"
      "\n"
      "\n"
      "\n"
      "\n")

wrong_guesses = 0

while wrong_guesses < 10:

    guess = str(input("Guess a letter: "))
    length = len(guess)
    guess_list = []

    if length == 1:  # if the length of the character is 1

        # if guess has already been guessed
        # need to add guesses to a list
        # everytime a letter is guessed, scan through list to see if it appears
        # append list if not already in it

        if guess in word:  # if the guessed character is in the word
            print(guess, "is in the word!")

        else:  # if the guessed character is not in the word
            print("Sorry, ", guess, " is not in the word.\n")
            print("You have", (9 - wrong_guesses), "wrong guesses remaining.")
            wrong_guesses = wrong_guesses + 1

    else:  # if the length of the character is not equal to 1
        print("--Please enter a single character--\n")

# while loop has stopped, maximum number of wrong guesses achieved
print("You ran out of guesses, you lose!")
