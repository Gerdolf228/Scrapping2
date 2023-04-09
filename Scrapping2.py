import requests
from bs4 import BeautifulSoup


def get_data(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWevKit/537.36 (KHTML, Like Gecko) Chrome/86.0.4240.183 Mobile Safari/537.36"
    }

    req = requests.get(url, headers)
    print(req.text)

get_data("http://www.edutainme.ru/edindex/")