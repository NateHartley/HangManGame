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
guess_list = []

while wrong_guesses < 10:

    guess = str(input("Guess a letter: "))
    length = len(guess)

    if length == 1:  # if the length of the character is 1

        if guess in guess_list:  # if character has already been guessed before
            print("This letter has already been guessed ")

        else:  # if character has not already been guessed before
            guess_list = guess_list.append(guess)

            if guess in word:  # if the guessed character is in the word
                print(guess, "does appear in the word!")
                # word.split()??
                # print out set of ----- with length of word
                # if guess is in word, replace - with guess in same index as it occurs in word

            else:  # if the guessed character is not in the word
                print("Sorry, ", guess, " is not in the word.\n")
                print("You have", (9 - wrong_guesses), "wrong guesses remaining.")
                wrong_guesses = wrong_guesses + 1

    else:  # if the length of the character is not equal to 1
        print("--Please enter a single character--\n")

# while loop has stopped, maximum number of wrong guesses achieved
print("You ran out of guesses, you lose!")
