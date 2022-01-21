word = str(input("Enter a word for the other player to guess: "))
for i in range(1, 15):
    print('\n')


wrong_guesses = 0
guess_list = []
word = list(dict.fromkeys(word))  # removes the duplicate letters from the word
word_list = []

while wrong_guesses < 10:

    guess = str(input("Guess a letter: "))
    length = len(guess)

    if length == 1:  # if the length of the character is 1

        if guess in guess_list:  # if character has already been guessed before
            print("This letter has already been guessed ")
            print(guess_list)

        else:  # if character has not already been guessed before
            guess_list.append(guess)  # just fyi, this cant be guess_list = guess_list.append(guess), as it turns the list into a None type

            if guess in word:  # if the guessed character is in the word
                print(guess, "does appear in the word!")
                for i in word:
                    word_list.append(i)
                word_list = list(dict.fromkeys(word_list))
                print(word_list)
                print(guess_list)
                if word_list in guess_list:
                    print('You have guessed all the correct letters! The word was ',word)
                    break

            else:  # if the guessed character is not in the word
                print("Sorry, ", guess, " is not in the word.\n")
                print("You have", (9 - wrong_guesses), "wrong guesses remaining.")
                wrong_guesses = wrong_guesses + 1

    else:  # if the length of the character is not equal to 1
        print("--Please enter a single character--\n")

# while loop has stopped, maximum number of wrong guesses achieved
print("You ran out of guesses, you lose!")
