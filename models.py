from flask_sqlalchemy import SQLAlchemy
from settings import ( DB_NAME, DB_USER, DB_PASSWORD, RENDER_DB_HOST, RENDER_DB_NAME,  
                     RENDER_DB_PASSWORD, RENDER_DB_USER)
              
database_host = 'localhost:5432'
#database_path = f'postgresql://{DB_USER}:{DB_PASSWORD}@{database_host}'

db= SQLAlchemy()

"""
setup_db(app)
    binds a flask application and a SQLAlchemy service
"""

def get_database_uri():
    # Check if Render DB details are available
    if RENDER_DB_HOST and RENDER_DB_NAME and RENDER_DB_USER and RENDER_DB_PASSWORD:
        # Use Render database URI
        database_path = f'postgresql://{RENDER_DB_USER}:{RENDER_DB_PASSWORD}@{RENDER_DB_HOST}:5432/{RENDER_DB_NAME}'
    else:
        # Fall back to local database URI
        database_path = f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost:5432/{DB_NAME}'
    return database_path

def setup_db(app):
    database_path = get_database_uri() 
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

 # Movie class.
class Movies(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    title = db.Column(db.String(120))
    releasedate = db.Column(db.Date,nullable=False)
    actors = db.relationship('Actors',backref='Movieid',lazy=True)
    
# Actor class.

class Actors(db.Model):
    __tablename__ = 'actors'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(120))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id',ondelete='CASCADE'),nullable=False)
