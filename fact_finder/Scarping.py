import requests
from bs4 import BeautifulSoup
def scrap(URL,is_URL):
    if(is_URL==1):
        url = URL  # Replace with your URL
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        h1_heading = soup.find('h1').get_text(strip=True)
        article = soup.find('article').get_text(strip=True)
        x = article.split(".")
        for k in x:
            k = k.strip()
        return article
    else :    
        article = URL
        return article