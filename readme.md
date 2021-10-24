[python3]: https://www.python.org/downloads/release/python-397/
[PostgreSQL]: https://www.postgresql.org/

# My Pantry Saver

A Web-App that helps user plan out their weekly meal plan, helping them buy ingredients and guiding them on how to prepare and cook their weekly dishes

# Dependeicies
- `Python 3.9.7`
- `Django 3.2.6`
- `psycopg2 2.9.1`

# Installation
#### Install [Python 3.9.7][python3] :

```
https://www.python.org/downloads/release/python-397/
```

##### Install packages
The dependendencies are listed in requirements.txt and can be installed via:
```
python -m pip install -r requirements.txt
```

# First time setup
By default, My Pantry Saver uses sqlite3 as its primary database

##### Creating the relational database (Making migrations)
```
python manage.py makemigrations ingredient recipe user
```

##### Migrating
```
python manage.py migrate
```

##### If you want to run the application using a 3rd party database, (In this example, we will use [PostgreSQL][PostgreSQL])
Navigate to `~/my_pantry_saver/settings.py`

In line 83-96, modify the database settengs, removing the default database adapter and setting the primary adapter as a default

```
DATABASES = {
    'postgres': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{YOUR DB NAME}}',
        'USER': '{YOUR DB USER}}',
        'PASSWORD': '{YOUR USER PASSWORD}',
        'HOST': '{localhost OR CUSTOM IP}',
        'PORT': 'DEFAULT = 5432',
    },
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

An example of a modified database settings


```
DATABASES = {
    'defailt': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'my_pantry_saver',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

# Running the application
```
python manage.py runserver
```

# Guides

#### Heading to the my-pantry page

1. Head to `http://127.0.0.1:8000/`
2. Log-in or create an account
3. The app will bring you to the my-pantry page

### The following guides is meant for administrators and is not meant for users to access

#### Adding a new Ingredient

1. Head to `http://127.0.0.1:8000/ingredients/`
2. Click on “Add New Ingredient”
3. Enter ingredient details and press submit.

#### Adding a new Recipe

1. Head to `http://127.0.0.1:8000/recipes/`
2. Click on **Add New Recipe**
3. Enter recipe details and press **submit**.

#### Attaching Ingredients to a Recipe

1. Head to `http://127.0.0.1:8000/recipes/`
2. Find the Recipe and click on **View** next to the recipe name.
3. Click on **Add ingredient**
4. Enter details for an ingredient
5. Repeat step 3 until all ingredients are added.
