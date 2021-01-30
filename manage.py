
import os
from arc_application import create_app, db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_cors import CORS


app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
CORS(app, resources={r"*": {"origins": "*"}})

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@ manager.command
def run():
    app.run()


if __name__ == '__main__':
    manager.run()
