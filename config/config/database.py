from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
sqliteDesarrollo = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'juggertmitoDesarrollo.sqlite3',
    }
}

sqlitePrueba = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'juggertmitoprueba.sqlite3',
    }
}


sqliteProducion = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'juggertmitoproduccion.sqlite3',
    }
}