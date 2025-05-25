from flask import Flask
from flasgger import Swagger
from .db import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emp.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    Swagger(app) # Enable Swagger UI
    db.init_app(app)

    #Register employee routes
    from  app.routes.employee_routes import employee_bp
    app.register_blueprint(employee_bp, url_prefix="/employees")

    with app.app_context():
        db.create_all()

    return app
