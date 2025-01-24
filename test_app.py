import os
import unittest
import json
from unittest.mock import MagicMock
from app import create_app
from models import Actors, Movies, db, setup_db
from settings import TESTDB_NAME, TESTDB_USER, TESTDB_PASSWORD

class capstoneTestCase(unittest.TestCase):
    """This class represents the test cases"""
    def setUp(self):
        """Define test variables and initialize app."""
        self.database_name=TESTDB_NAME
        self.database_user=TESTDB_USER
        self.database_password=TESTDB_PASSWORD
        self.database_host = "localhost:5432"
        self.database_path = f"postgresql://{self.database_user}:{self.database_password}@{self.database_host}/{self.database_name}"
        #self.database_path = f"postgresql://{self.database_user}:{self.database_password}@{self.database_host}"

        # Create app with the test configuration
        self.client = create_app({
            "SQLALCHEMY_DATABASE_URI": self.database_path,
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
            "TESTING": True
        })
        self.client = self.client.test_client()
        # Bind the app to the current context and create all tables
        #with self.client.application.app_context():
          #db.create_all()

    def tearDown(self):
        """Executed after each test"""
        #with self.client.application.app_context():
         # db.session.remove()
          #db.drop_all()
        pass

    # tests for Get movie endpoint
    def test_get_movies(self):
        required_auth = MagicMock()
        required_auth.return_value = None
        res = self.client.get("/movies",headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVYSU5MY2s1a1VzSGNOYUxCTU1TZiJ9.eyJpc3MiOiJodHRwczovL2Rldi1wMmNoZnlvN3Zydmdwa3FtLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NzkyMmQ5NTkzMGRlMDcwOWY2MmI4YmMiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTczNzczNzczMCwiZXhwIjoxNzM3ODI0MTI4LCJzY29wZSI6IiIsImF6cCI6Im9XeFVwUzJzejlBRUoyaVVVQ1Q2N0s2NXRGNGt1TUZtIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIl19.I0VgHKAIbnken8Ykumy5MaBcQI2uV3OL0UWpMuGTYFPt3jz9-YwJ1-3hh5WfU45L-Gqxcx5YotVCt40UNep8PkF0pY28mVVXk7FkJfoy_YlBQcKkzmPeaY3Z1tQ2TuWExLyqQFcgy6DAQbPw4OJpMlvqIfKIkH9WSVKpmu1oRxUTKL4ZpXcw5eQXQQp3O1ZY80LnFRAMULGnOp1aq64C5nmC5FXskxTyADhoj-J_TvkvMibyUW9DVbllS8IliXBL-t9W_4Mfrau7uLkFXKF-lI-Q2yAwl3-NJrG9Uwb3W_kdN3zuUHWkkqzzvJ9S21uxjfCpg3gm9PkAfN6HzSxPeQ'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        for item in data:
            self.assertTrue(item["id"])
            self.assertTrue(item["title"])
            self.assertTrue(item["Releasedate"])

    def test_404_get_movies(self):
        required_auth = MagicMock()
        required_auth.return_value = None
        res = self.client.get("/movie",headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVYSU5MY2s1a1VzSGNOYUxCTU1TZiJ9.eyJpc3MiOiJodHRwczovL2Rldi1wMmNoZnlvN3Zydmdwa3FtLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NzkyMmQ5NTkzMGRlMDcwOWY2MmI4YmMiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTczNzczNzczMCwiZXhwIjoxNzM3ODI0MTI4LCJzY29wZSI6IiIsImF6cCI6Im9XeFVwUzJzejlBRUoyaVVVQ1Q2N0s2NXRGNGt1TUZtIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIl19.I0VgHKAIbnken8Ykumy5MaBcQI2uV3OL0UWpMuGTYFPt3jz9-YwJ1-3hh5WfU45L-Gqxcx5YotVCt40UNep8PkF0pY28mVVXk7FkJfoy_YlBQcKkzmPeaY3Z1tQ2TuWExLyqQFcgy6DAQbPw4OJpMlvqIfKIkH9WSVKpmu1oRxUTKL4ZpXcw5eQXQQp3O1ZY80LnFRAMULGnOp1aq64C5nmC5FXskxTyADhoj-J_TvkvMibyUW9DVbllS8IliXBL-t9W_4Mfrau7uLkFXKF-lI-Q2yAwl3-NJrG9Uwb3W_kdN3zuUHWkkqzzvJ9S21uxjfCpg3gm9PkAfN6HzSxPeQ'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    # tests for Get actor endpoint
    def test_get_actor(self):
        required_auth = MagicMock()
        required_auth.return_value = None
        res = self.client.get("/actors",headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVYSU5MY2s1a1VzSGNOYUxCTU1TZiJ9.eyJpc3MiOiJodHRwczovL2Rldi1wMmNoZnlvN3Zydmdwa3FtLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NzkyMmQ5NTkzMGRlMDcwOWY2MmI4YmMiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTczNzczNzczMCwiZXhwIjoxNzM3ODI0MTI4LCJzY29wZSI6IiIsImF6cCI6Im9XeFVwUzJzejlBRUoyaVVVQ1Q2N0s2NXRGNGt1TUZtIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIl19.I0VgHKAIbnken8Ykumy5MaBcQI2uV3OL0UWpMuGTYFPt3jz9-YwJ1-3hh5WfU45L-Gqxcx5YotVCt40UNep8PkF0pY28mVVXk7FkJfoy_YlBQcKkzmPeaY3Z1tQ2TuWExLyqQFcgy6DAQbPw4OJpMlvqIfKIkH9WSVKpmu1oRxUTKL4ZpXcw5eQXQQp3O1ZY80LnFRAMULGnOp1aq64C5nmC5FXskxTyADhoj-J_TvkvMibyUW9DVbllS8IliXBL-t9W_4Mfrau7uLkFXKF-lI-Q2yAwl3-NJrG9Uwb3W_kdN3zuUHWkkqzzvJ9S21uxjfCpg3gm9PkAfN6HzSxPeQ'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        for item in data:
         self.assertTrue(item["Id"])
         self.assertTrue(item["Name"])
         self.assertTrue(item["Age"])
         self.assertTrue(item["Gender"])
         self.assertTrue(item["Movie-id"])


    def test_401_without_header(self):
        required_auth = MagicMock()
        required_auth.return_value = None
        res = self.client.get("/actors",headers={'Authorization': 'Bearer '})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["description"], "Authorization header doesnt contain token.")

    #test for post end point for movie

    def test_add_movie(self):
        required_auth = MagicMock()
        required_auth.return_value = None
        res = self.client.post("/addmovie",headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVYSU5MY2s1a1VzSGNOYUxCTU1TZiJ9.eyJpc3MiOiJodHRwczovL2Rldi1wMmNoZnlvN3Zydmdwa3FtLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NzkyMmQ1NDVhMTFlYzg3ZGE0YWQyZWQiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTczNzczNzg4MCwiZXhwIjoxNzM3ODI0Mjc4LCJzY29wZSI6IiIsImF6cCI6Im9XeFVwUzJzejlBRUoyaVVVQ1Q2N0s2NXRGNGt1TUZtIiwicGVybWlzc2lvbnMiOlsiYWRkOm1vdmllIiwiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiXX0.q9iLxPcSzqHXzSjIUPIxXnMy4QqnmJPBWzuxzi830uaIOEMjs9iI_Y0xjvWVYA46QCmvYzGmgTSh1CYRI2s8LHReM5Ork_SvZ_PnDdAv1WfEs8dl3kb5lNpnRJ-d6gkrAwv4HeW6RAtY_PKETLIPsiUXPcbHYUBn6bmgsvELuNM0TuNL-1JGYRXhc7TAoH_02bD0zIvFi3kzjERBxwgA4g-Ma0Y8oS3fK7d7DlvonP0AVcruHCKs_uY1Syo-kb85L4gVB6BMmszR5Izg2gbwSbDhHG3OcntTqEJPs0X7SCTHC2N7GOLhw-C4IdWbF4nRvsgpgdyNm-YyxiAbXxvg_A'},
                json={"title":"The sony pictures", 
                    "releasedate":"12-12-2025"})
        data = json.loads(res.data)

        self.assertTrue(data["success"], True)

    def test_405_add_movie(self):
        required_auth = MagicMock()
        required_auth.return_value = None
        res = self.client.get("/addmovie",headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVYSU5MY2s1a1VzSGNOYUxCTU1TZiJ9.eyJpc3MiOiJodHRwczovL2Rldi1wMmNoZnlvN3Zydmdwa3FtLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NzkyMmQ5NTkzMGRlMDcwOWY2MmI4YmMiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTczNzczNzczMCwiZXhwIjoxNzM3ODI0MTI4LCJzY29wZSI6IiIsImF6cCI6Im9XeFVwUzJzejlBRUoyaVVVQ1Q2N0s2NXRGNGt1TUZtIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIl19.I0VgHKAIbnken8Ykumy5MaBcQI2uV3OL0UWpMuGTYFPt3jz9-YwJ1-3hh5WfU45L-Gqxcx5YotVCt40UNep8PkF0pY28mVVXk7FkJfoy_YlBQcKkzmPeaY3Z1tQ2TuWExLyqQFcgy6DAQbPw4OJpMlvqIfKIkH9WSVKpmu1oRxUTKL4ZpXcw5eQXQQp3O1ZY80LnFRAMULGnOp1aq64C5nmC5FXskxTyADhoj-J_TvkvMibyUW9DVbllS8IliXBL-t9W_4Mfrau7uLkFXKF-lI-Q2yAwl3-NJrG9Uwb3W_kdN3zuUHWkkqzzvJ9S21uxjfCpg3gm9PkAfN6HzSxPeQ'},
              json={"title":"The sony pictures", 
                    "releasedate":"12-12-2025"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], 
                         "Method is wrong")
        
    #test for post end point for actor

    def test_add_actor(self):
        required_auth = MagicMock()
        required_auth.return_value = None
        res = self.client.post("/addactor",headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVYSU5MY2s1a1VzSGNOYUxCTU1TZiJ9.eyJpc3MiOiJodHRwczovL2Rldi1wMmNoZnlvN3Zydmdwa3FtLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NzkyMmQ1NDVhMTFlYzg3ZGE0YWQyZWQiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTczNzczNzg4MCwiZXhwIjoxNzM3ODI0Mjc4LCJzY29wZSI6IiIsImF6cCI6Im9XeFVwUzJzejlBRUoyaVVVQ1Q2N0s2NXRGNGt1TUZtIiwicGVybWlzc2lvbnMiOlsiYWRkOm1vdmllIiwiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiXX0.q9iLxPcSzqHXzSjIUPIxXnMy4QqnmJPBWzuxzi830uaIOEMjs9iI_Y0xjvWVYA46QCmvYzGmgTSh1CYRI2s8LHReM5Ork_SvZ_PnDdAv1WfEs8dl3kb5lNpnRJ-d6gkrAwv4HeW6RAtY_PKETLIPsiUXPcbHYUBn6bmgsvELuNM0TuNL-1JGYRXhc7TAoH_02bD0zIvFi3kzjERBxwgA4g-Ma0Y8oS3fK7d7DlvonP0AVcruHCKs_uY1Syo-kb85L4gVB6BMmszR5Izg2gbwSbDhHG3OcntTqEJPs0X7SCTHC2N7GOLhw-C4IdWbF4nRvsgpgdyNm-YyxiAbXxvg_A'},
              json={"name": "Starliner", 
                    "age": "25",
                    "gender": "F",
                    "movie_id": "1",
                    })
        data = json.loads(res.data)
        print(res.status_code)
        self.assertTrue(data["success"], True)
        print(res.status_code)
    
    def test_404_add_actor(self):
        res = self.client.post("/addactors", 
              json={"name": "Starliner", 
                    "age": "25",
                    "gender": "F",
                    "movie-id": "4",
                    })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)

    #test for update end point for movie

    def test_update_movie(self):
        res = self.client.patch("/updatemovie/5",headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVYSU5MY2s1a1VzSGNOYUxCTU1TZiJ9.eyJpc3MiOiJodHRwczovL2Rldi1wMmNoZnlvN3Zydmdwa3FtLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NzkyMmQ1NDVhMTFlYzg3ZGE0YWQyZWQiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTczNzczNzg4MCwiZXhwIjoxNzM3ODI0Mjc4LCJzY29wZSI6IiIsImF6cCI6Im9XeFVwUzJzejlBRUoyaVVVQ1Q2N0s2NXRGNGt1TUZtIiwicGVybWlzc2lvbnMiOlsiYWRkOm1vdmllIiwiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiXX0.q9iLxPcSzqHXzSjIUPIxXnMy4QqnmJPBWzuxzi830uaIOEMjs9iI_Y0xjvWVYA46QCmvYzGmgTSh1CYRI2s8LHReM5Ork_SvZ_PnDdAv1WfEs8dl3kb5lNpnRJ-d6gkrAwv4HeW6RAtY_PKETLIPsiUXPcbHYUBn6bmgsvELuNM0TuNL-1JGYRXhc7TAoH_02bD0zIvFi3kzjERBxwgA4g-Ma0Y8oS3fK7d7DlvonP0AVcruHCKs_uY1Syo-kb85L4gVB6BMmszR5Izg2gbwSbDhHG3OcntTqEJPs0X7SCTHC2N7GOLhw-C4IdWbF4nRvsgpgdyNm-YyxiAbXxvg_A'},
              json={"title":"Mummy returns", 
                    "releasedate":"11-11-1990"})
        data = json.loads(res.data)

        self.assertTrue(data["success"], True)

    def test_500_update_movie(self):
        res = self.client.patch("/updatemovie/100",headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVYSU5MY2s1a1VzSGNOYUxCTU1TZiJ9.eyJpc3MiOiJodHRwczovL2Rldi1wMmNoZnlvN3Zydmdwa3FtLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NzkyMmQ1NDVhMTFlYzg3ZGE0YWQyZWQiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTczNzczNzg4MCwiZXhwIjoxNzM3ODI0Mjc4LCJzY29wZSI6IiIsImF6cCI6Im9XeFVwUzJzejlBRUoyaVVVQ1Q2N0s2NXRGNGt1TUZtIiwicGVybWlzc2lvbnMiOlsiYWRkOm1vdmllIiwiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiXX0.q9iLxPcSzqHXzSjIUPIxXnMy4QqnmJPBWzuxzi830uaIOEMjs9iI_Y0xjvWVYA46QCmvYzGmgTSh1CYRI2s8LHReM5Ork_SvZ_PnDdAv1WfEs8dl3kb5lNpnRJ-d6gkrAwv4HeW6RAtY_PKETLIPsiUXPcbHYUBn6bmgsvELuNM0TuNL-1JGYRXhc7TAoH_02bD0zIvFi3kzjERBxwgA4g-Ma0Y8oS3fK7d7DlvonP0AVcruHCKs_uY1Syo-kb85L4gVB6BMmszR5Izg2gbwSbDhHG3OcntTqEJPs0X7SCTHC2N7GOLhw-C4IdWbF4nRvsgpgdyNm-YyxiAbXxvg_A'},
              json={"title":"Mummy returns",
                    "releasedate":"12-12-2025"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 500)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["error"], 
                         "Could not able to update the given movie details.")
        
    #test for update end point for actor

    def test_update_actor(self):
        res = self.client.patch("/updateactor/6", headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVYSU5MY2s1a1VzSGNOYUxCTU1TZiJ9.eyJpc3MiOiJodHRwczovL2Rldi1wMmNoZnlvN3Zydmdwa3FtLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NzkyMmQ1NDVhMTFlYzg3ZGE0YWQyZWQiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTczNzczNzg4MCwiZXhwIjoxNzM3ODI0Mjc4LCJzY29wZSI6IiIsImF6cCI6Im9XeFVwUzJzejlBRUoyaVVVQ1Q2N0s2NXRGNGt1TUZtIiwicGVybWlzc2lvbnMiOlsiYWRkOm1vdmllIiwiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiXX0.q9iLxPcSzqHXzSjIUPIxXnMy4QqnmJPBWzuxzi830uaIOEMjs9iI_Y0xjvWVYA46QCmvYzGmgTSh1CYRI2s8LHReM5Ork_SvZ_PnDdAv1WfEs8dl3kb5lNpnRJ-d6gkrAwv4HeW6RAtY_PKETLIPsiUXPcbHYUBn6bmgsvELuNM0TuNL-1JGYRXhc7TAoH_02bD0zIvFi3kzjERBxwgA4g-Ma0Y8oS3fK7d7DlvonP0AVcruHCKs_uY1Syo-kb85L4gVB6BMmszR5Izg2gbwSbDhHG3OcntTqEJPs0X7SCTHC2N7GOLhw-C4IdWbF4nRvsgpgdyNm-YyxiAbXxvg_A'},
              json={"name": "Rajinikanth", 
                    "age": "65",
                    "gender": "M",
                    "movie_id": "3",
                    })
        data = json.loads(res.data)

        self.assertTrue(data["success"], True)

    def test_403_update_actor_permission_missing(self):
        res = self.client.patch("/updateactor/100", headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVYSU5MY2s1a1VzSGNOYUxCTU1TZiJ9.eyJpc3MiOiJodHRwczovL2Rldi1wMmNoZnlvN3Zydmdwa3FtLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NzkyMmQ5NTkzMGRlMDcwOWY2MmI4YmMiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTczNzczNzczMCwiZXhwIjoxNzM3ODI0MTI4LCJzY29wZSI6IiIsImF6cCI6Im9XeFVwUzJzejlBRUoyaVVVQ1Q2N0s2NXRGNGt1TUZtIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIl19.I0VgHKAIbnken8Ykumy5MaBcQI2uV3OL0UWpMuGTYFPt3jz9-YwJ1-3hh5WfU45L-Gqxcx5YotVCt40UNep8PkF0pY28mVVXk7FkJfoy_YlBQcKkzmPeaY3Z1tQ2TuWExLyqQFcgy6DAQbPw4OJpMlvqIfKIkH9WSVKpmu1oRxUTKL4ZpXcw5eQXQQp3O1ZY80LnFRAMULGnOp1aq64C5nmC5FXskxTyADhoj-J_TvkvMibyUW9DVbllS8IliXBL-t9W_4Mfrau7uLkFXKF-lI-Q2yAwl3-NJrG9Uwb3W_kdN3zuUHWkkqzzvJ9S21uxjfCpg3gm9PkAfN6HzSxPeQ'},
              json={"name": "Rajinikanth", 
                    "age": "65",
                    "gender": "M",
                    "movie-id": "3",
                    })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["description"], 
                         "Permission not found.")
        
      #test for delete end point for actor

    def test_delete_actor(self):
        res = self.client.delete("/removeactor/5",headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVYSU5MY2s1a1VzSGNOYUxCTU1TZiJ9.eyJpc3MiOiJodHRwczovL2Rldi1wMmNoZnlvN3Zydmdwa3FtLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NzkyMmQ1NDVhMTFlYzg3ZGE0YWQyZWQiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTczNzczNzg4MCwiZXhwIjoxNzM3ODI0Mjc4LCJzY29wZSI6IiIsImF6cCI6Im9XeFVwUzJzejlBRUoyaVVVQ1Q2N0s2NXRGNGt1TUZtIiwicGVybWlzc2lvbnMiOlsiYWRkOm1vdmllIiwiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiXX0.q9iLxPcSzqHXzSjIUPIxXnMy4QqnmJPBWzuxzi830uaIOEMjs9iI_Y0xjvWVYA46QCmvYzGmgTSh1CYRI2s8LHReM5Ork_SvZ_PnDdAv1WfEs8dl3kb5lNpnRJ-d6gkrAwv4HeW6RAtY_PKETLIPsiUXPcbHYUBn6bmgsvELuNM0TuNL-1JGYRXhc7TAoH_02bD0zIvFi3kzjERBxwgA4g-Ma0Y8oS3fK7d7DlvonP0AVcruHCKs_uY1Syo-kb85L4gVB6BMmszR5Izg2gbwSbDhHG3OcntTqEJPs0X7SCTHC2N7GOLhw-C4IdWbF4nRvsgpgdyNm-YyxiAbXxvg_A'})
        print(res.data)
        data = json.loads(res.data)

        self.assertTrue(data["success"], True)

    def test_405_delete_actor(self):
        res = self.client.patch("/removeactor/100",headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVYSU5MY2s1a1VzSGNOYUxCTU1TZiJ9.eyJpc3MiOiJodHRwczovL2Rldi1wMmNoZnlvN3Zydmdwa3FtLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NzkyMmQ1NDVhMTFlYzg3ZGE0YWQyZWQiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTczNzczNzg4MCwiZXhwIjoxNzM3ODI0Mjc4LCJzY29wZSI6IiIsImF6cCI6Im9XeFVwUzJzejlBRUoyaVVVQ1Q2N0s2NXRGNGt1TUZtIiwicGVybWlzc2lvbnMiOlsiYWRkOm1vdmllIiwiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiXX0.q9iLxPcSzqHXzSjIUPIxXnMy4QqnmJPBWzuxzi830uaIOEMjs9iI_Y0xjvWVYA46QCmvYzGmgTSh1CYRI2s8LHReM5Ork_SvZ_PnDdAv1WfEs8dl3kb5lNpnRJ-d6gkrAwv4HeW6RAtY_PKETLIPsiUXPcbHYUBn6bmgsvELuNM0TuNL-1JGYRXhc7TAoH_02bD0zIvFi3kzjERBxwgA4g-Ma0Y8oS3fK7d7DlvonP0AVcruHCKs_uY1Syo-kb85L4gVB6BMmszR5Izg2gbwSbDhHG3OcntTqEJPs0X7SCTHC2N7GOLhw-C4IdWbF4nRvsgpgdyNm-YyxiAbXxvg_A'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], 
                         "Method is wrong")
        
     #test for delete end point for movie

    def test_delete_movie(self):
        res = self.client.delete("/removemovie/2",headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVYSU5MY2s1a1VzSGNOYUxCTU1TZiJ9.eyJpc3MiOiJodHRwczovL2Rldi1wMmNoZnlvN3Zydmdwa3FtLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NzkyMmQ1NDVhMTFlYzg3ZGE0YWQyZWQiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTczNzczNzg4MCwiZXhwIjoxNzM3ODI0Mjc4LCJzY29wZSI6IiIsImF6cCI6Im9XeFVwUzJzejlBRUoyaVVVQ1Q2N0s2NXRGNGt1TUZtIiwicGVybWlzc2lvbnMiOlsiYWRkOm1vdmllIiwiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiXX0.q9iLxPcSzqHXzSjIUPIxXnMy4QqnmJPBWzuxzi830uaIOEMjs9iI_Y0xjvWVYA46QCmvYzGmgTSh1CYRI2s8LHReM5Ork_SvZ_PnDdAv1WfEs8dl3kb5lNpnRJ-d6gkrAwv4HeW6RAtY_PKETLIPsiUXPcbHYUBn6bmgsvELuNM0TuNL-1JGYRXhc7TAoH_02bD0zIvFi3kzjERBxwgA4g-Ma0Y8oS3fK7d7DlvonP0AVcruHCKs_uY1Syo-kb85L4gVB6BMmszR5Izg2gbwSbDhHG3OcntTqEJPs0X7SCTHC2N7GOLhw-C4IdWbF4nRvsgpgdyNm-YyxiAbXxvg_A'})
        print(res.data)
        print(res.status_code)
        data = json.loads(res.data)

        self.assertTrue(data["success"], True)

    def test_405_delete_movie(self):
        res = self.client.patch("/removemovie/100",headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVYSU5MY2s1a1VzSGNOYUxCTU1TZiJ9.eyJpc3MiOiJodHRwczovL2Rldi1wMmNoZnlvN3Zydmdwa3FtLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NzkyMmQ1NDVhMTFlYzg3ZGE0YWQyZWQiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTczNzczNzg4MCwiZXhwIjoxNzM3ODI0Mjc4LCJzY29wZSI6IiIsImF6cCI6Im9XeFVwUzJzejlBRUoyaVVVQ1Q2N0s2NXRGNGt1TUZtIiwicGVybWlzc2lvbnMiOlsiYWRkOm1vdmllIiwiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiXX0.q9iLxPcSzqHXzSjIUPIxXnMy4QqnmJPBWzuxzi830uaIOEMjs9iI_Y0xjvWVYA46QCmvYzGmgTSh1CYRI2s8LHReM5Ork_SvZ_PnDdAv1WfEs8dl3kb5lNpnRJ-d6gkrAwv4HeW6RAtY_PKETLIPsiUXPcbHYUBn6bmgsvELuNM0TuNL-1JGYRXhc7TAoH_02bD0zIvFi3kzjERBxwgA4g-Ma0Y8oS3fK7d7DlvonP0AVcruHCKs_uY1Syo-kb85L4gVB6BMmszR5Izg2gbwSbDhHG3OcntTqEJPs0X7SCTHC2N7GOLhw-C4IdWbF4nRvsgpgdyNm-YyxiAbXxvg_A'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], 
                         "Method is wrong")
        
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
