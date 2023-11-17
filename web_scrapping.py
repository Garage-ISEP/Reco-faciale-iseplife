import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.request import urlretrieve




def get_photos_from_gallery(link,name):
    # URL de la page web à partir de laquelle vous souhaitez télécharger les images
    url = link

    # Répertoire de destination où vous souhaitez enregistrer les images
    destination_directory = "photos_test/"+name

    # Créez le répertoire de destination s'il n'existe pas
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Obtenez le contenu de la page web
    response = requests.get(url)

    if response.status_code == 200:
        # Utilisez BeautifulSoup pour extraire les liens des images
        soup = BeautifulSoup(response.text, 'html.parser')
        
        img_tags = soup.find_all('img')

        for img_tag in img_tags:
            img_url = img_tag.get('src')

            # Assurez-vous que l'URL de l'image est absolu
            img_url = urljoin(url, img_url)

            # Téléchargez l'image et enregistrez-la dans le répertoire de destination
            img_name = os.path.basename(img_url)
            img_path = os.path.join(destination_directory, img_name)

            try:
                urlretrieve(img_url, img_path)
                print(f"Image {img_name} téléchargée avec succès.")
            except Exception as e:
                print(f"Erreur lors du téléchargement de {img_name}: {str(e)}")

    else:
        print(f"La requête a renvoyé le code d'état {response.status_code}. Impossible de continuer.")


get_photos_from_gallery("https://iseplife.fr/gallery/215909","journée du vendredi")
