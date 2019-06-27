import os

PYTHON_ENV = os.environ.get('PYTHON_ENV', 'development')
TOKEN = os.environ.get('TOKEN', '12345')

if PYTHON_ENV == 'docker':
    DB_DATABASE = os.getenv('DB_DATABASE', 'face_api_test_db')
    DB_HOST = os.getenv('DB_HOST', 'postgresql')
    DB_USER = os.getenv('DB_USER', 'postgres')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '')
    DB_PORT = os.getenv('DB_PORT', 5432)
    API_HOST = os.getenv('API_HOST', '0.0.0.0')
    API_PORT = os.getenv('API_PORT', 8463)
    TIME_CACHE = float(os.environ.get('TIME_CACHE', 600))
elif PYTHON_ENV == 'development':
    DB_DATABASE = 'face_api_test_db'
    DB_HOST = '0.0.0.0'
    DB_USER = 'postgres'
    DB_PASSWORD = ''
    DB_PORT = 5432
    API_HOST = '0.0.0.0'
    API_PORT = 8463
    TIME_CACHE = 30
else:
    raise ("Unknown environment " + PYTHON_ENV)

config = {
    "host": API_HOST,
    "port": API_PORT
}

CROP_SIZE = 25

USE_GPU = False
GPU_USAGE = 0.3

CREATE_PROFILE_IF_NOT_EXIST = False
