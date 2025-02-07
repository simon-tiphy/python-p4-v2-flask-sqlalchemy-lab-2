# from flask import Flask
# from flask_migrate import Migrate

# from models import db

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# migrate = Migrate(app, db)

# db.init_app(app)


# @app.route('/')
# def index():
#     return '<h1>Flask SQLAlchemy Lab 2</h1>'


# if __name__ == '__main__':
#     app.run(port=5555, debug=True)



from flask import Flask
from flask_migrate import Migrate
from sqlalchemy import inspect

from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route('/')
def index():
    return '<h1>Flask SQLAlchemy Lab 2</h1>'


@app.cli.command('list-tables')
def list_tables():
    """Custom CLI command to list tables in the database."""
    with app.app_context():
        inspector = inspect(db.engine)
        print("Tables in the database:", inspector.get_table_names())


if __name__ == '__main__':
    app.run(port=5555, debug=True)