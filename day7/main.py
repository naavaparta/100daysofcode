import random
import hangman_art
import hangman_words

# choose a word, assign to chosen_word
chosen_word = random.choice(hangman_words.word_list)

# display logo
print(hangman_art.logo)

# for testing purposes only, commented out for gaming purposes
# print(f"The solution is {chosen_word}.")

# lives are six
lives = 6

# display list
display = len(chosen_word) * ["_"]

# initialize end to false to allow for looping
end = False

# game loop
while not end:
    # ask for a guess and make it lowercase
    guess = input("Guess a letter! ").lower()

    if guess in display:
        print(f"You guessed {guess} but you've already guessed it. No lives deducted. Choose another letter!")

    # check guessed letter
    for position in range(0, len(display)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(f"You guessed {guess} and it's in the word! Good job. Now continue!")

    # if wrong guess
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess} but it's not in the word. You have {lives} lives left.")
        # losing notification
        if lives == 0:
            end = True
            print("You lose!")

    print(f"{' '.join(display)}")
    # flip the switch, end of game is true, looping stops
    if "_" not in display:
        end = True
        print("You win!")

    print(hangman_art.stages[lives])