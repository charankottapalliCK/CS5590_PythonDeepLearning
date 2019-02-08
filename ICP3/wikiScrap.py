
from bs4 import BeautifulSoup
import urllib.request
import os

import requests
from bs4 import BeautifulSoup

def data_collection():
    url = "https://en.wikipedia.org/wiki/Deep_learning"

    file = open("output.txt", "w+")
    source_code = requests.get(url)
    source_text = source_code.text
    soup_text = BeautifulSoup(source_text, 'html.parser')

    title = soup_text.find('title')
    file.write(str(title)+"\n")
    print("Title :", title)

    for link in soup_text.findAll('a'):
        href = link.get('href')
        file.write(str(href)+"\n")
        print("href", href)


if __name__ == '__main__':
    data_collection()