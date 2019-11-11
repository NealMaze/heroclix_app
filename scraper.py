# imports
import requests
import bs4
from bs4 import BeautifulSoup

# definitions
site = 'https://www.hcrealms.com/forum/units/units_bbcode.php?id='
ask_page = 'no'


page = requests.get(
    'https://www.hcrealms.com/forum/units/units_bbcode.php?id=bm058'
    )
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())





input("googbye cruel world!")
