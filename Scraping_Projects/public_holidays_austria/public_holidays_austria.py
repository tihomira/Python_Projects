import requests
from bs4 import BeautifulSoup
from csv import writer

base_url = "http://zentrum-online.at/gesetzliche-feiertage-oesterreich-2018"

response = requests.get(base_url)
#print(response.text)
soup = BeautifulSoup(response.text,"html.parser")
days = soup.find_all("tbody")

with open("holidays.csv","w") as csv_file:
	csv_writer = writer(csv_file)
	csv_writer.writerow(["date","name"])

# holidays = []
	for day in days:
		for i in range(0,len(day.select(".column-2"))):
			# holidays.append(day.select(".column-2")[i].get_text() + base_url[-4:])
			date = day.select(".column-2")[i].get_text() + base_url[-4:]
			name = day.select(".column-3")[i].get_text()
			csv_writer.writerow([date, name])
			# print(date,name)


