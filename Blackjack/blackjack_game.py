import random
from blackjack_art import logo

# --------- deal_card() -------------- #
def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return int(card)



# --------- calculate_score() -------------- #
def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  
  # Check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if sum(cards) == 21 and len(cards) == 2:
    return 0

  # Check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)



# --------- compare_score() -------------- #
# If the computer and user both have the same score, then it's a draw. 
# If the computer has a blackjack (0), then the user loses. 
# If the user has a blackjack (0), then the user wins. 
# If the user_score is over 21, then the user loses. 
# If the computer_score is over 21, then the computer loses. 
# If none of the above, then the player with the highest score wins.
def compare_score(user_score, computer_score):

  if user_score > 21 and computer_score > 21:
    return "You went over. You loose."

  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "You loose. Opponent has Blackjack."
  elif user_score == 0:
    return "You have a Blackjack. You win."
  elif user_score > 21:
    return "You went over. You loose."
  elif computer_score > 21:
    return "Oponent went over. You win."
  elif user_score > computer_score:
    return "You win."
  else:
    return "You loose."




# --------- play_game() -------------- #
def play_game():
  print(logo)

  user_cards = []
  computer_cards = []
  game_over = False


  # Deal the user and computer 2 cards each using deal_card()
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not game_over:
    # Call calculate_score(). 
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")      

    # End game if user or computer wins.
    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:
      # Continue game
      deal_user = input("Type 'y' to get another card, type 'n' to pass: ")
      if deal_user == 'y':
        user_cards.append(deal_card())
      else:
        game_over = True

  # Set computer strategy
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare_score(user_score, computer_score))


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Play game!
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  play_game()






