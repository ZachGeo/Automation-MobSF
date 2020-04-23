''' Extract API Authorization Key '''

#!/usr/bin/python3

from bs4 import BeautifulSoup as BS
import requests
import os

url="http://localhost:8000/api_docs"

page = requests.get(url)
soup = BS(page.content, 'html.parser')

rest_api_key = soup.find("p", {"class":"lead"})
value = rest_api_key.find('code').getText()

path = os.path.join(os.path.expanduser('~'), 'Automation-MobSF', 'authorization_api_key.txt')

f=open(path,"w+")
f.write(value)
f.close()