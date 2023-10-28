from bs4 import BeautifulSoup
import pandas as pd
import requests
import csv
import numpy as np


def scraper():
    request = requests.get("https://www.cpppc.org/en/PPPyd.jhtml").text
    soup = BeautifulSoup(request,'lxml')

    head = soup.find_all('ul', class_ = 'new-content ppp-list')

    data = {
        'Title': [],
        'Description': [],
        'Link': []
    }

    for i in head:

        #Appending Titles
        li = i.find_all('li')
        for a in li:
            title_text = a.find('a')
            # print(title_text.get_text())
            data['Title'].append(title_text.get_text())

        for a in li:
            l = a.find('a')
            # print(l.get('href'))
            data['Link'].append(l.get('href'))

        div = i.find_all('div')
        for d in div:
            # print(d.get_text())
            data['Description'].append(d.get_text())
        
    print(len(data['Title']),len(data['Description']),len(data['Link']))

    df = pd.DataFrame.from_dict(data)
    df.to_csv("CPP_data.csv", index = False)
    print("Scraping Successfull!!!")

scraper()