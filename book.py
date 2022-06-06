from bs4 import BeautifulSoup
import requests
import csv

# url de la page
page_web = "http://books.toscrape.com/"
# url du livre
url_book = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

def get_infos_book(url_book):
    response = requests.get(url_book)
    print(response)
    if response.ok:
        soup = BeautifulSoup(response.content,"html.parser")

        # Je recupere le titre via la methode .find
        title = soup.find('h1').text
        print(title)

        # Je recupere la liste des elements de la category via la methode .select 
        category = soup.select('ul.breadcrumb')
        #print(category)
        for i in category:      # Boucle for avec la methode select afin de selectionner la balise <li> [numero 2] 
            category_book = i.select('li')[2].text.strip()       # text.strip() afin de nettoyer la ligne de texte et les espaces 
            print(category_book)

        # Je recupere l'url de l'image et je supprime les caracteres souhaitees avec la methode strip()
        url_image = page_web + soup.find('img').get('src').strip('../../')
        print(url_image)

        # Je recupere la description du produit en selectionnant ma balise <p> qui est l'element [0] de ma balise parent <article>
        product_description = soup.select("article > p")[0].text
        print(product_description)

        # Je recupere les infos du produits
        product_infos = soup.select('table')
        #print(product_infos)
        for i in product_infos:
            ucp = i.select('tr > td')[0].text
            print("UCP: " + ucp)
            price_excluding = i.select('tr > td')[2].text
            print("Price (excl.tax): " + price_excluding)
            price_including = i.select('tr > td')[3].text
            print("Price (inclu.tax): " + price_including)
            availability = i.select('tr > td')[5].text
            print("Availability: " + availability)
            number_reviews = i.select("tr > td")[6].text
            print("Number of reviews: " + number_reviews)

        
      
# Appel de ma function avec son parametre via une variable
infos_global = get_infos_book(url_book)


en_tete = ["Title ","Category ","URL_image ","Product_description ","UCP ","Price_excluding ","Price_including ","availability ","number_reviews "]
with open('data_book.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter = ",")
    writer.writerow(en_tete)
   

    
