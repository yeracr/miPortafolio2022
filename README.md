procurar analizar las versiones de las librerias 
a la actualizada 8/8/2024

se debe actualizar algunas cosas en el codigo

from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy


from datetime import date
import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/sanagustin.db"
app = Flask(__name__, instance_relative_config=True)
app.app_context().push()

este seria un ejemplo
