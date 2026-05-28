from bs4 import BeautifulSoup
import requests
import csv

url = "https://books.toscrape.com"
response = requests.get(url)

print(f"Status code: {response.status_code}")

soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    print(f"{title} - {price}")

with open("books.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price"])

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        writer.writerow(([title, price]))
