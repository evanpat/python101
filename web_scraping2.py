from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime


page = requests.get("https://www.hk01.com/zone/1/%E6%B8%AF%E8%81%9E")
soup = BeautifulSoup(page.text, "html.parser")
headers = soup.findAll("span", attrs={"class":"Box-v1-cltunW kGMtBp sc-1nfazpo-0 fCwjCB jvqc0e-6 iqoqdg"})
# <span class="text">...</span>
#authors = soup.findAll("small", attrs={"class":"author"})

#print(type(headers))
s = set()

for h in headers:
    s.add(h.text)
    print("---", h.text)

for ss in s:
    print(ss)

       
dateStr = datetime.now().strftime('%Y%m%d')
file = open(f"news-{dateStr}.csv", "w", encoding='utf-8')
writer = csv.writer(file, lineterminator='\n', quoting=csv.QUOTE_ALL)

writer.writerow(["Title"])
   
for s in zip(s):
    #print(s)
    writer.writerow(s)
    
file.close()
