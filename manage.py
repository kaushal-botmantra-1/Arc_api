
import os
from arc_application import create_app, db
from flask_cors import CORS


app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
CORS(app, resources={r"*": {"origins": "*"}})

app.app_context().push()


if __name__ == '__main__':
    app.run(host=app.config["HOST"], port=app.config["PORT"])
