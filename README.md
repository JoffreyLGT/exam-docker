# Examen Docker Joffrey Lagut

## Tests sur l'API

Le fichier tests.py permet de lancer les tests sur l'API.

### Liste des commandes permettant de réaliser les tests

#### Permissions : `perm.test.py`

Permissions de Alice
```shell
python perm.test.py  -a 127.0.0.1 -p 8000 -s 200 -l alice --password wonderland
```

Permissions de Bob
```shell
python perm.test.py  -a 127.0.0.1 -p 8000 -s 200 -l bob --password builder
```

Persmissions de Clémentine
```shell
python perm.test.py  -a 127.0.0.1 -p 8000 -s 403 -l clementine --password mandarine
```

#### Authorization : `auth.test.py`
```shell
python auth.test.py  -a 127.0.0.1 -p 8000 -s 200 -v 1 -l alice --password wonderland --sentence "life sucks"
python auth.test.py  -a 127.0.0.1 -p 8000 -s 200 -v 2 -l alice --password wonderland --sentence "life sucks"
python auth.test.py  -a 127.0.0.1 -p 8000 -s 200 -v 1 -l bob --password builder --sentence "life sucks"
python auth.test.py  -a 127.0.0.1 -p 8000 -s 403 -v 2 -l bob --password builder --sentence "life sucks"
```

#### Sentiment : `sentiment.test.py`

```sheel
python sentiment.test.py  -a 127.0.0.1 -p 8000 -v 1 -r 1 -l alice --password wonderland --sentence "life is beautiful"
python sentiment.test.py  -a 127.0.0.1 -p 8000 -v 2 -r 1 -l alice --password wonderland --sentence "life is beautiful"
python sentiment.test.py  -a 127.0.0.1 -p 8000 -v 2 -r 0 -l alice --password wonderland --sentence "life sucks"
python sentiment.test.py  -a 127.0.0.1 -p 8000 -v 1 -r 0 -l alice --password wonderland --sentence "life sucks"
```
