import requests
from bs4 import BeautifulSoup


page = requests.get("https://en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser)")

soup = BeautifulSoup(page.text, "html.parser")
for anchor in soup.find_all('a'):
    print(anchor.get('href', '/'))
