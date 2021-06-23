import random
import hangman_art
from hangman_words import word_list

print(hangman_art.logo)
chosen_word = random.choice(word_list)
# print(chosen_word)
word_len = len(chosen_word)
end_of_game = False
lives = 6


# Create blanks
display = list("_") * word_len

while not end_of_game:
  usr_input = input("Guess a letter? ").lower()

  # If the user has entered a letter they've already guessed, print the letter and let them know.
  if usr_input in display:
    print(f"You've already guessed the letter '{usr_input}'.")

  # Check guessed letter
  for position in range(word_len):
    letter = chosen_word[position]
    if letter == usr_input:
      display[position] = letter
      

  # Check if user is wrong
  if usr_input not in chosen_word:
    # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    print(f"You guessed '{usr_input}' that's not in the word. You loose a life.")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You loose!")

  print(f"Remaining lives: {lives}")

  # Join all elements in the list
  print(f"{' '.join(display)}")


  # Check if user has got all letters correct:
  if "_" not in display:
    end_of_game = True
    print("You win!")

  # Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
  print(hangman_art.stages[lives])






