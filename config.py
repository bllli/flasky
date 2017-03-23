# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    WEBSITE_NAME = 'MyFlasky'
    SECRET_KEY = os.environ.get('SECRET_KEY') or '2B|!2B, there is a question'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # Email stuff
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'your email addr'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'your email passwd'
    # 邮箱密码是QQ邮箱的授权码, 需要在QQ邮箱单独申请

    # administrator's email account
    FLASKY_MAIL_SUBJECT_PREFIX = '[%s]' % WEBSITE_NAME
    FLASKY_MAIL_SENDER = MAIL_USERNAME + '@qq.com'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN') or 'your administrator email account'

    logfile = os.environ.get('LOG_FILE') or os.path.join(basedir, '%s.log' % WEBSITE_NAME)

    @classmethod
    def init_app(cls, app):
        import logging
        from logging import FileHandler, Formatter, getLogger
        logger = getLogger('werkzeug')
        file_handler = FileHandler(filename=cls.logfile, )
        file_handler.setLevel(logging.WARNING)
        file_handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s '))
        logger.addHandler(file_handler)
        app.logger.addHandler(file_handler)


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
