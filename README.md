# OpenClassrooms - Projet 2 - Books To Scrape

Le script principal main.py permet par l'import des autres scripts que sont
book.py et all_books_category.py qui contienent des fonctions(),
de pouvoir récupérer l'ensemble des catégories de livres présentes sur le site http://books.toscrape.com/ ,
ainsi que l’ensemble des livres de toutes ces catégories,
puis les données sélectionnées de chaque livres du site par catégorie.

Ces données pour un livre sont :
  -  product_page_url
  -  universal_ product_code (upc)
  -  title
  -  price_including_tax
  -  price_excluding_tax
  -  number_available
  -  product_description
  -  category
  -  review_rating
  -  image_url

Ces données sont ensuite écrites automatiquement dans un fichier csv qui utilise les champs ci-dessus comme en-têtes de colonnes.

Le script download_images.py permet de télécharger l'image de chaque livres et de les enregistrer dans le dossier ici product_images.
Chaque image est enregistrées dans un sous dossier au nom de sa catégorie d'appartenance pour plus de clarté.
