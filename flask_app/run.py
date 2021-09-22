from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_restful import Api
from flask_script import Manager, Server

from api.items import ItemsAPI
from models.items import db
from views.main import main

# init app
app = Flask(__name__)

# add config prorpeties.
app.config.from_object('config.default')

# init app to sqlalchemy.
db.init_app(app)

# init restful API
api_manager = Api(app)
api_manager.add_resource(
    ItemsAPI,
    '/api/items', '/api/items/',
    '/api/items/<int:id>'
)
# Register Blueprint
app.register_blueprint(main)

# Add app to manager
manager = Manager(app)

# Add alembic migration
Migrate(app, db)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host='localhost', port=5050))


if __name__ == '__main__':
    manager.run()
