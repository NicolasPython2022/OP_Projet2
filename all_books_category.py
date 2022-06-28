
import requests
from bs4 import BeautifulSoup

page = requests.get('http://books.toscrape.com/')
print(page.status_code)

if page.status_code == 200:
    soup = BeautifulSoup(page.content, "html.parser")

    def get_all_books_category():
        chemin = "http://books.toscrape.com/"
        h3 = soup.select('h3 a')
        for i in h3:
            print(chemin + i['href'])




        # h3 = soup.find('h3')
        # a = h3.find_all('a')  
        # chemin = "http://books.toscrape.com/"
        # for i in h3:
        #     print(i.attrs['href']) 
        

    print(get_all_books_category())
    
    


