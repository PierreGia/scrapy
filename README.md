apres avoir créer un clone du projet certaine etapes sont a réalisées pour que tout fonctionne.

En premier lieu il faut se placer dans l'environement virtuel avec la commande : .venv/Scripts/activate

Une fois dans l'environement virtuel il faut executer la commande pip freeze requirement.txt pour installer les packages necessaire

apres ca il faut créer une db mongodb si vou avez mongodb d'installer sur votre machine.

Ensuite il faut aller dans le fichier setting.py qui est dans le dossier quotes_scraper pour modifer la conexion a la db mongodb

apres ca il faut utiliser cd quotes_scraper pour aller dans le dossier

ensuite une fois dans le dossier il faut utiliser la commande scrapy crawl quotes -L WARNING pour executer le scraper cela va créer une collection appelé quotes dans la db mongodb si vous avez mongodb d'installer mais aussi créer un fichier json contenant la collection quotes

ensuite dans le fichier app.py de l'api flask a la racine du projet il faut changer le chemin du fichier json pour qu'il corresponde a la ou il est dans le dossier.

apres ca il faut utiliser la utiliser la commande flask --app app run pour lancer l'api

utiliser la commande streamlit run streamlit_app.py pour lancer l'app streamlit