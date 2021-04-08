import os

BASE_DIR = os.path.dirname(__file__)

#SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_DATABASE_URI = 'oracle+cx_oracle://admin:!$Khu20022002@dboracle_high'
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "dev"