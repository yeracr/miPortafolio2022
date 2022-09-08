from flask import Flask
from routes.comentario import comentario
from flask_sqlalchemy import SQLAlchemy

#configuracion env 
#from config import DATABASE_CONNECTION_URI
import os
app = Flask(__name__)

app.secret_key = 'SADADS89A76D7ASHDABSBASC788ACJ898ssa'

#CONFIGMySQL
#app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/sanagustin.db"
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["MAX_CONTENT_LENGTH"] = 16*2**20
app.config["ALLOWED_EXTENSIONS"] = set(["pdf", "png", "jpg", "jpeg", "gif"])
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_FILE_DIR"] = os.path.join(app.root_path, "cache")
app.config["SECRET_KEY"] = "SADADS89A76D7ASHDABSBASC788ACJ898ssa"
app.config["SESSION_FILE_THRESHOLD"] = 1000



# no cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

SQLAlchemy(app)

app.register_blueprint(comentario)
