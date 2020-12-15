import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess-2'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ...
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_DONMAIN = os.environ.get('MAIL_DONMAIN')
    MAIL_FROM = os.environ.get('MAIL_FROM')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['hoangtrongminh@luvina.net', 'nguyenxuantruong@luvina.net']

    DATA_MAIL_CC = os.environ.get('DATA_MAIL_CC') or 'mail'
    DATA_TITLE_MAIL = os.environ.get('DATA_TITLE_MAIL') or '[Test] mail'
    DATA_CURR_PATH = os.environ.get('DATA_CURR_PATH') or '/var/www/html/vpn_app/data'
    DATA_CURR_PATH_DESKTOP = os.environ.get('DATA_CURR_PATH_DESKTOP') or './data'
    DATA_FILE_TEST_ENABLE = eval(os.environ.get('DATA_FILE_TEST_ENABLE') or True)
    DATA_FILE_TEST = os.environ.get('DATA_FILE_TEST') or "test.txt"
    DATA_FILE_HUONGDAN_ENABLE = eval(os.environ.get('DATA_FILE_HUONGDAN_ENABLE') or False)
    DATA_FILE_HUONGDAN = os.environ.get('DATA_FILE_HUONGDAN')
    DATA_FILE_OVPN_ENABLE = eval(os.environ.get('DATA_FILE_OVPN_ENABLE') or False)
    MAIL_SEND_FROM = os.environ.get('MAIL_SEND_FROM') or "test@luvina.net"
    MAIL_PASS = os.environ.get('MAIL_PASS') or ""

    #
    VPN_SRV_PROTOCOL = os.environ.get('VPN_SRV_PROTOCOL') or "udp"

    # ...
    POSTS_PER_PAGE = 25

    # ...
    LANGUAGES = ['en', 'vi']

    # ...
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
