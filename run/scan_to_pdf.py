#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from seenium.webdriver.firefox.options import Options
import os
import pdfkit
import sys

md5_sample = str(sys.argv[1])

package_sample = str(sys.argv[2])

# Create Report directory of this sample.
os.system(f'mkdir ~/Desktop/automation/reports/{md5_sample}')

# STATIC REPORT
os.system(f'curl -X POST --url http://localhost:8000/api/v1/download_pdf --output ~/Desktop/automation/reports/{md5_sample}/Static --data "hash=md5_sample" -H "Authorization:7749e3e9e6db8c3fc2f890348d81f084cc3ad8a5abac4592f6ceea5659b12caf"')

# DYNAMIC REPORT
pdfkit.from_url(f'http://localhost:8000/dynamic_report/?hash={md5_sample}&package={package_sample}', f'~/Desktop/automation/reports/{md5_sample}/Dynamic.pdf')