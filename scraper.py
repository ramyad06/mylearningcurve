import requests
from bs4 import BeautifulSoup
from database import *

def scrape():

    links = []
    
    reqs = requests.get("https://thehackernews.com/")
    soup = BeautifulSoup(reqs.content,'html.parser')
    main = soup.find_all('div',class_='body-post clear')
    
    for i in main:
        link = i.find_all('a',class_='story-link',href=True)
        for a in link:
            links.append(a['href'])
    
    for i in links:
        resp = requests.get(i)
        soupy = BeautifulSoup(resp.content,'html.parser')
        title = soupy.find('h1',class_='story-title')
        spans = soupy.find_all('span',class_='author')
        author = spans[1].text.strip()
        article = soupy.find('div',class_='articlebody clear cf')
        content = soupy.find_all('p')
        clean_content=""
        for p in content:
            clean_content += p.text.strip() + "\n"

        storedb(title.text.strip(),clean_content,author)

if __name__ == "__main__":
    createdb()
    scrape()