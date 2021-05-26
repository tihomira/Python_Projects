import sqlite3
import requests
from bs4 import BeautifulSoup


# scrape books 
def scrape_books(url):
	# Request url
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")
	books = soup.find_all("article") # extract artile class
	all_books = []
	for book in books:
		book_data = (get_title(book), get_price(book), get_rating(book))# create a tuple
		all_books.append(book_data) 
	save_books(all_books)


# scrape books to db
def save_books(all_books):
	# establish the connection to db and create table books
	connection = sqlite3.connect("books.db") 
	c = connection.cursor()
	# if the table already exists comment the line
	c.execute('''CREATE TABLE books 
		(title TEXT, price REAL, rating INTEGER)''')
	c.executemany("INSERT INTO books VALUES (?,?,?)", all_books) # insert data(all_books) into table
	connection.commit()
	connection.close()


# get title 
def get_title(book):
	return book.find("h3").find("a")["title"]


# get price
def get_price(book):
	price = book.select(".price_color")[0].get_text() # extract the price
	return float(price.replace("£","").replace("Â","")) # remove the symbols and covert to float


# get rating
def get_rating(book):
	# make a dict to map the words to number ratings
	ratings = {"Zero": 0, "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
	paragraph = book.select(".star-rating")[0]
	rating_word = paragraph.get_attribute_list("class")[-1]
	return ratings[rating_word] # map the integers to the words



scrape_books("http://books.toscrape.com/catalogue/category/books/history_32/index.html")





#print(books)
# Initialize BS
# Extract data we want
# Save data to database




# # unrefactored
# response = requests.get("http://books.toscrape.com/catalogue/category/books/history_32/index.html")
# soup = BeautifulSoup(response.text, "html.parser")
# books = soup.find_all("article")
# for book in books:
# 	title = book.find("h3").find("a")["title"]
# 	price = book.select(".price_color")[0].get_text()
# 	price = float(price.replace("£","").replace("Â",""))
# 	# make a dict to map the words to number ratings
# 	ratings = {"Zero": 0, "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
# 	paragraph = book.select(".star-rating")[0]
# 	rating = paragraph.get_attribute_list("class")[-1]
# 	int_rating = ratings[rating]
# 	print(int_rating)

