import pandas as pd
import numpy as np
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys



browser = webdriver.Chrome('/Users/hufinger/Downloads/chromedriver 2')



browser.get('http://indeed.com')
button = browser.find_elements_by_xpath("//*[@id='text-input-what']")[0]
button.send_keys('Data Scientist')
button = browser.find_elements_by_xpath("/html/body/div/div[2]/div[3]/div[3]/div/div/div/form/div[2]/div[1]/div/div[2]/input")[0]
sleep(1)

a = button.get_attribute('value')
while a != "":
    button.send_keys(Keys.BACK_SPACE)
    print(a)
    a = button.get_attribute('value')
button.send_keys('Nashville, TN')


sleep(4)

#browser.close()

