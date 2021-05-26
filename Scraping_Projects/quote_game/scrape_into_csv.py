import requests
from bs4 import BeautifulSoup
from time import sleep 
from random import choice
from csv import DictWriter

base_url = "http://quotes.toscrape.com/"

def get_quotes():
	all_quotes = [] #init empty list
	author_url = "/page/1"

	# extract all info from every subpage 
	while author_url:
		res = requests.get(f"{base_url}{author_url}")
		print(f"Now Scraping {base_url}{author_url}...") # --------- delete
		soup = BeautifulSoup(res.text, "html.parser") 
		quotes = soup.find_all(class_ = "quote") # find all quotes

		# create dictionary and store quotes, authors and link to the author
		for quote in quotes:
			all_quotes.append({
			"text": quote.find(class_ = "text").get_text(),
			"author": quote.find(class_ = "author").get_text(),
			"link": quote.find("a")["href"]
			})

		next_btn = soup.find(class_ = "next") #find the button 'next' 
		author_url = next_btn.find("a")["href"] if next_btn else None #extract the link from the 'next' button
		sleep(1) # number of seconds b/n requests
	return all_quotes

quotes = get_quotes()
# write to csv file
with open("quotes.csv", "w") as file:
	headers = ["text","author","link"]
	csv_writer = DictWriter(file, fieldnames = headers)
	csv_writer.writeheader()
	for quote in quotes:
		csv_writer.writerow(quote)