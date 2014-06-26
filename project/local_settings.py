DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'hausbud.db',                      # Or path to database file if using sqlite3.
        'AUTOCOMMIT': True,
        'ATOMIC_REQUESTS': True,
    }

}