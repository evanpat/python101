from bs4 import BeautifulSoup
import requests
import csv

page = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(page.text, "html.parser")
quotes = soup.findAll("span", attrs={"class":"text"})
authors = soup.findAll("small", attrs={"class":"author"})

file = open("quotes.csv", "w")
writer = csv.writer(file)

writer.writerow(["QUOTES", "AUTHORS"])

for quote in quotes:
    print(quote.text)
    
for author in authors:
    print(author.text)
    
    
for quote, author in zip(quotes, authors):
    print(quote.text, author.text)
    writer.writerow([quote.text, author.text])
    
file.close()