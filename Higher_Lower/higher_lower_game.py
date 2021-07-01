# Display art
import art
import random
from game_data import data
from replit import clear
print(art.logo)

# Format the account data into printable format.
def format_account(indx):
	name = data[indx]["name"]
	follower_count = data[indx]["follower_count"]
	description = data[indx]["description"]
	country = data[indx]["country"]

	return f"{name}, {description}, from {country}, ((((FOLLOWERS: {follower_count}))))." 


# Compare accounts:
def comapre_accounts(indx_a,indx_b):
	follower_count_a = data[indx_a]["follower_count"]
	follower_count_b = data[indx_b]["follower_count"]
	if follower_count_a > follower_count_b:
		return "A"
	else:
		return "B"




def game():
	# Generate a random account from the game data
	n_a = random.randint(0,len(data)-1)
	n_b = random.choice([i for i in range(0,49) if i != n_a])

	end_game = False
	score = 0


	while not end_game:
		# Ask user for a guess
		print(f"Compare A: {format_account(n_a)}")
		print(art.vs)
		print(f"Against B: {format_account(n_b)}")

		guess = input("Who has more followers? 'A' or 'B': ").upper()
		answer = comapre_accounts(n_a, n_b)

		clear()
		print(art.logo)

		# Check if user is correct
		if guess == answer:
			score +=1
			print(f"You are right! Your current score is {score}.")
			# Making account at postition B come the next account at position A
			if guess == "A":
				n_b = random.choice([i for i in range(0,49) if i != n_a])
			elif guess == "B":
				n_a = n_b
				n_b = random.choice([i for i in range(0,49) if i != n_a])
		else:
			print(f"Sorry you are wrong. Your final score is {score}")
			end_game = True


game()

# Clear the screen