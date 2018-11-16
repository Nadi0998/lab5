DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lab5',
        'USER': 'dbuser',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': 3306,  # Стандартный порт MySQL
        'OPTIONS': {'charset': 'utf8'},
        'TEST_CHARSET': 'utf8',
    }
}
