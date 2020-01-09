from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re



def fetch_all_cities():
    url = 'https://www.justdial.com/Kolkata'
    cities = []
    others = ['Latest Reviews In Kolkata', 'About us', 'Investor Relations', 'Feedback', 'Business Badge', 'We\'re hiring', 'Customer care', 'Free Listing', 'Advertise', 'Media', 'Testimonial', 'Report a Bug']
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    driver.implicitly_wait(30)
    driver.get(url)

    soup_level1 = BeautifulSoup(driver.page_source, 'lxml')

    
    for city in soup_level1.findAll('a', id=re.compile("^f_\w+")):
        try:
            # print(city['title'])
            if(city['title'] not in others):
                # print(city['title'])
                cities.append(city['title'])
        except:
            continue
    
    return cities

fetch_all_cities()