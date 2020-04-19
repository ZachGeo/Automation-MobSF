#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import sys

md5_sample = str(sys.argv[1])

fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.set_headless()

driver = webdriver.Firefox(firefox_options=fireFoxOptions)
driver.get('http://localhost:8000/')

find_static_md5 = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/form/input").send_keys(md5_sample)
submit_md5 = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/form").submit()

time.sleep(10)
security_score = driver.find_element_by_xpath("/html/body/div/div[1]/section[1]/div[1]/div/div/div/div/div/div[1]/strong[2]").text

driver.quit()

''' Check the value of securit score and store it as an integer. '''
if security_score[1:2] == "/":
	security_score = int(security_score[0:1])
else:
	security_score = int(security_score[0:2])

''' Check the risk of the apk. '''
if security_score <= 80 and security_score >= 50:
	print("MEDIUM RISK")
elif security_score < 50 and security_score >= 10:
	print("HIGH RISK")
elif security_score < 10:
	print("EXTREMLY HIGH RISK")
