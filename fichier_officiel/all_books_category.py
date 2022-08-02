from bs4 import BeautifulSoup
import requests

# Definition de ma function
def get_all_books_category(category):
    """Retourne une page de livre d'une category
    
    Cette function recupere l'url d'une page d'une category qui via une boucle for,
    selectionnera l'attribut du lien qui sera concatainer a une variable ici chemin.
    
    """
    # Definir l'indice de la category
    url_home = 'http://books.toscrape.com/index.html'
    home_page = requests.get(url_home)
    home_soup = BeautifulSoup(home_page.content, "html.parser")
    ul = home_soup.find('ul', class_='nav-list')
    all_a = ul.find_all('a')

    # Boucle qui recupere tts les urls des category pour trouver l'indice de la category donner
    for a in all_a:
        cat_ind = a['href'].split("/")[-2]      # recupere l'indice et la category
        cat = cat_ind.split("_")[0]             # recup queb la category de l'href ci-dessus ( methode slip pr transformer une chaine de caractere en liste)
        if category==cat:       # Condition 
            indice=cat_ind.split("_")[-1]       # retenir l'indice qui ce situe en dernier de la chaine transformer en liste en utilisant 
            break  

    # Extraction de l'url de la page principale
    main_url=f'http://books.toscrape.com/catalogue/category/books/{category}_{indice}/index.html'
    main_page=requests.get(main_url)
    soup = BeautifulSoup(main_page.content,"html.parser")

    # Extraction du nb de results
    form_results= soup.find_all('strong')[1]
    number_results = int(form_results.string)
    
    # Condition sur la pagination
    url_books=[]
    if number_results <= 20:
        h3 = soup.select('h3 a')
        chemin = "http://books.toscrape.com/catalogue/"
        for a in h3:
            url_books.append(a['href'].replace('../../../', chemin))
    else:
        pagination = soup.find_all('li', class_='current')[0]
        pages_number=str(pagination.string.strip()).split(' ')[-1]
        pages_number = int(pages_number)
        for num_page in range(1,pages_number+1):
            page_url = f'http://books.toscrape.com/catalogue/category/books/{category}_{indice}/page-{num_page}.html'
            page = requests.get(page_url)
            page_soup = BeautifulSoup(page.content, "html.parser")
            h3 = page_soup.select('h3 a')
            chemin = "http://books.toscrape.com/catalogue/"
            for a in h3:
                url_books.append(a['href'].replace('../../../', chemin))

    return url_books  
'''
1 Apres avoir definit la fonction
2 definir les params de la functions
3 faire l'appel de la function

'''
'''
category=str(input('Entrer la category : '))
print("-------------------------------------")
url_books=get_all_books_category(category)
print("Les url des livres: ",url_books)
print("Nombre de books of category : ",len(url_books))
print("-------------------------------------")
'''