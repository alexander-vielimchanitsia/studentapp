import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'students_db',
        'USER': 'students_db_user',
        'PASSWORD': 'admin',
        'HOST': '127.0.0.1',
    }
}