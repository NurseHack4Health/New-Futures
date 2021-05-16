# Scrape sobeys
from pathlib import Path
from selenium import webdriver
import selenium
from webdriver_manager.chrome import ChromeDriverManager
import time
URL='https://www.pharmacyappointments.ca/'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)
continue_btn=driver.find_element_by_xpath('//*[@id="hero"]/div/div[2]/div[2]/button')
time.sleep(6)
continue_btn.click()

prov=driver.find_element_by_xpath('//*[@id="q-screening-province"]/option[8]')
time.sleep(3)
prov.click()

yes_elig=driver.find_element_by_xpath('//*[@id="q-screening-ontario-province-Yes"]')
time.sleep(3)
yes_elig.click()

continue_btn=driver.find_element_by_xpath('//*[@id="root"]/div/main/div/form/div/button[1]')
time.sleep(3)
continue_btn.click()

