#Team Crime 9/13
#Version 0.1

from CSVLogger import writeToCSV
import requests
from bs4 import BeautifulSoup

headers = {"user-agent" : "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36;", "from": "cmcgraw@email.davenport.edu"}
url = "https://data.grcity.us/Dispatch/Dispatched_Calls.html"

def scrapeDispatch(url):
	#page = the url request
	page = requests.get(url, headers = headers)
	pageContent = page.content
	soup = BeautifulSoup(pageContent, "html.parser")
	
	data = []

	headerContent = soup.find("table")
	table = headerContent.find_next("table").getText().splitlines()
	for line in table:
		if line != "" and line[0:4] != "Date":
			date = line[0:10]
			time = line[11:16]

			x = 16
			incident = ""
			while line[x].isalpha():
				incident = incident + line[x]
				x = x+1
			
			location = line[x:]

			data.append([date, time, incident, location])

	#TODO: fix assumtion that the first part of the location is a number

	writeToCSV(data)
	return data

scrapeDispatch(url)