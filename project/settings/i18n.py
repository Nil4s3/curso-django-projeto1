# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/
from . import BASE_DIR

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Cuiaba'

USE_I18N = True

USE_TZ = True

LOCALE_PATH = [
    BASE_DIR / 'locale',
]
