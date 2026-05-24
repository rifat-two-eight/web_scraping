import sys
import requests
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

url = "https://quotes.toscrape.com"

response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

print(soup.title.text)