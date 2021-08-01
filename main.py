import random, hangman_art
from main_hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)
print(" \n", hangman_art.stages[lives])

display = []
for _ in range(word_length):
    display += "_"

print("Press ENTER to start")
while not end_of_game:
    guess = input("\nGuess a letter: ")
    if guess in display:
        print(f"\n{guess} was already chosen\n")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == "\'" or letter == '?' or letter == "-" or letter == " ":
            display[position] = letter
        if letter.lower() == guess.lower():
            display[position] = letter
    if guess.lower() not in chosen_word.lower():
        lives -= 1
        print(f"\n'{guess}' isn't included in the word.\n")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(hangman_art.logo)
    print(hangman_art.stages[lives])
    print(f"{' '.join(display)}")
print(f"\nThe answer was:\n{chosen_word}\n\n ")