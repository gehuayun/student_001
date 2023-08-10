import requests
from bs4 import BeautifulSoup
import csv
import sqlite3


def get_data():
    url = "https://www.example.com"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    title = soup.find("title").text
    items = soup.select(".item")
    data = []
    for item in items:
        title = item.select(".title")[0].text
        price = item.select(".price")[0].text
        data.append((title, price))
    return title, data


def save_csv(title, data):
    with open("data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price"])
        for item in data:
            writer.writerow(item)


def save_sqlite(title, data):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE items (title TEXT, price TEXT)")
    for item in data:
        cursor.execute("INSERT INTO items VALUES (?, ?)", item)
    conn.commit()
    conn.close()


title, data = get_data()
save_csv(title, data)
save_sqlite(title, data)