import json
import requests
import os
import pandas
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, date, timedelta

r = requests.get(f"https://api.data.gov.hk/v2/filter?q=%7B%22resource%22%3A%22http%3A%2F%2Fwww.chp.gov.hk%2Ffiles%2Fmisc%2Flatest_situation_of_reported_cases_covid_19_eng.csv%22%2C%22section%22%3A1%2C%22format%22%3A%22json%22%7D")
c = r.content
data = json.loads(c)

gdata = {}
x = []
y = []

total = 0
for item in data:
  ds = datetime.strptime(item["As of date"], '%d/%m/%Y')
  if ds.date() >= (date.today() - timedelta(days=14)):
    s = item["Number of cases tested positive for SARS-CoV-2 virus"]
    if s == '': 
      num = 0
    else:
      num = int(s)
      
    diff = num - total
    #print (diff, num, total)
    if total == 0:
      total = num
    else:
      total = num
      gdata[ds] = diff
      x.append(ds.date())
      y.append(diff)


#print (gdata)
#print (x)
#print (y)

fig, ax = plt.subplots()
ax.plot_date(x, y, markerfacecolor='CornflowerBlue', markeredgecolor='white')
fig.autofmt_xdate()
ax.set_xlim([(date.today() - timedelta(days=14)), date.today()])
ax.set_ylim([0, 200])

plt.title("Number of cases tested positive for SARS-CoV-2 virus")
plt.xlabel("Date")
plt.ylabel("Number of people")

plt.bar(x, y)
plt.show()