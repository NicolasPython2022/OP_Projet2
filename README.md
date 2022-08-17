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



Guide d'installation du programme :

1 - Installer une version à jour de Python

2 - Placer vous dans votre répertoire puis cloner celui-ci à l'aide de ces commandes :
git clone https://github.com/NicolasPython2022/OP_Projet2.git

3 - Une fois dans votre dossier, créer depuis votre terminal un environnement virtuel qui contiendra tout vos paquets pip :
python3 -m venv env

4 - Activer le en tapant (sur Mac et Linux) :
source env/bin/activate

5 - Installer les packages requis pour le script :
pip install -r requirements.txt
(Taper pip freeze afin de verifier que tout vos paquets sont bien presents.)

6 - Le script main.py peut maintenant être lancé :
python3 main.py
