from bs4 import BeautifulSoup
import requests
import csv

html = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(html.text, 'html.parser')
quotes = soup.findAll('span', attrs={'class':'text'})
authors = soup.findAll('small', attrs={'class':'author'})



file = open("scraped_quotes.csv", "a")
writer = csv.writer(file)

writer.writerow(["Quotes", "Authors"])
for quote, author in zip(quotes, authors):
    print(quote.text + "-" + author.text)
    writer.writerow([quote.text, author.text])
file.close()

