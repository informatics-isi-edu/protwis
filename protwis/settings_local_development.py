# local settings
# override these settings by copying and editing this file to protwis/settings_local.py

# Site specific constants
SITE_NAME = 'gpcr' # used for site specific files
SITE_TITLE = 'GPCRdb' # for display in templates
DATA_DIR = '/protwis/data/protwis/' + SITE_NAME
BUILD_CACHE_DIR = DATA_DIR + '/cache'
DEFAULT_NUMBERING_SCHEME = 'gpcrdb'
DEFAULT_PROTEIN_STATE = 'inactive'
REFERENCE_POSITIONS = {'TM1': '1x50', 'ICL1': '12x50', 'TM2': '2x50', 'ECL1': '23x50', 'TM3': '3x50', 'ICL2': '34x50',
    'TM4': '4x50', 'ECL2': '45x50', 'TM5': '5x50', 'TM6': '6x50', 'TM7': '7x50', 'H8': '8x50'}
DOCUMENTATION_URL = 'http://docs.gpcrdb.org/'

# Analytics
GOOGLE_ANALYTICS_KEY = False

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
          'OPTIONS': {
                'options': '-c search_path=protwis_schema'
            },
        'NAME': '_ermrest_95tv-YdSQC2VyrhXWudhZQ',
    }
}


# Quick-start development settings - unsuitable for production

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-eqrx61@n*z3y1mc1w_@x1+yo(@^!k7i-vjaz0tx1$902a!4mu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ['127.0.0.1', 'localhost','gpcr-dev.misd.isi.edu','128.9.132.104','128.9.128.243','div20-anoopk.isi.edu']
ALLOWED_HOSTS = ['*']
