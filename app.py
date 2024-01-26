from flask import Flask, jsonify
import random
import json
import logging

from flask_cors import CORS

app = Flask(__name__)
logging.basicConfig(filename='app.log', level=logging.INFO)
CORS(app)




# Charger le fichier JSON
with open(r'scrapy\quotes_database.quotes.json', 'r', encoding='utf-8') as file:
    quotes_data = json.load(file)


@app.route('/random_quote', methods=['GET'])
def random_quote():
    # Récupérer une citation aléatoire depuis la liste des citations chargées depuis le fichier JSON
    random_quote = random.choice(quotes_data)

    # Formater les données pour la réponse JSON
    result = {
        'text': random_quote['text'],
        'author': random_quote['author'],
        'tags': random_quote['tags'],
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
