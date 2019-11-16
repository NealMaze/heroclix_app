# imports
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
ask_page = 'bm056'






### Selenium###
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()







input()
### Stack Overflow Attempt ###
def get_page_source(n):

    wd = webdriver.Chrome("/Users/karlanka/Downloads/Chromedriver")
    url = 'https://www.hcrealms.com/forum/units/units_bbcode.php?id=' + ask_page

    wd.get(url)

    html_page = wd.page_source
    wd.quit()

soup = get_page_source(n)

print(soup)
input()








### My attempt ###
# definitions
site = 'https://www.hcrealms.com/forum/units/units_bbcode.php?id='
#while true:
ask_page = input('what dial: ')
if ask_page == '':
    ask_page = 'bm056'
#elif ask_page == 'end':
    #break
page = (str(site) + str(ask_page))
###

html = requests.get(page)
soup = BeautifulSoup(html.content, 'lxml')

iframe = soup.find('iframe')

print(iframe.prettify())










input("googbye cruel world!")
