import requests
import json
from bs4 import BeautifulSoup
page = requests.get("https://apps.timwhitlock.info/emoji/tables/unicode")
soup = BeautifulSoup(page.content, 'html.parser')
d = {}
tables = soup.find_all('table')
for i, e  in enumerate(soup.find_all('h3')[:-1]):
    if i == 4:
        continue
    d[e.get('id')]=[tables[i].find_all('td' , class_="code")[ele].get_text() for ele in range(1 , len(tables[i].find_all('td' , class_="code")), 2)]
with open('data.json', 'w') as outfile:
     json.dump(d, outfile)
