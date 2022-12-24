from flask import Flask
from flask_restplus import Api

def create_app():
    from backend.api_case import api_namespace
    from backend.admin_case import admin_namespace

    application = Flask(__name__)
    api = Api(application, version='0.1', title='Books backend API',
              description='CRUD API')

    from backend.db import db, db_config
    application.config['RESTPLUS_MASK_SWAGGER'] = False
    application.config.update(db_config)
    db.init_app(application)
    application.db = db

    api.add_namespace(api_case)
    api.add_namespace(admin_case)

    return application