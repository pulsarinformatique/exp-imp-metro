# STARTER IMP/EXP PYTHON

Ce projet est une application/outil/programme qui utilise Python pour interagir avec une base de données, effectuer du web scraping et bien plus encore.

## Fonctionnalités

- Interagir avec une base de données MySQL à l'aide de mysql-connector-python.
- Effectuer le web scraping avec beautifulsoup4 pour extraire des données à partir de pages HTML.
- Utiliser requests pour obtenir des données à partir d'URLs.
- Utiliser openpyxl pour travailler avec des fichiers Excel.

## Installation

Cloner ce dépôt vers votre machine locale :

```bash
git clone https://github.com/stackyagency/starter-python-import-export
cd starter-python-import-export
```

## Créer et activer l'environnement virtuel :

#### Sur macOS/Linux :

```bash
python -m venv venv
source venv/bin/activate
```

#### Sur Windows :

```bash
python -m venv venv
venv\Scripts\activate
```

## Installer les dépendances :

```bash
pip install -r requirements.txt
```

## Configurer la base de données :

Assurez-vous d'avoir MySQL installé. (WPLOCAL, WAMP, XAMPP ...)
Créez une base de données et un utilisateur pour l'application.

#### Problème de droit

Si vous rencontrez des soucis lié aux autorisations, depuis votre base de donnée :

```sql
CREATE USER 'root'@'%' IDENTIFIED BY 'some_pass';GRANT ALL PRIVILEGES ON *.* TO 'root'@'%';
FLUSH PRIVILEGES;
```

## Configuration

Avant de lancer le projet, assurez-vous de configurer correctement votre environnement dans le fichier script.py :

#### Pour trouver le port de votre application :

```bash
mysql -e "SHOW VARIABLES WHERE Variable_name = 'port';"
```

```python
connection_config = {
        "development": {
            "host": "localhost",
            "database": "local",
            "user": "main",
            "password": "main",
            "port": 10043,
        },
        "production": {
            "host": "database.example.com",
            "database": "production",
            "user": "prod_user",
            "password": "prod_password",
            "port": 3306,
        },
    }
```

### Lancer le projet :

```bash
python main.py
```
