class Config(object):
    pass

class DevConfig(Config):
    debug = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///maths_mcq.db'
    SQLALCHENY_BINDS = {'db2':'sqlite:///science_mcq.db'}
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '22d4fb45bbc83ff39bca1e2226ab6a64905ab503f104f4f8'
    SESSION_PERMANENT = False
    SESSION_TYPE = 'filesytem'
    
    
    class ProdConfig(Config):
        pass