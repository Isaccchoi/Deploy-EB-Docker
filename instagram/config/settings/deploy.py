import random
import string

from .base import *

config_secret = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())
DEBUG = False

# AWS
AWS_ACCESS_KEY_ID = config_secret['aws']['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = config_secret['aws']['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = config_secret['aws']['S3_BUCKET_NAME']
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = 'ap-northeast-2'

# AWS Storage
STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'

# S3 FileStorage
DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
STATICFILES_STORAGE = 'config.storages.StaticStorage'

# DATABASE
DATABASES = config_secret['django']['databases']

# SECURITY KEY
SECRET_KEY = ''.join(
    [random.choice(string.ascii_lowercase) for i in range(40)]
)

# Allowed HOSTS
ALLOWED_HOSTS = [
    '.elasticbeanstalk.com',
    '.isaccchoi.com'
]
