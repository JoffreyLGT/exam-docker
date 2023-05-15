# Examen Docker Joffrey Lagut

## Setup

- Ouvrir un terminal et se placer dans le dossier du projet
- Saisir la commande `docker-compose up`
- Vérifier le contenu du fichier `logs/api_logs`

## Description du projet

Ce projet va créer 4 conteneurs : un pour l'api et un par type de test à effectuer.  
Les sous-dossier `api`, `auth`, `perm` et `sentiment` contiennent les fichiers permettant de créer les images des conteneurs.  
Le sous-dossier `logs` contient les logs des tests exécutés.

## Liste des commandes permettant de réaliser les tests

### Permissions : `perm.test.py`

```shell
python perm.test.py  -a 127.0.0.1 -p 8000 -s 200 -l alice --password wonderland
python perm.test.py  -a 127.0.0.1 -p 8000 -s 200 -l bob --password builder
python perm.test.py  -a 127.0.0.1 -p 8000 -s 403 -l clementine --password mandarine
```

### Authorization : `auth.test.py`

```shell
python auth.test.py  -a 127.0.0.1 -p 8000 -s 200 -v 1 -l alice --password wonderland --sentence "life sucks"
python auth.test.py  -a 127.0.0.1 -p 8000 -s 200 -v 2 -l alice --password wonderland --sentence "life sucks"
python auth.test.py  -a 127.0.0.1 -p 8000 -s 200 -v 1 -l bob --password builder --sentence "life sucks"
python auth.test.py  -a 127.0.0.1 -p 8000 -s 403 -v 2 -l bob --password builder --sentence "life sucks"
```

### Sentiment : `sentiment.test.py`

```sheel
python sentiment.test.py  -a 127.0.0.1 -p 8000 -v 1 -r 1 -l alice --password wonderland --sentence "life is beautiful"
python sentiment.test.py  -a 127.0.0.1 -p 8000 -v 2 -r 1 -l alice --password wonderland --sentence "life is beautiful"
python sentiment.test.py  -a 127.0.0.1 -p 8000 -v 2 -r 0 -l alice --password wonderland --sentence "life sucks"
python sentiment.test.py  -a 127.0.0.1 -p 8000 -v 1 -r 0 -l alice --password wonderland --sentence "life sucks"
```
