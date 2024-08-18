# Application definition
INSTALLED_APPS = [
    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # CORS Headers
    'corsheaders',

    # Django Rest Framework
    'rest_framework_simplejwt',
    'rest_framework',
    # Apps
    'recipes',
    'authors',
    'tag',
]
