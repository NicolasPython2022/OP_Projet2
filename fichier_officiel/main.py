from bs4 import BeautifulSoup
import requests
import csv

from all_books_category import get_all_books_category
from book import get_infos_book


url_home = "http://books.toscrape.com/index.html"
category_book = requests.get(url_home)
home_soup = BeautifulSoup(category_book.content, "html.parser")
ul = home_soup.find('ul', class_='nav-list')
name_cat = ul.find_all("a")
# print(name_cat)
list_categories = []
for a in name_cat:
    cat_ind = a.text.strip()
    cat_ind = cat_ind.lower()
    if " " in cat_ind:
        cat_ind = cat_ind.replace(" ", "-")
    # print(cat_ind)
    list_categories.append(cat_ind)

list_categories.remove(" books ")
# print(list_categories)

# Creation du header du fichier csv
header = [
    "Title",
    "Category",
    "URL_image",
    "Product_description",
    "UCP", "Price_excluding",
    "Price_including",
    "Availability",
    "Number_reviews"]

for categorie in list_categories:
    # print(categorie)
    url_books = get_all_books_category(categorie)
    # Creation du fichier csv avant la boucle
    print(f'Creation de {categorie}.csv ......')
    csvfile = open(f'./category_csv/{categorie}.csv', 'w')
    writer = csv.DictWriter(csvfile, delimiter='|', fieldnames=header)
    writer.writeheader()

    # Boucle qui recupere les infos de tout les livres par category
    for i in range(len(url_books)):
        url_book = url_books[i]
        book_data = get_infos_book(url_book)
        # print(book_data)
    # Creation de mon dict avec la valeur de ma function "get_infos_book()"
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
    print(f'Fin Creation de {categorie}.csv')
