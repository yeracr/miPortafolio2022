from utils.db import db


class Comentario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(100))
    comentario = db.Column(db.String(100))

    def __init__(self, usuario, comentario):
        self.usuario = usuario
        self.comentario = comentario


try:

    class UsuariosOficiales(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(50), unique=True, nullable=False)
        password = db.Column(db.String(80), nullable=False)
        nombreusuario = db.Column(db.String(255))
        codigo = db.Column(db.String(255))
        celular = db.Column(db.String(255))
        direccion = db.Column(db.String(255), nullable=False)

        def serialize(self):
            return {
                "id": self.id, "username": self.username, "password": self.password, "nombreusuario": self.nombreusuario, "codigo ": self.codigo, "celular": self.celular, "direccion": self.direccion
            }

    class OficialesEntrada(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        idoficial = db.Column(db.String(50), unique=True, nullable=False)
        codigo = db.Column(db.String(80), nullable=False)
        horaEntrada = db.Column(db.String(255))
        horaSalida = db.Column(db.String(255))
        puesto = db.Column(db.String(255))

        def serialize(self):
            return {
                "id": self.id, "idoficial": self.idoficial, "codigo": self.codigo, "horaEntrada": self.horaEntrada, "horaSalida ": self.horaSalida, "puesto": self.puesto
            }

    class UsuariosSanAgustin(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(50), unique=True, nullable=False)
        password = db.Column(db.String(80), nullable=False)
        nombreusuario = db.Column(db.String(255))
        pin = db.Column(db.String(255))
        casa = db.Column(db.String(255))
        permanentes = db.Column(db.String(255), nullable=False)

        def serialize(self):
            return {
                "id": self.id, "username": self.username, "password": self.password, "nombreusuario": self.nombreusuario, "pin": self.pin, "casa": self.casa, "permanentes": self.permanentes
            }

    class VisitasDiariasDB(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        idcondomino = db.Column(db.String(50))
        nombrevisita = db.Column(db.String(80))
        empresa = db.Column(db.String(255))
        hora = db.Column(db.String(255))
        fecha = db.Column(db.String(255))

        def serialize(self):
            return {
                "id": self.id, "idcondomino": self.idcondomino, "nombrevisita": self.nombrevisita, "empresa": self.empresa, "hora": self.hora, "fecha": self.fecha
            }

    class Ranchos(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        idcondomino = db.Column(db.String(50))
        etapa = db.Column(db.String(80))
        hora = db.Column(db.String(255))
        fecha = db.Column(db.String(255))

        def serialize(self):
            return {
                "id": self.id, "idcondomino": self.idcondomino, "etapa": self.etapa, "hora": self.hora, "fecha": self.fecha
            }

except Exception as e:
    print(str(e))
