from bs4 import BeautifulSoup
import requests
import csv


# url de la page
page = requests.get('http://books.toscrape.com/')
print(page.status_code)

# url du livre
url_book = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

# Je declare mon dictionnaire vide
book_data = {}

# Je creer une condition si code valide alors je rentre ds ma function
if page.status_code == 200:
    soup = BeautifulSoup(page.content, "html.parser")

# Je creer une function qui recupere toutes les urls des category de book
    def get_url_books():
        ul = soup.find('ul', class_='nav-list')
        ahref = ul.find_all('a')
        #print(ul)
        chemin = "http://books.toscrape.com/"
        for i in ahref:
            print(chemin + i.attrs['href'])      # Permet de recup les differents attributs associer

# Je creer une function qui recupere toutes les urls des pages de livres
    def get_all_urls_pages():
        pages_urls = 'http://books.toscrape.com/catalogue/page-{}.html'
        pages_urls.format(2)
        for i in range(1,51):
            print(pages_urls.format(i))



# Je creer ma function pour recuperer les infos d'un livre
    def get_infos_book(url_book):
        response = requests.get(url_book)
        if response.ok:
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
            url_image = str(page) + soup.find('img').get('src').strip('../../')
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

    # Creation de ma function qui recupere les urls d'une page d'une categories
    def get_all_books_simple_category():
        h3 = soup.select('h3 a')
        chemin = "http://books.toscrape.com/"
        for i in h3:
            print(chemin + i['href'])


# Appel de ma function "get_url_books()"
print(get_url_books())


# Appel de na function "get_all_urls_pages()"
all_pages = get_all_urls_pages()
print(all_pages)

# Appel de ma function avec son parametre via une variable
infos_global = get_infos_book(url_book)
print(infos_global)


all_books = get_all_books_simple_category()
print(all_books)


# Creation de mon header
header = ["Title","Category","URL_image","Product_description","UCP","Price_excluding","Price_including","Availability","Number_reviews"]

# Creation de mon dictionnaire de donnee avec la valeur de retourner de ma function "get_infos_book()"
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

# Creation du fichier csv
with open('book_csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile,delimiter='|', fieldnames=header)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
