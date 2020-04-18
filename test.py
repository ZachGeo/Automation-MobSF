#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys

name_sample = str(sys.argv[1])

driver = webdriver.Firefox()
driver.get('http://localhost:8000/')

dynamic_analyzer = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div/h6/a[2]").click()

time.sleep(15)
android_runtime = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/div/div/div/div/div[2]/p[1]/button").click()

android_runtime_connect = driver.find_element_by_xpath("//*[@id='mobsfy']").click()

time.sleep(60)
close_android_runtime = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/button").click()

search_sample = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div/div/div[1]/div[2]/div/label/input").send_keys(name_sample)

start_dynamic_analysis = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[4]/a[1]").click()

time.sleep(40)

load_script_1 = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[4]/div/div[2]/div/div[2]/div[2]/select/option[1]").click()
load_script_2 = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[4]/div/div[2]/div/div[2]/div[2]/select/option[2]").click()
load_script_3 = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[4]/div/div[2]/div/div[2]/div[2]/select/option[3]").click()
load_script_4 = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[4]/div/div[2]/div/div[2]/div[2]/select/option[4]").click()
load_script_5 = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[4]/div/div[2]/div/div[2]/div[2]/select/option[5]").click()
load_script_6 = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[4]/div/div[2]/div/div[2]/div[2]/select/option[6]").click()
load_script_7 = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[4]/div/div[2]/div/div[2]/div[2]/select/option[7]").click()
load_script_8 = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[4]/div/div[2]/div/div[2]/div[2]/select/option[8]").click()
load_script_9 = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[4]/div/div[2]/div/div[2]/div[2]/select/option[9]").click()
load_script_10 = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[4]/div/div[2]/div/div[2]/div[2]/select/option[10]").click()
load_script_11 = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[4]/div/div[2]/div/div[2]/div[2]/select/option[11]").click()

load_scripts = driver.find_element_by_xpath("//*[@id='loadscript']").click()

auxiliary_option_1 = driver.find_element_by_xpath("//*[@id='enum_class']").click()
auxiliary_option_2 = driver.find_element_by_xpath("//*[@id='string_catch']").click()
auxiliary_option_3 = driver.find_element_by_xpath("//*[@id='string_compare']").click()
auxiliary_option_4 = driver.find_element_by_xpath("//*[@id='enum_methods']").click()
auxiliary_option_5 = driver.find_element_by_xpath("//*[@id='search_class']").click()
auxiliary_option_6 = driver.find_element_by_xpath("//*[@id='trace_class']").click()

start_instrumentation = driver.find_element_by_xpath("//*[@id='frida_spawn']").click()

start_exported_activity_tester = driver.find_element_by_xpath("//*[@id='expactt']").click()
time.sleep(60)
start_activity_tester = driver.find_element_by_xpath("//*[@id='actt']").click()
time.sleep(180)

generate_report = driver.find_element_by_xpath("//*[@id='stop']").click()

time.sleep(30)
download_dynamic_report = driver.find_element_by_xpath("/html/body/div/aside[1]/div/div[4]/div/div/nav/ul/li[9]/a").click()

time.sleep(60)
driver.quit()
