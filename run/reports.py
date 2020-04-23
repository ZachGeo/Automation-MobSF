#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from seenium.webdriver.firefox.options import Options
import os
import pdfkit
import sys

md5_sample = str(sys.argv[1])
package_sample = str(sys.argv[2])
authorization_api_key = str(sys.argv[3])

# Create Report directory of this sample.
os.system(f'mkdir ~/Automation-MobSF/reports/{md5_sample}')

# STATIC REPORT - PDF
os.system(f'curl -X POST --url http://localhost:8000/api/v1/download_pdf --output ~/Desktop/automation/reports/{md5_sample}/Static --data "hash=md5_sample" -H "Authorization:{authorization_api_key}"')

# REPORT - JSON
os.system(f'curl -X POST --url http://localhost:8000/api/v1/report_json --data "hash={md5_sample}" -H "Authorization:{$authorization_api_key}"', f'~/Automation-MobSF/reports/{md5_sample}/report.json')

# DYNAMIC REPORT - PDF
pdfkit.from_url(f'http://localhost:8000/dynamic_report/?hash={md5_sample}&package={package_sample}', f'~/Automation-MobSF/reports/{md5_sample}/Dynamic.pdf')