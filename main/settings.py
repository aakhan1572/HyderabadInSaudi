

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = "django-insecure-^=o@(=*)%ntp+spzqv*&x@0)wqtgj+jl*niryfqlirix^-h@rf"
#SECRET_KEY = 'django-insecure-jen5vx9s)dry05=68_edf^v-_6h7dx)e7^#duo@8&)o2iwbv88'

from pathlib import Path
import dj_database_url
import os
import environ
env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),

)

# Take environment variables from .env file
environ.Env.read_env(BASE_DIR/'.env')
DEBUG= env('DEBUG')
SECRET_KEY= env('SECRET_KEY')
ALLOWED_HOSTS=['hyderabadinsaudi-production.up.railway.app','127.0.0.1']
#ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(' ')
#ALLOWED_HOSTS=['web-production-c07f.up.railway.app','127.0.0.1','localhost','https://web-production-8948.up.railway.app']
#ALLOWED_HOSTS=['web-production-c07f.up.railway.app','web-production-c07f.up.railway.app/','127.0.0.1','localhost']
#ALLOWED_HOSTS = ['https://www.hydinsaudi.com/', 'https://web-production-8948.up.railway.app/','https://web-production-9ba7.up.railway.app','127.0.0.1', 'localhost']

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django.contrib.humanize',
    "phonenumber_field",
    'sorl.thumbnail',
    'widget_tweaks',
    'django_filters',
    "django_htmx",
    "accounts",
    "categories",
    "expads",
    "vendor",
    "ads",
    "bbg",
    "storages",
    "django_extensions",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "main.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ['templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'expads.context_processors.menu_links',
                'accounts.context_processors.get_user_profile',                
            ],
        },
    },
]

WSGI_APPLICATION = "main.wsgi.application"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',                      
        'USER': 'postgres',
        'PASSWORD': 'lNeVsld6FcP7M60Ti6EP',
        'HOST': 'containers-us-west-36.railway.app',
        'PORT': '5876',
    }
}
#CSRF_TRUSTED_ORIGINS= ["https://web-production-c07f.up.railway.app"]

AUTH_USER_MODEL='accounts.User'
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'

STATIC_ROOT=BASE_DIR/'static'
STATICFILES_DIRS=['main/static']

STATIC_ROOT=os.path.join(BASE_DIR,"/static")
STATICFILES_DIRS=[os.path.join(BASE_DIR,"static")]

MEDIA_URL='/media/'
MEDIA_ROOT=BASE_DIR/'media'
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST=env('EMAIL_HOST')
EMAIL_PORT=587
EMAIL_HOST_USER=env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL= env('DEFAULT_FROM_EMAIL')
SECURE_CROSS_ORIGIN_OPENER_POLICY='same-origin-allow-popups'
DEFAULT_AUTO_FIELD="django.db.models.BigAutoField"


AWS_ACCESS_KEY_ID=env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY=env('AWS_SECRET_ACCESS_KEY')
AWS_S3_BUCKET_NAME=env('AWS_S3_BUCKET_NAME')
AWS_S3_REGION_NAME=env('AWS_S3_REGION_NAME')
AWS_STORAGE_BUCKET_NAME=env('AWS_STORAGE_BUCKET_NAME')
DEFAULT_FILE_STORAGE=env('DEFAULT_FILE_STORAGE')
STATICFILES_STORAGE=env('STATICFILES_STORAGE')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME


"""
DATABASES = {
    "default": dj_database_url.config(default=env("DATABASE_URL"), conn_max_age=1800,conn_health_checks=True),
}
ENGINE=django.db.backends.postgresql
DB_NAME=hydinsaudiaws
DB_USER=hydsuperuser
DB_PASSWORD=Slv$1572$$$   or Slv1572slv1572#
DB_HOST=hydinsaudiaws.ctznq7w54n8c.ap-south-1.rds.amazonaws.com
DB_PORT=5432


#SECURE_PROXY_SSL_HEADER= ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE= True
CSRF_COOKIE_SECURE= True
SECURE_CONTENT_TYPE_NOSNIFF= True
SECURE_BROWSER_XSS_FILTER= True
USE_X_FORWARDED_HOST=True
SECURE_SSL_REDIRECT= True
SECURE_HSTS_SECONDS= 31536000 
SECURE_HSTS_INCLUDE_SUBDOMAINS= True
SECURE_HSTS_PRELOAD= True

# SITE SECURITY (security)
SECURE_SSL_REDIRECT = False
if DEBUG is False:
    #SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    CSRF_COOKIE_SECURE = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SESSION_COOKIE_SECURE = True
    #USE_X_FORWARDED_HOST=True
    #X_FRAME_OPTIONS = 'DENY'
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000 # > 6 months (197 days)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    #DEFAULT_FILE_STORAGE = env('DEFAULT_FILE_STORAGE')
    AWS_ACCESS_KEY_ID=env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY=env('AWS_SECRET_ACCESS_KEY')
    AWS_S3_BUCKET_NAME=env('AWS_S3_BUCKET_NAME')
    AWS_S3_REGION_NAME=env('AWS_S3_REGION_NAME')
    AWS_STORAGE_BUCKET_NAME=env('AWS_STORAGE_BUCKET_NAME')
    DEFAULT_FILE_STORAGE=env('DEFAULT_FILE_STORAGE')
    STATICFILES_STORAGE=env('STATICFILES_STORAGE')
    #AWS_S3_CUSTOM_DOMAIN=env('AWS_S3_CUSTOM_DOMAIN')
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    #print(f"AWS_SECRET_ACCESS_KEY = {AWS_SECRET_ACCESS_KEY}")
    DATABASES = {
        "default": {
            'ENGINE': env('ENGINE'),
            'NAME': env('DB_NAME'),
            'USER': env('DB_USER'),
            'PASSWORD': env('DB_PASSWORD'),
            'HOST': env('DB_HOST'),
            "PORT": env("DB_PORT"),
        }
    }

else:
    SECURE_SSL_REDIRECT=False
    SESSION_COOKIE_SECURE=False
    CSRF_COOKIE_SECURE=False
    DATABASES = {
        "default": {
            'ENGINE': env('ENGINE'),
            'NAME': env('LDB_NAME'),
            'USER': env('LDB_USER'),
            'PASSWORD': env('LDB_PASSWORD'),
            'HOST': env('LDB_HOST'),
        }
    }"""

"""
#print(f"SECURE_SSL_REDIRECT = {SECURE_SSL_REDIRECT}")
#print(f"SECRET_KEY = {SECRET_KEY}")

#if DEBUG == True:
#    print('True')
#else:
#    print('False')


# Following setting for http 
# python manage.py runserver 8080

DEBUG=True
CORS_REPLACE_HTTPS_REFERER      = False
HOST_SCHEME                     = "http://"
SECURE_PROXY_SSL_HEADER         = None
SECURE_SSL_REDIRECT             = False
SESSION_COOKIE_SECURE           = False
CSRF_COOKIE_SECURE              = False
SECURE_HSTS_SECONDS             = None
SECURE_HSTS_INCLUDE_SUBDOMAINS  = False
SECURE_FRAME_DENY               = False
"""