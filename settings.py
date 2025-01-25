from dotenv import load_dotenv
import os 
load_dotenv() 
DB_NAME = os.environ.get("DB_NAME") 
DB_USER=os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
TESTDB_NAME = os.environ.get("TESTDB_NAME") 
TESTDB_USER=os.environ.get("TESTDB_USER")
TESTDB_PASSWORD = os.environ.get("TESTDB_PASSWORD")
port = os.environ.get('PORT')
RENDER_DB_HOST = os.getenv('RENDER_DB_HOST')  
RENDER_DB_NAME = os.getenv('RENDER_DB_NAME')  
RENDER_DB_USER = os.getenv('RENDER_DB_USER')  
RENDER_DB_PASSWORD = os.getenv('RENDER_DB_PASSWORD')