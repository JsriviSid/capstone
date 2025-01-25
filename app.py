import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import func
from sqlalchemy.exc import ( SQLAlchemyError,IntegrityError, 
                            OperationalError, DataError)
from models import Actors, Movies, db, setup_db
from auth import AuthError, requires_auth

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    if test_config is None:
        setup_db(app)
    else:
        database_path = test_config.get('SQLALCHEMY_DATABASE_URI')
        setup_db(app, database_path=database_path)
    CORS(app)
    
    # Endpoint to get movie details
    @app.route('/movies')
    @requires_auth(permission='get:movie')
    def get_movie(payload):
        try:
            movies = Movies.query.with_entities(Movies.id,
                                                Movies.title,
                                                Movies.releasedate).all()
            formatted_movie= []
            for movie in movies:
                formatted_movie.append({
                    'id':movie.id,
                    'title':movie.title,
                    'Releasedate':movie.releasedate
                })
            print(formatted_movie)
            return jsonify(formatted_movie)

        except Exception as e:
            print(f"Error occurred: {str(e)}")
            return jsonify({
                'success': False,
                'error': 'Could not retrieve movies.'
            }), 500
        
    # Endpoint to get Actor details
    @app.route('/actors')
    @requires_auth(permission='get:actor')
    def get_actors(payload):
        try:
            actors = Actors.query.all()
            formatted_actor= []
            for actor in actors:
                formatted_actor.append({
                    'Id':actor.id,
                    'Name':actor.name,
                    'Age':actor.age,
                    'Gender':actor.gender,
                    'Movie-id':actor.movie_id
                })
            return jsonify(formatted_actor)

        except Exception as e:
            print(f"Error occurred: {str(e)}")
            return jsonify({
                'success': False,
                'error': 'Could not retrieve actors.'
            }), 500
        
    #End point to add new movies

    @app.route('/addmovie', methods=["POST"])
    @requires_auth(permission='add:movie')
    def add_movie(payload):
        body = request.get_json()
        new_title = body.get("title", None)
        new_releasedate = body.get("releasedate", None)

        try:
            new_movie = Movies(title=new_title, releasedate=new_releasedate)
            db.session.add(new_movie)
            db.session.commit()

            return jsonify({"success": True
                            })
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            return jsonify({
                'success': False,
                'error': 'Could not able to add the given movie.'
            }), 500
        
    #End point to add new actors
    @app.route('/addactor', methods=["POST"])
    @requires_auth(permission='post:actor')
    def add_actor(payload):
        body = request.get_json()
        new_name = body.get("name", None)
        new_age = body.get("age", None)
        new_gender = body.get("gender", None)
        new_movie_id = body.get("movie_id", None)

        try:
            new_actor = Actors(name=new_name, age=new_age,
                               gender=new_gender,movie_id=new_movie_id)
            db.session.add(new_actor)
            db.session.commit()

            return jsonify({"success": True
                            })
        
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            return jsonify({
                'success': False,
                'error': 'Could not able to add the given actor.'
            }), 500
        
    #End point to delete movie 
    @app.route('/removemovie/<id>', methods=["GET", "DELETE"])
    @requires_auth(permission='delete:movie')
    def delete_movie(payload,id):
        try:
            movie = Movies.query.filter(Movies.id == id).one_or_none()
            #checking if given movie id is existing, else prompt error
            if movie is None:
                abort(404)

            db.session.delete(movie)
            db.session.commit()

            return jsonify({"success": True,
                            "id removed": id
                            })
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            return jsonify({
                'success': False,
                'error': 'Could not able to delete movie.'
            }), 500
        
    #End point to delete actor 
    @app.route('/removeactor/<id>', methods=["GET", "DELETE"])
    @requires_auth(permission='delete:actor')
    def delete_actor(payload,id):
        try:
            actor = Actors.query.filter(Actors.id == id).one_or_none()
            #checking if given actor id is existing, else prompt error
            if actor is None:
                abort(404)

            db.session.delete(actor)
            db.session.commit()

            return jsonify({"success": True,
                            "id removed": id
                            })
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            return jsonify({
                'success': False,
                'error': 'Could not able to delete actor.'
                }), 500
    
    #End point to update actor details 
    @app.route('/updateactor/<id>', methods=["PATCH", "GET"])
    @requires_auth(permission='patch:actor')
    def update_actor(payload,id):
        body = request.get_json()
        if body is None:
          return jsonify({"error": "Invalid or empty JSON body"}), 400
        new_name = body.get("name")
        new_age = body.get("age")
        new_gender = body.get("gender")
        new_movie_id = body.get("movie_id")

        if not new_name or not new_age or not new_gender or not new_movie_id:
            return jsonify({"error": "valueerror - missing required input fields"
                            }), 400

        try:
            actor=Actors.query.filter(Actors.id == id).one_or_none()

            # check whether actor data is existing in DB, else prompt error
            if actor is None:
              abort(404)

            actor.name=new_name
            actor.age=new_age
            actor.gender=new_gender
            actor.movie_id=new_movie_id 
            # DB commit the updated row
            db.session.commit()

            return jsonify({"success": True
                            })
        
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            return jsonify({
                'success': False,
                'error': 'Could not able to update the given actor.'
            }), 500
        
    #End point to update movie details 
    @app.route('/updatemovie/<id>', methods=["PATCH", "GET"])
    @requires_auth(permission='patch:movie')
    def update_movie(payload,id):
        body = request.get_json()
        if body is None:
          return jsonify({"error": "Invalid or empty JSON body"}), 400
        new_title = body.get("title")
        new_releasedate = body.get("releasedate")

        if not new_title or not new_releasedate:
            return jsonify({"error": "valueerror - missing required input fields"
                            }), 400

        try:
            movie=Movies.query.filter(Movies.id == id).one_or_none()

            # check whether movie data is existing in DB, else prompt error
            if movie is None:
              abort(404)

            movie.title=new_title
            movie.releasedate=new_releasedate
 
            # DB commit the updated row
            db.session.commit()

            return jsonify({"success": True
                            })
        
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            return jsonify({
                'success': False,
                'error': 'Could not able to update the given movie details.'
            }), 500
    
    # Error handlers 
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
          "success": False,
          "error": 422,
          "message": "unprocessable"
         }), 422
    
    # 405 error handler
    @app.errorhandler(405)
    def methodnotfound(error):
        return jsonify({
          "success": False,
          "error": 405,
          "message": "Method is wrong"
         }), 405

    # 404 error handler 
    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 404,
                    "message": "resource not found"}),
            404,
        )

    #Error handler for auth - errors
    @app.errorhandler(AuthError)
    def handle_auth_error(error):
        print(f"AuthError raised: {error}")
        response = jsonify({
          'success': False,
          'error': error.status_code,
          'code':error.error.get('code',' uncaptured error'),
          'description':error.error.get('description','uncaught error occured')
        })
        response.status_code = error.status_code
        return response

    return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port= 10000, debug=True)