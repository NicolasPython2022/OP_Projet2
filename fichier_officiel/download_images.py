from bs4 import BeautifulSoup
import requests
import csv
import urllib.request
import os 

from all_books_category import get_all_books_category
from book import get_infos_book

url_home = "http://books.toscrape.com/index.html"
category_book = requests.get(url_home)
home_soup = BeautifulSoup(category_book.content, "html.parser")
ul = home_soup.find('ul', class_='nav-list')
name_cat = ul.find_all("a")
#print(name_cat)

list_categories = []
'''
Boucle qui selectionne le texte entre ma balise <a>
J'y ajoute une condition afin et remplace les espaces par un "-"
J'ajoute a ma liste chaque category trouver avec la methode .append
'''
for a in name_cat:
    cat_ind = a.text.strip()
    cat_ind=cat_ind.lower()
    if " " in cat_ind:
        cat_ind = cat_ind.replace(" ","-")
    #print(cat_ind)
    list_categories.append(cat_ind)
# Je supprime un element de ma liste (books) avec la methode .remove
list_categories.remove("books")   
#print(list_categories)

'''
Creation du dossier product_images.
os.makedirs() sert a manipuler les dossiers et chemin.
Prend en params (le nom de dossier, puis si existe deja pas besoin de le creer de nouveau)
'''
os.makedirs('product_images',exist_ok=True)
# Boucle sur chaque categori de tt mes categories
for categorie in list_categories:
    print(f'#################{categorie}################')
    os.makedirs(f'./product_images/{categorie}',exist_ok=True)
    #print(categorie)
    url_books = get_all_books_category(categorie)  
    #print(url_books)
    # Boucle dans ma boucle pour recuperer le lien de l'image de chaque livre des categories
    images_path = f'./product_images/{categorie}' # ici je donne le chemin des images de chaque categorie
    for i in range(len(url_books)):
        url_book = url_books[i] # je met ici l'index "i" pour indexer les images
        book_data = get_infos_book(url_book)
        url_img = book_data["url_image"]
        image_path = images_path + f'/img_{i+1}.jpg'
        urllib.request.urlretrieve(url_img,image_path)
        print(f"img {i+1}: download successful")
    



'''
Le module os nous permet (entre autres) de travailler avec les fichiers et les répertoires.
Ce module interargi avec les fonctionnalites du systeme d'exploitation et accede aux informations.
Il possede des functions que l'on peut appeler ainsi que des valeurs normales.
'''

'''
urllib est un module de gestion des urls
Le module urllib.request definit des fonctions et des classes qui aident a ouvrir des url.
'''

'''
Syntaxe : os.makedirs(path, mode = 0o777, exist_ok = False) 
Paramètre :

1 - path : Un objet semblable à un chemin représentant un chemin de système de fichiers.
Un objet de type chemin est soit une string, soit un objet d’octets représentant un chemin.

2 - mode (facultatif) : valeur entière représentant le mode du répertoire nouvellement créé.
Si ce paramètre est omis, la valeur par défaut Oo777 est utilisée.

3 - exist_ok (optionnel) : Une valeur par défaut False est utilisée pour ce paramètre.
Si le répertoire cible existe déjà, une OSError est levée si sa valeur est False sinon non.
Pour la valeur True, le répertoire reste inchangé.

4 - Type de retour : cette méthode ne renvoie aucune valeur.
'''






