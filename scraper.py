# imports
import requests
import bs4
ask_page = input('what page: ')
site = 'https://www.hcrealms.com/forum/units/units_bbcode.php?id=bm058'

# definitions
page = requests.get(str(site+ask_page))

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())




print(page.status_code)
input("googbye cruel world!")
