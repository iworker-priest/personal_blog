# -*- coding: utf-8 -*-

class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True 

    @staticmethod
    def init_app(app):
        pass 

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456abcdef@192.168.72.171/myblog"

config = {
    'development' : DevelopmentConfig,
    'default'     : DevelopmentConfig
}