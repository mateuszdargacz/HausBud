DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'hausbud',                      # Or path to database file if using sqlite3.
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',                      # Empty for localhost through$
        'PORT': '',
        'OPTIONS': {
         "init_command": "SET foreign_key_checks = 0;",
    },
    }

}