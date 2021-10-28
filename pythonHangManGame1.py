# Create a hangman game and allow the user to guess letters


import random


def main():
    # Create a list of words to choose from
    word_list = ["fraud", "collusion","sybil","moloch","ethbot","cheating","deception","complicity","comspiracy","ethereum","blockchain"]

    # Choose a random word from the list
    word = random.choice(word_list)

    # Create an empty list to store the letters of the word
    word_list = []

    # Create a list of letters in the word
    for letter in word:
        word_list.append(letter)

    # Create a list of letters that have been guessed
    guessed_letters = []

    # Create a list of letters that have not been guessed
    unguessed_letters = []

    # Create a list of underscores corresponding to the letters in the word
    for letter in word:
        unguessed_letters.append("_")

    # Print the word
    print(" ".join(unguessed_letters))

    # Create a variable to track the number of guesses
    guesses = 0

    # Create a while loop to continue until the user guesses all the letters
    while unguessed_letters != word_list:
        # Get the user's guess
        guess = input("Guess a letter: ")

        # Check if the user has guessed the letter
        if guess in guessed_letters:
            print("You already guessed that letter")
        else:
            # Add the letter to the list of guessed letters
            guessed_letters.append(guess)

            # Check if the letter is in the word
            if guess in word_list:
                # If the letter is in the word, replace the underscore with the letter
                for i in range(len(word_list)):
                    if guess == word_list[i]:
                        unguessed_letters[i] = guess
            else:
                # If the letter is not in the word, add one to the number of guesses
                guesses += 1

        # Print the word
        print(" ".join(unguessed_letters))

    # Check if the user won or lost
    if guesses == 6:
        print("You lost!")
    else:
        print("You won!")


if __name__ == "__main__":
    main()





