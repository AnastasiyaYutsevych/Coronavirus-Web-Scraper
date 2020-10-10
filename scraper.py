import requests 
from bs4 import BeautifulSoup
from datetime import date,timedelta


country = input("Please enter your country: ").lower()
src = "https://www.worldometers.info/coronavirus/country/{}/".format(country)
result = requests.get(src)
src =result.content
yesterday = date.today() - timedelta(days=1)
d1 = "newsdate"+ yesterday.strftime("%Y-%m-%d")
soup = BeautifulSoup(src,'lxml')
error_found = False
try:
  li = soup.findAll("li", {"class":"news_li"})
  div = soup.findAll("div", {"class":"maincounter-number"})
  li = str(li).split(">")[2].split("new cases")
  div = str(div[0]).split("\n")[1].split(">")[1].split("<")
except:
    print("Oops it seems like the country you entered does not exist, please check your spelling and try again")
    error_found = True
if not error_found:
    print("Total number of cases is: ", div[0])
    print("New cases: " ,li[0])