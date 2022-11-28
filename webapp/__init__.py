from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DevConfig

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    from .views.home import home_bp
    from .views.quizz import quizz_bp
    #...
    #...
    #...
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(DevConfig)

    
    db.init_app(app)
    migrate.init_app(app,db)

    app.register_blueprint(home_bp)
    app.register_blueprint(quizz_bp)


    return app