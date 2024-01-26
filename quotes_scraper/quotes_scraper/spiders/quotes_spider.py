import scrapy
import pymongo
from urllib.parse import urljoin
import json
from bson import ObjectId
from redmail import EmailSender

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com']

    email = EmailSender(
        host='smtp.gmail.com',
        port=587,
        username='pierregia13@gmail.com',
        password='pgny uwym bvwh npxj '
    )

    def parse(self, response):
        # Connexion à MongoDB
        client = pymongo.MongoClient(self.settings.get('MONGO_URI'))
        database = client[self.settings.get('MONGO_DATABASE')]

        # Extraire les citations et les auteurs
        for quote in response.css('div.quote'):
            text = quote.css('span.text::text').get()
            author = quote.css('small::text').get()
            tags = quote.css('div.tags a::text').getall()

            # Recherche du document existant dans la base de données
            existing_quote = database.quotes.find_one({'text': text, 'author': author})

            if existing_quote:
                # Si le document existe, mettez à jour les tags (ou d'autres champs selon vos besoins)
                database.quotes.update_one(
                    {'text': text, 'author': author},
                    {'$set': {'tags': tags}}
                )
                print(f'Document mis à jour : Text: {text}, Author: {author}, Tags: {tags}')

            else:
                # Si le document n'existe pas, insérez-le dans la base de données
                database.quotes.insert_one({
                    'text': text,
                    'author': author,
                    'tags': tags,
                })
                print(f'Document ajouté : Text: {text}, Author: {author}, Tags: {tags}')

        # Fermer la connexion à MongoDB
        client.close()

        # Trouver le lien vers la page suivante
        next_page = response.css('li.next a::attr(href)').get()

        # Si le lien vers la page suivante existe, créer une nouvelle requête
        if next_page:
            # Construire l'URL complète
            next_page_url = urljoin(response.url, next_page)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
        else:
            # Toutes les pages ont été traitées, générer un fichier JSON
            self.generate_json_file()

    def generate_json_file(self):
        # Connexion à MongoDB
        client = pymongo.MongoClient(self.settings.get('MONGO_URI'))
        database = client[self.settings.get('MONGO_DATABASE')]

        # Récupérer toutes les citations depuis la collection 'quotes'
        all_quotes = list(database.quotes.find())

        # Fermer la connexion à MongoDB
        client.close()

        # Convertir les ObjectId en chaînes de caractères
        for quote in all_quotes:
            quote['_id'] = str(quote['_id'])

        # Écrire les données dans un fichier JSON
        with open('quotes.json', 'w', encoding='utf-8') as json_file:
            json.dump(all_quotes, json_file, ensure_ascii=False, indent=2)
