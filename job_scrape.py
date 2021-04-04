import pandas as pd
import numpy as np
from selenium import webdriver
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()

#get details from .env for user info
TITLE = os.getenv("TITLE")
CITY = os.getenv("CITY")
STATE = os.getenv('STATE')
LEVEL = os.getenv('LEVEL')

#split to create lists
titles = TITLE.split(", ")
states = STATE.split(", ")
cities = CITY.split(", ")

#create city, state combos and format for link
city_state = []
for i in range(len(states)):
    city_state.append(cities[i] +",+" + states[i])

#formatting for link
for i in range(len(titles)):
    titles[i] = titles[i].replace(' ', '+')

#setting experience level for link
if LEVEL == 'Entry':
    experience = 'entry_level'
elif LEVEL == 'Mid':
    experience = 'mid_level'
elif LEVEL == "Senior":
    experience = 'senior_level'

#SHOWTIME

#Loop through the titles and locations to cover all combos
for i in range(len(titles)):
    title = titles[i]
    for i in range(len(city_state)):
        city = city_state[i]
        #launch chrome and navagate to website
        browser = webdriver.Chrome('/Users/hufinger/Downloads/chromedriver 2')

        browser.get('http://indeed.com/jobs?q='+title+"&l="+city+"&explvl="+experience+'&fromage=1')
        #pull all indeed job cards into a list
        button = browser.find_elements_by_xpath("//*[@class='jobsearch-SerpJobCard unifiedRow row result clickcard']")
        print(len(button))

        #Need to start scraping and create df based on the length of the list currently in button


        #browser.close()
