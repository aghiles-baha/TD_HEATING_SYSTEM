# TD_HEATING_SYSTEM
Ce TD permet de mettre en pratique toutes les notions vu en cours sur Git, Python, Test et Docker.



## Exercice 2 — Procédure interactive (test manuel)

Ces commandes permettent de tester manuellement l'insertion et la lecture dans MongoDB.

```bash
# 1. Lancer MongoDB
docker run -d --name mongodb --network mynet mongo

# 2. Lancer un conteneur Python interactif
docker run -it --name python-mongo --network mynet python:alpine sh

# 3. Dans le conteneur, installer pymongo
pip install pymongo

# 4. Lancer Python et insérer un document
python
```

```python
from pymongo import MongoClient

client = MongoClient(host="mongodb")
db = client["heating_db"]
col = db["equipements"]

col.insert_one({"type": "Chaudiere", "annee": 2005, "puissance": 20})
print(col.find_one())
```
