# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

from . import BASE_DIR

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# python manage.py makemessages -l "pt_BR" -i 'venv'
# python manage.py compilemessages -l "pt_BR" -i 'venv'
