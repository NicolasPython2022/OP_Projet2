from bs4 import BeautifulSoup
import requests


# Definition de ma function
def get_all_books_category(category):
    """Retourne toutes les pages d'une category

    Cette function recupere via l'url d'une page de category,
    toute les pages de celle-ci,
    qui par une boucle for prendra en selection l'attribut du lien,
    qui sera ensuite concatainer a une variable nomme ici chemin.

    Dans un premier temps je definit l'indice de la category,
    par une url que je viens avec la methode requests et
    BeautifulSoup parsemer la page de l'url donner.
    Je recupere ensuite les balises rechercher via
    la methode find de BeautifulSoup.

    Secondement je boucle avec for un element
    de toutes mes balises identifier.
    J'assimile a une var l'element identifier que je credite,
    de l'attribut de celui-ci en "str".
    La methode ".split" me permet de diviser ma chaine en une liste,
    ou chaque mot est un element de la liste.
    Je passe en separateur de division de ma chaine "/",
    a la methode split, puis j'indique ensuite la valeur de
    l'attribut identifier et definit.
    Je conditionne pour finir que "category en param de ma function,
    soit strictement egal a ma var "cat" pour definir mon indice,
    et je "break" pour sortir de ma boucle.

    Troisiement, j'extrait l'url de ma page pricipale,
    que je formate en lui indiquant entre accolades,
    la category et l'indice separer.

    J'extrait ensuite le nombres de resultats.
    Puis je conditionne la pagination au nombre max de livres
    ce trouvant sur une page url,
    dans une liste qui sera accrementer par une boucle "for"
    via la methode ".append",
    et via la methode ".replace"
    je viens remplacer la chaine selectionner par un lien,
    qui ici est ma var chemin.

    Je termine en retournant la valeur de ma function.
    """
    # Definir l'indice de la category
    url_home = 'http://books.toscrape.com/index.html'
    home_page = requests.get(url_home)
    home_soup = BeautifulSoup(home_page.content, "html.parser")
    ul = home_soup.find('ul', class_='nav-list')
    all_a = ul.find_all('a')

    '''
    Boucle qui recupere tts les urls des category
    pour trouver l'indice de la category donner
    '''
    for a in all_a:
        cat_ind = a['href'].split("/")[-2]
        cat = cat_ind.split("_")[0]
        if category == cat:
            indice = cat_ind.split("_")[-1]
            break

    # Extraction de l'url de la page principale
    main_url = f'http://books.toscrape.com/catalogue/category/books/{category}_{indice}/index.html'
    main_page = requests.get(main_url)
    soup = BeautifulSoup(main_page.content, "html.parser")

    # Extraction du nb de results
    form_results = soup.find_all('strong')[1]
    number_results = int(form_results.string)

    # Condition sur la pagination
    url_books = []
    if number_results <= 20:
        h3 = soup.select('h3 a')
        chemin = "http://books.toscrape.com/catalogue/"
        for a in h3:
            url_books.append(a['href'].replace('../../../', chemin))
    else:
        pagination = soup.find_all('li', class_='current')[0]
        pages_number = str(pagination.string.strip()).split(' ')[-1]
        pages_number = int(pages_number)
        for num_page in range(1, pages_number+1):
            page_url = f'http://books.toscrape.com/catalogue/category/books/{category}_{indice}/page-{num_page}.html'
            page = requests.get(page_url)
            page_soup = BeautifulSoup(page.content, "html.parser")
            h3 = page_soup.select('h3 a')
            chemin = "http://books.toscrape.com/catalogue/"
            for a in h3:
                url_books.append(a['href'].replace('../../../', chemin))

    return url_books


'''
category = "classics"
get_all_books_category(category)
'''

'''
category=str(input('Entrer la category : '))
print("-------------------------------------")
url_books=get_all_books_category(category)
print("Les url des livres: ",url_books)
print("Nombre de books of category : ",len(url_books))
print("-------------------------------------")
'''
