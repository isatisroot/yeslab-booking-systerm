"""
Django settings for bookingSysterm project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sys,datetime
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 添加导包路径

sys.path.insert(0,os.path.join(BASE_DIR,'users'))
# print(sys.path)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7e&-rc(ku-i33k*%0+5ftqlk7)foz)+*ilebu1susbef#7454o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1","183.6.116.44"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'users.apps.UsersConfig',
    'infos.apps.InfosConfig',
    'experiments.apps.ExperimentsConfig',
    'courses.apps.CoursesConfig',
    # 允许跨域
    'corsheaders',
    'rest_framework',
    'django_crontab',  # 定时任务

    # 配置后台管理系统
    'xadmin',
    'crispy_forms',
    'reversion',

]

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'bookingSysterm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bookingSysterm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

class DBS():
    def __init__(self,DEBUG):
        self.DEBUG=DEBUG
        self.formal_db = {
            "ENGINE": "django.db.backends.mysql",
            "HOST": os.getenv("MYSQL_HOST", "172.99.0.4"),
            "PORT": os.getenv("MYSQL_PORT", 3306),
            "USER": os.getenv("MYSQL_USER", "root"),
            "PASSWORD": os.getenv("MYSQL_PWD", "0.0010.0"),
            "NAME": os.getenv("MYSQL_NAME", "yeslab_db"),
        }
        self.test_db = {
            "ENGINE": "django.db.backends.mysql",
            "HOST": os.getenv("MYSQL_HOST", "192.168.92.149"),
            "PORT": os.getenv("MYSQL_PORT", 3306),
            "USER": os.getenv("MYSQL_USER", "root"),
            "PASSWORD": os.getenv("MYSQL_PWD", "mysql"),
            "NAME": os.getenv("MYSQL_NAME", "userinfo"),
        }
        self.lj_db = {
            "ENGINE": "django.db.backends.mysql",
            "HOST": os.getenv("MYSQL_HOST", "192.168.2.161"),
            "PORT": os.getenv("MYSQL_PORT", 3306),
            "USER": os.getenv("MYSQL_USER", "root"),
            "PASSWORD": os.getenv("MYSQL_PWD", "0.0010.0"),
            "NAME": os.getenv("MYSQL_NAME", "yeslab_db"),
        }

    def default_db(self):
        if self.DEBUG:
            if os.getenv("DB_NAME") == "lj":
                return self.lj_db
            else:
                return self.test_db
        else:
            return self.formal_db

dbs = DBS(DEBUG)

DATABASES = {
    "default": dbs.default_db()
}

uri = "redis://192.168.2.161:6379" if os.getenv("DB_NAME")=="lj" else "redis://192.168.92.149:6379"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "%s/0"%os.getenv("REDIS_URI",uri),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "%s/1"%os.getenv("REDIS_URI",uri),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "verify": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "%s/2"%os.getenv("REDIS_URI",uri),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "email": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "%s/3"%os.getenv("REDIS_URI",uri),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR,"static")


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
}

# 定时任务
"""
* * * * *
分 时 日 月 周      命令
M: 分钟（0-59）。每分钟用*或者 */1表示
H：小时（0-23）。（0表示0点）
D：天（1-31）。
m: 月（1-12）。
d: 一星期内的天（0~6，0为星期天）。
"""
# CRONJOBS = [
#     # 每天０点执行一次
#     ('* 0 1 * *', 'scripts.gen_reservation_table.main','>>/home/python/Desktop/yeslab-booking-systerm/backend/logs/generate.log')
# ]

# 解决crontab中文问题
# CRONTAB_COMMAND_PREFIX = 'LANG_ALL=zh_cn.UTF-8'

# 邮件设置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.exmail.qq.com'
EMAIL_PORT = 465
#发送邮件的邮箱
EMAIL_HOST_USER = 'Chensy@yeslab.net'
#在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = 'Csy727167175'
#收件人看到的发件人
EMAIL_FROM = 'python<admin@yeslab.net>'


# 权限认证
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',   # 基本认证
        # 'rest_framework.authentication.SessionAuthentication',  # session认证
    )
}