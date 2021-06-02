import requests
from bs4 import BeautifulSoup
from csv import DictWriter
from time import sleep


def get_at_holidays():
	base_url = "https://zentrum-online.at/gesetzliche-feiertage-oesterreich-2018/"
	holidays = []

	while base_url:
		response = requests.get(base_url)
		print(f"Now Scraping {base_url} .... ")
		soup = BeautifulSoup(response.text,"html.parser")
		days = soup.find_all("tbody")

		for day in days:
			for i in range(0,len(day.select(".column-2"))):
				holidays.append({ 
					"date": day.select(".column-2")[i].get_text() + base_url[-5:-1],
					"name": day.select(".column-3")[i].get_text()
				})
			if int(base_url[-5:-1])==2020:
				next_year=soup.find_all('div', attrs={'style': 'text-align: right;'})[1]
				# base_url = next_year.find("a")["href"] if next_year else None
			else:
				next_year = soup.find('div', attrs={'style': 'text-align: right;'})
			base_url = next_year.find("a")["href"] if next_year else None
			sleep(2)

	return holidays

holidays = get_at_holidays()
print(holidays)

# write holidays to csv file
with open("holidays.csv","w") as csv_file:
	headers = ["date","name"]
	csv_writer = DictWriter(csv_file, fieldnames = headers)
	csv_writer.writeheader()
	for holiday in holidays:
		csv_writer.writerow(holiday)













