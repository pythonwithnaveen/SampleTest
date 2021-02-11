
import requests
from bs4 import BeautifulSoup

res = requests.request("GET","https://www.timeanddate.com/worldclock/india")

bs = BeautifulSoup(res.text,"html.parser")

text = bs.find("span",{"id":"ctdat"}).text

print(text)
