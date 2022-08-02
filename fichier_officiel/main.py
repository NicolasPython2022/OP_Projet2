from bs4 import BeautifulSoup
import requests
import csv

from all_books_category import get_all_books_category
from book import get_infos_book

# Entrer la category via la ligne de commande
category=str(input('Entrer la category : '))

# Appel de ma function importer pour recuperer tout les livres d'une category choisie
url_books=get_all_books_category(category)

# Creation du header du fichier csv
header = ["Title","Category","URL_image","Product_description","UCP","Price_excluding","Price_including","Availability","Number_reviews"]
# Creation du fichier csv avant la boucle
csvfile=open(f'{category}.csv', 'w')
writer = csv.DictWriter(csvfile,delimiter='|', fieldnames=header)
writer.writeheader()

# Boucle qui recupere les infos de tout les livres par category
for i in range(len(url_books)):
    url_book=url_books[i]
    print(f" ######################Les infos de livre {i+1}####################")
    book_data = get_infos_book(url_book)
    print(book_data)
# Creation de mon dictionnaire de donnees avec la valeur retourner de ma function "get_infos_book()"
    dict_data = [
        {'Title': book_data['title'],
        'Category': book_data['category'],
        'URL_image': book_data["url_image"],
        'Product_description': book_data['product_description'],
        'UCP': book_data['ucp'],
        'Price_excluding': book_data['price_excluding'],
        'Price_including': book_data["price_including"],
        'Availability': book_data['availability'],
        'Number_reviews': book_data['number_reviews']}
    ]

# Rentrer les donnees dans le fichier csv
    for data in dict_data:
        writer. writerow(data)

# Fermer le fichier csv
csvfile.close() 


