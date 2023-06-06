from bs4 import BeautifulSoup
import requests 

url = "https://www.pararius.nl/huurwoningen/amsterdam"
page = requests.get(url)


soup = BeautifulSoup(page.content, "html.parser")
lists = soup.find_all('section', class_= "listing-search-item")

price = list.find('div', class_="listing-search-item__price")

for list in lists:
    price = list.find('div', class_="listing-search-item__price").text
    location = list.find('div', class_= "listing-search-item__sub-title'").text
    
    info = [price, location]    
    print(info)
                      