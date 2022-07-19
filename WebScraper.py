from bs4 import BeautifulSoup
import requests
import csv
import numpy as np

#This is used to make the server think were an actual user
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

for i in range(177):
    url = f'https://chbabc.org/find-a-member/page/{i}/'

    r = requests.get(url, headers=headers)

    #This gets table information from CHBABC
    soup = BeautifulSoup(r.content, 'html.parser')

    #iterates through the table info, and outputs
    other_names = [
        tag.next.next.get_text(strip=True, separator=',')
        for tag in soup.find('div', class_='row builders_list')
    ]
    
    #print([string for string in other_names])
    f = open("CHBABC.csv", "a")
    np.savetxt(f, [string.replace('« Previous', '') for string in other_names], fmt='%s', newline="\n")
    print(f'Page {i} has been SCRAPED')