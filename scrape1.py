from bs4 import BeautifulSoup 
import requests

html_text = requests.get('https://quotes.toscrape.com/').text

print(html_text)