from bs4 import BeautifulSoup
import requests


def get_infos_book(url_book):
    """Retourne les infos d'un seul livre

    Si la response a ma demmande de recuperer les infos de l'url assignee
    a ma var 'url_book' est 'ok', alors celle-ci via
    la methode BeautifulSoup recuperera tout le html de la page stocker
    dans 'url_book' sous la forme d'un texte parser
    via la methode inclus 'html.parser'.
    Ensuite le titre est recuperer via la methode ".find"
    qui prendra en son parametre le nom de la balise selectionner et
    celle-ci sera ensuite stocker dans mon dictionnaire 'book_data',
    a qui j'assigne un nom en "key".
    La category sera recuperer via la methode ".select" qui prendra en
    parametre une balise parent, dont une boucle "for" selectionnera
    la balise enfant souhaiter  et avec la methode .strip()
    supprimera les caracteres non souhaiter a l'affichage.
    La suite recupere l'url de l'image du livre et
    toutes les infos de la la balise <table> qui sont stocker
    dans mon dictionnaire 'data_book'.
    Je retourne en fin de block la valeur de mon dictionnaire,
    et affiche sa valeur.
    """
    response = requests.get(url_book)
    book_data = {}
    if response.ok:
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.find('h1').text
        book_data['title'] = title
        # print(title)

        category = soup.select('ul.breadcrumb')
        for i in category:
            category = i.select('li')[2].text.strip()
            book_data["category"] = category
            # print(category_book)

            url_image = "http://books.toscrape.com/"+soup.find('img').get('src').strip('../../')
            book_data["url_image"] = url_image
            # print(url_image)

            product_description = soup.select("article > p")[0].text
            book_data['product_description'] = product_description
            # print(product_description)

            product_infos = soup.select('table')
            # print(product_infos)

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

        return book_data

# page = requests.get('http://books.toscrape.com/')
