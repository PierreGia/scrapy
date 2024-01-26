apres avoir créer un clone du projet certaine etapes sont a réalisées pour que tout fonctionne.

En premier lieu il faut se placer dans l'environement virtuel avec la commande : .venv/Scripts/activate

Une fois dans l'environement virtuel il faut executer la commande pip freeze requirement.txt pour installer les packages necessaire

apres ca il faut créer une db mongodb si vou avez mongodb d'installer sur votre machine.

Ensuite il faut aller dans le fichier setting.py qui est dans le dossier quotes_scraper pour modifer la conexion a la db mongodb

il faut aller dans le fichier quotes_spider.py pour modifier les informations relative a l'envoi du mail donc dans le fichier a la ligne 15 au niveau de username pour mettre votre adrresse mail a vous, ensuite juste en dessous il faut changer le password pour votre mot de passe a vous pour cela aller dans les parametres de votre compte google ensuite aller dans securité puis validation en deux etapes puis mot de passe d'application puis enfin créer une nouvelle application pour avoir le mot de passe. et pour finir modifier la ligne 68 pour changer les informations du mail envoyer principalement l'envoyeur le receveur et le text du message.

apres ca il faut utiliser la commande cd quotes_scraper pour aller dans le dossier

ensuite une fois dans le dossier il faut utiliser la commande scrapy crawl quotes -L WARNING pour executer le scraper cela va créer une collection appelé quotes dans la db mongodb si vous avez mongodb d'installer mais aussi créer un fichier json contenant la collection quotes et cela envera un mail disant que le scraping a bien eu lieu.

ensuite dans le fichier app.py de l'api flask a la racine du projet il faut changer le chemin du fichier json pour qu'il corresponde a la ou il est dans le dossier.

apres ca il faut utiliser la utiliser la commande flask --app app run pour lancer l'api

utiliser la commande streamlit run streamlit_app.py pour lancer l'app streamlit