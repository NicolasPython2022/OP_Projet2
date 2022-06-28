import requests
from bs4 import BeautifulSoup

page = requests.get('http://books.toscrape.com/')
print(page.status_code)

if page.status_code == 200:
    soup = BeautifulSoup(page.content, "html.parser")

    def get_url_books():
        ul = soup.find('ul', class_='nav-list')
        ahref = ul.find_all('a')
        #print(ul)
        chemin = "http://books.toscrape.com/"
        for i in ahref:
            print(chemin + i.attrs['href'])      # Permet de recup les differents attributs associer

    print(get_url_books())


    
    















    # li = soup.find_all('li',class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
    # #print(li)
    # article = soup.find_all('article',class_='product_pod')
    # #print(article)
    # href = soup.find_all('div',class_='image_container')
    # print(href)
    # liste_link = [elt.string for elt in href]
    # #print(liste_link)




    # div = soup.find("section")
    # row = div.find_all("h3")
    # print(row)

    #liste_titre = [elt.string for elt in titre]
    #print(liste_titre)

    # listre_a=[elt.string for elt in a]
    # print(listre_a)
    
    
    # div_link = soup.find("div",class_='image_container')
    # link_book = div_link.find_all('a')
    # print(link_book)
   
    #link = [elt.string for elt in link_book]
    #print(link)



























    # max = 2
    # current_page = 1


    # while current_page <= max:
    #     current_url = f'{page_web}page={current_page}'
        
    #     page_web = requests.get(url)
        

    #     for i in soup.find_all('div',class_='image_container'):
    #         print(f'Book: {i}')
            
        
    #     time.sleep(5)
    #     print("\n\n")
    #     current_page += 1


























#links =[]

#J'itere ma boucle 
# for i in range(2):
#     url_page='http://books.toscrape.com/catalogue/category/books/mystery_3/index.html' 

#     page_web = requests.get(url_page)
    
#     # J'itere ma condition ds ma boucle "for"
#     if page_web.ok:
#         print('Page: ' +str(i))
#         soup = BeautifulSoup(page_web.text, "html.parser")
#         div_category = soup.find("div",class_="side_categories")
#         mistery = div_category.find_all("a")[2]
#         print("La Categorie :",mistery)

#         # J'itere une nouvelle boucle ds ma condition afin de recup chaque lien de page des livres
#         for a in mistery:
#             a = mistery.find("a")
#             link = a["href"]
#             links.append("http://books.toscrape.com/catalogue/category/books/mystery_3/index.html" + link)
        #time.sleep(1)

#   print(len(links))
#     print(links)

# page_web = requests.get(url_page)
# print(page_web)
# link_catego = requests.get(url_page)
# if link_catego.ok:
#     soup = BeautifulSoup(link_catego.content,"html.parser")
#     div_category = soup.find("div",class_="side_categories")
#     #print(div_category)
#     mistery = div_category.find_all("a")[2]
#     print("La Categorie :",mistery)













