import html
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen ("http://www.pythonscraping.com/pages/page1.html")
soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())