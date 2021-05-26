# Web Scraping Project
# Introduction
# In this project you'll be building a quotes guessing game. When run, your program will scrape a website for a collection of quotes. Pick one at random and display it. The player will have four chances to guess who said the quote. After every wrong guess they'll get a hint about the author's identity.

# Requirements
# Create a file called `scraping_project.py` which, when run, grabs data on every quote from the website http://quotes.toscrape.com
# You can use `bs4` and `requests` to get the data. For each quote you should grab the text of the quote, the name of the person who said the quote, and the href of the link to the person's bio. Store all of this information in a list.
# Next, display the quote to the user and ask who said it. The player will have four guesses remaining.
# After each incorrect guess, the number of guesses remaining will decrement. If the player gets to zero guesses without identifying the author, the player loses and the game ends. If the player correctly identifies the author, the player wins!
# After every incorrect guess, the player receives a hint about the author. 
# For the first hint, make another request to the author's bio page (this is why we originally scrape this data), and tell the player the author's birth date and location.
# The next two hints are up to you! Some ideas: the first letter of the author's first name, the first letter of the author's last name, the number of letters in one of the names, etc.
# When the game is over, ask the player if they want to play again. If yes, restart the game with a new quote. If no, the program is complete.

import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader

base_url = "http://quotes.toscrape.com/"


def read_quotes(filename):
	with open(filename, "r") as file:
		csv_reader = DictReader(file)
		return list(csv_reader)
		


def start_game(quotes):
	# set variables
	quote = choice(quotes)
	remaining_quesses = 4
	print("Here's a quote:")
	print(quote["text"])
	#print(quote["author"])
	quess = ''

	# begin a while loop with hint suggestions when answer is wrong
	while quess.lower() != quote["author"].lower() and remaining_quesses > 0:
		quess = input(f"Who said this quote? Guesses remaining: {remaining_quesses} ")
		# exit loop if correct answer
		if quess.lower() == quote["author"].lower():
			print("Correct!")
			break
		# decrease remaining number of quesses
		remaining_quesses -=1

		# set conditions on remaining quesses by giving different hints
		if remaining_quesses == 3:
			# extract necessary hint from csv file
			res = requests.get(f"{base_url}{quote['link']}")
			soup = BeautifulSoup(res.text, "html.parser")
			birth_date = soup.find(class_ = "author-born-date").get_text()
			birth_place = soup.find(class_ = "author-born-location").get_text()
			print(f"Here's a hint: The author was born on {birth_date} {birth_place}")

		elif remaining_quesses == 2:
			print(f"Here's a hint: the author's first name starts with: {quote['author'][0]}")

		elif remaining_quesses == 1:
			last_name_initial = quote["author"].split(" ")[1][0]
			print(f"Here's a hint: the author's last name starts with: {last_name_initial}")

		else:
			print(f"Sorry you ran out of quesses. The answer was {quote['author']}")




	# prompt to play or to quit
	again = ''
	while again.lower() not in ('y','yes','n','no'):
		again = input("Would you like to play again (y/n)? ")
	if again.lower() in ('y','yes'):
		print("Play again!")
		return start_game(quotes)
	else:
		print("Ok, goodbye!")
	



# start game
quotes = read_quotes("quotes.csv")
start_game(quotes)








