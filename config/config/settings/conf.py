import os

from dotenv import load_dotenv


load_dotenv()

DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')

SECRET_KEY = os.environ.get('SECRET_KEY')

STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY')
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
USD_SECRET_KEY = os.environ.get('USD_SECRET_KEY')
EUR_SECRET_KEY = os.environ.get('EUR_SECRET_KEY')
