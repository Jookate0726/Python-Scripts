import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/"
r = requests.get(url)
s = BeautifulSoup(r.text, "html.parser")
data = s.find_all("div", class_ = "maincounter-number")
data_active = s.find_all("div", class_ = "number-table-main")

print("\n--- COVID-19 LIVE STATS ---")
print("Total Cases: ", data[0].text.strip())
print("Total Deaths: ", data[1].text.strip())
print("Total Recovered: ", data[2].text.strip())
print("Total Active Cases: ", data_active[0].text.strip())
print("Total Closed Cases: ", data_active[1].text.strip())