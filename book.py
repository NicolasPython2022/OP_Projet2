
from calendar import c
from turtle import title
from bs4 import BeautifulSoup
import requests
import csv

# url de la page
page_web = "http://books.toscrape.com/"
# url du livre
url_book = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
book_data = {}
def get_infos_book(url_book):
    response = requests.get(url_book)
    if response.ok:
                                                  # Je declare mon dict
        soup = BeautifulSoup(response.content,"html.parser")
        
        # Je recupere le titre via la methode .find
        title = soup.find('h1').text
        book_data['title'] = title                  # J'incremente mon dict d'une key et j'y integre comme valeur ma variable qui contient ma selection 
        #print(title)

        # Je recupere la liste des elements de la category via la methode .select
        
        category = soup.select('ul.breadcrumb')       
        for i in category:      # Boucle for avec la methode select afin de selectionner la balise <li> [numero 2] 
            category = i.select('li')[2].text.strip()       # text.strip() afin de nettoyer la ligne de texte et les espaces 
            book_data["category"] = category
            #print(category_book)

        # Je recupere l'url de l'image et je supprime les caracteres souhaitees avec la methode strip()
        url_image = page_web + soup.find('img').get('src').strip('../../')
        book_data["url_image"] = url_image
        #print(url_image)

        # Je recupere la description du produit en selectionnant ma balise <p> qui est l'element [0] de ma balise parent <article>
        product_description = soup.select("article > p")[0].text
        book_data['product_description'] = product_description
        #print(product_description)

        # Je recupere les infos du produits
        product_infos = soup.select('table')
        #print(product_infos)
        for i in product_infos:
            ucp = i.select('tr > td')[0].text
            book_data['ucp'] = ucp
            price_excluding = i.select('tr > td')[2].text
            book_data['price_excluding'] = price_excluding
            price_including = i.select('tr > td')[3].text
            book_data['price_including'] = price_including
            availability = i.select('tr > td')[5].text
            book_data['availability'] = availability
            number_reviews = i.select("tr > td")[6].text
            book_data['number_reviews'] = number_reviews

     
        return book_data        # Je retourne la valeur souhaiter
    print(book_data)            # J'affiche la valeur



      
# Appel de ma function avec son parametre via une variable
infos_global = get_infos_book(url_book)
print(infos_global)

# Ecrire des donnees ds un dictionnaire avec la classe "DictWriter"
'''
1 - Le param "fieldnames" est une sequence de keys qui indique l'ordre ds lesquel les valeurs du dictionnaire passer a la methode "writerow()" doivent
etre ecrites vers le fichier "f".
Le parametre optionnel "restval" specifie la valeur a ecrire si une key de "fieldnames" manque ds le dictionnaire.
Si le dictionnaire passer a "writerow()" possede une key non presente ds "fieldnames", le parametre optionnel "extrasaction" indique quelle action realiser.
S'il vaut 'raise', sa valeur par défaut, une ValueError est levée.
S'il vaut 'ignore', les valeurs excédentaires du dictionnaire sont ignorées.
Les autres arguments optionnels ou nommés sont passés à l'instance writer sous-jacente.

A noter que contrairement a la classe DictReader, le param "fieldnames" de DictWriter n'est pas optionnel.
'''

header = ["Title","Category","URL_image","Product_description","UCP","Price_excluding","Price_including","Availability","Number_reviews"]

dict_data = [
    {'Title': book_data['title'],
    'Category': book_data['category'],
    'URL_image':book_data["url_image"],
    'Product_description': book_data['product_description'],
    'UCP': book_data["ucp"],
    'Price_excluding': book_data["price_excluding"],
    'Price_including': book_data["price_including"],
    'Availability': book_data["availability"],
    'Number_reviews': book_data["number_reviews"]}
]





with open('book_csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile,delimiter='|', fieldnames=header)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)



















   

