from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.comentario import Comentario, Ranchos, VisitasDiariasDB, UsuariosSanAgustin, UsuariosOficiales, OficialesEntrada
from utils.db import db
import time
import datetime
from flask import render_template, request, session, redirect, url_for
import os

from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/sanagustin.db"

Base = declarative_base()


engine = create_engine(dbdir)
session_maker = sessionmaker()
session_maker.configure(bind=engine)
Base.metadata.create_all(engine)
sessionx = session_maker()


comentario = Blueprint("comentario", __name__)


@comentario.route('/comentario')
def index():
    comentario = Comentario.query.all()
    print(comentario)
    for a in comentario:
        print(a)
    return render_template('index.html', comentario=comentario)


@comentario.route('/new', methods=['POST'])
def add_comentario():
    if request.method == 'POST':

        usuario = request.form['usuario']
        comentario = request.form['comentario']

        new_comentario = Comentario(usuario, comentario )

        db.session.add(new_comentario)
        db.session.commit()

        flash('comentario agregado con exito!')

        return redirect(url_for('comentario.index'))


@comentario.route("/update/<string:id>", methods=["GET", "POST"])
def update(id):
    print(id)
    comentario = Comentario.query.get(id)

    if request.method == "POST":
        comentario.usuario = request.form['usuario']
        comentario.comentario = request.form['comentario']

        db.session.commit()

        flash('Mensaje guardado con exito!')

        return redirect(url_for('comentario.index'))

    return render_template("update.html", comentario=comentario)


@comentario.route("/delete/<id>", methods=["GET"])
def delete(id):
    comentario = Comentario.query.get(id)
    db.session.delete(comentario)
    db.session.commit()

    flash('Comentario Eliminado!')

    return redirect(url_for('comentario.index'))



@comentario.route('/')
def miperfil():
    return render_template('miportafoliox/miperfil.html')



@comentario.route('/')
def uno():
    return render_template('uno.html')


@comentario.route('/cv')
def cv():
    return render_template('miportafoliox/cv.html')


@comentario.route('/oficiales')
def oficiales():
    return render_template('miportafoliox/oficiales/oficiales.html')


@comentario.route("/logoutf")
def logoutf():
    try:
        session.pop('loggedin', None)
        return redirect(url_for('.oficiales'))
    except:
        return redirect(url_for('.oficiales'))


@comentario.route("/loginf", methods=["GET", "POST"])
def loginf():

    if request.method == "POST":
        mensaje = ''
        usuario_condominio = request.form["username"]
        password_condominio = request.form["password"]
        time.sleep(2)
        user = UsuariosOficiales.query.filter_by(
            username=request.form["username"]).first()
        if user and check_password_hash(user.password, request.form["password"]):
            session["usernamef"] = user.username
            session["idf"] = user.id
            session["loggedin"] = True
            usx = str(session["usernamef"])
            user = UsuariosOficiales.query.filter_by(username=usx).first()
            id_condominio = user.id
            usuario_condominio = user.username
            password_condominio = user.password
            nombreusuario_condominio = user.nombreusuario
            codigo = user.codigo
            celular = user.celular
            direccion = user.direccion
            usuarioCompleto = [[id_condominio, usuario_condominio, password_condominio,
                                nombreusuario_condominio, codigo, celular, direccion]]
            time.sleep(1)
            mensaje = ''
# codigo conjunto del tuturial video 1 2 y 3
            usx = str(session["usernamef"])
            user = UsuariosOficiales.query.filter_by(username=usx).first()
            id_condominio = user.id
            usuario_condominio = user.username
            password_condominio = user.password
            nombreusuario_condominio = user.nombreusuario
            codigo = user.codigo
            celular = user.celular
            direccion = user.direccion
            usuarioCompleto = [[id_condominio, usuario_condominio, password_condominio,
                                nombreusuario_condominio, codigo, celular, direccion]]
            time.sleep(1)
            nombre_xxx = nombreusuario_condominio
            msk = ''
            ausencias = '0'
            tardias = '1'
            faltas = '1'
            meritos = '98'
            amonestaciones = '0'
            return redirect(url_for('.homef'))
        else:
            mensaje = "Tu usuario es incorrecto, por seguridad te hemos sacado de nuestra plataforma"
    else:
        mensaje = 'Favor iniciar sesión'
    return render_template("miportafoliox/oficiales/login.html", mensaje=mensaje)


@comentario.route("/homef", methods=["GET", "POST"])
def homef():
    if "usernamef" in session:
        session['loggedin'] = True
        mensaje = ''
        usx = str(session["usernamef"])
        user = UsuariosOficiales.query.filter_by(username=usx).first()
        id_condominio = user.id
        usuario_condominio = user.username
        password_condominio = user.password
        nombreusuario_condominio = user.nombreusuario
        codigo = user.codigo
        celular = user.celular
        direccion = user.direccion
        usuarioCompleto = [[id_condominio, usuario_condominio, password_condominio,
                            nombreusuario_condominio, codigo, celular, direccion]]
        time.sleep(1)
        mensaje = ''
        msk = ''
        ausencias = '0'
        tardias = '1'
        faltas = '1'
        meritos = '98'
        amonestaciones = 'gfdg'

        return render_template('miportafoliox/oficiales/index.html', usuario_xxx=nombreusuario_condominio, tardias=tardias, faltas=faltas, meritos=meritos, amonestaciones=amonestaciones, ausencias=ausencias, direccion=direccion, mensaje=mensaje, celular=celular, codigo=codigo, msk=msk, usuarioCompleto=usuarioCompleto)
    else:
        session.pop('loggedin', None)
        session.pop('idf', None)
        session.pop('usernamef', None)
        mensaje = ''
    return render_template('miportafoliox/oficiales/login.html')


@comentario.route("/registrarf", methods=["GET", "POST"])
def registrarf():
    mensaje = ''
    if request.method == "POST":
        if request.form["acceso"] == '':
            hashed_pw = generate_password_hash(
                request.form["password"], method="sha256")
            username = request.form["username"]
            password = hashed_pw
            nombreusuario = request.form["nombreusuario"]
            codigo = request.form["codigo"]
            celular = request.form["celular"]
            direccion = request.form["direccion"]
            time.sleep(.6)
            try:
                new_user = UsuariosOficiales(username=request.form["username"], password=hashed_pw, nombreusuario=request.form["nombreusuario"],
                                             codigo=request.form["codigo"], celular=request.form["celular"], direccion=request.form["direccion"])
                db.session.add(new_user)
                db.session.commit()
                mensaje = 'Te has registrado con exito'
                return render_template('miportafoliox/oficiales/login.html')
            except:
                mensaje = 'Usuario incorrecto, por seguridad te hemos sacado del sistema'
                session.pop('loggedin', None)
                session.pop('id', None)
                session.pop('usernamef', None)
    return render_template('miportafoliox/oficiales/login.html')


@comentario.route("/formregistrof")
def formregistrof():
    return render_template("miportafoliox/oficiales/registrar.html")


@comentario.route("/emtrada")
def emtrada():
    return render_template("miportafoliox/oficiales/entrada.html")


@comentario.route('/horaentradaf', methods=['GET', 'POST'])
def horaentradaf():
    mensaje = ''
    fechass = str(datetime.datetime.now())

    if request.method == 'POST':
        mensaje = 'Entrada registrada'
        try:
            idoficial = session["id"]
            puesto = request.form["puesto"]
            codigo = request.form["codigo"]
            nombre_usuario = session['usernamef']
            horaEntrada = fechass
            horaSalida = ''
            time.sleep(.6)

            try:
                OficialesEntrada(idoficial=idoficial, codigo=codigo,
                                 horaEntrada=horaEntrada, horaSalida=horaSalida, puesto=puesto)
                db.session.commit()
                mensaje = 'se registro con exito tu entrada'
                return render_template('miportafoliox/oficiales/entrada.html', mensaje=mensaje)

            except Exception as e:
                mensaje = 'ERROR DE REGISTRO' + str(e)
                return redirect(url_for('.homef', mensaje=mensaje, fechass=fechass))
        except:
            pass
    return render_template(url_for('.emtrada', mensaje=mensaje, fechass=fechass))


@comentario.route("/logout")
def logout():
    try:
        session.pop('id', None)
        session.pop("username", None)
        mensaje = "¡Hasta pronto!"
        return redirect(url_for('.login', mensaje=mensaje))
    except:
        session.pop('id', None)
        session.pop("username", None)
        mensaje = "¡Hasta pronto!"

    return redirect(url_for('.miperfil'))


@comentario.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        mensaje = ''
        usuario_condominio = request.form["username"]
        password_condominio = request.form["password"]
        time.sleep(2)
        user = UsuariosSanAgustin.query.filter_by(
            username=request.form["username"]).first()
        if user and check_password_hash(user.password, request.form["password"]):
            session["username"] = user.username
            session["id"] = user.id
            usx = str(session["username"])
            user = UsuariosSanAgustin.query.filter_by(username=usx).first()
            id_condominio = user.id
            usuario_condominio = user.username
            password_condominio = user.password
            nombreusuario_condominio = user.nombreusuario
            pin_condominio = user.pin
            casa_condominio = user.casa
            permanentes_condominio = user.permanentes
            usuarioCompleto = [[id_condominio, usuario_condominio, password_condominio,
                                nombreusuario_condominio, pin_condominio, casa_condominio, permanentes_condominio]]
            time.sleep(1)
            mensaje = '{}'.format(nombreusuario_condominio)

            return redirect(url_for('.home', mensaje=mensaje, usuarioCompleto=usuarioCompleto))
        else:
            mensaje = "Tu usuario es incorrecto, por seguridad te hemos sacado de nuestra plataforma"
    else:
        mensaje = ''
        session["username"] = None
        session["id"] = None
    return render_template("miportafoliox/sanagustin/login.html", mensaje=mensaje)


@comentario.route("/sanagustin", methods=["GET", "POST"])
def home():
    mensaje = ''
    try:
        if "username" in session:
            mensaje = ''
            usx = str(session["username"])
            user = UsuariosSanAgustin.query.filter_by(username=usx).first()

            id_condominio = session["id"]

            usuario_condominio = user.username
            password_condominio = user.password
            nombreusuario_condominio = user.nombreusuario
            pin_condominio = user.pin
            casa_condominio = user.casa
            permanentes_condominio = user.permanentes
            usuarioCompleto = [[id_condominio, usuario_condominio, password_condominio,
                                nombreusuario_condominio, pin_condominio, casa_condominio, permanentes_condominio]]
            time.sleep(1)
            minombre = '{}'.format(nombreusuario_condominio)

            mensaje = ' Bienvenid@ a Hacienda San Agustín, es un gusto tenerte por acá '
            return render_template('miportafoliox/sanagustin/home.html', mensaje=mensaje, minombre=minombre, usuarioCompleto=usuarioCompleto)
        else:
            session.pop('id', None)
            session.pop('username', None)
            mensaje = ''
            msk = ''
    except:
        session.pop('id', None)
        session.pop('username', None)
        mensaje = 'error de inicio'
    return redirect(url_for('.login', mensaje=mensaje))


@comentario.route("/registrar", methods=["GET", "POST"])
def registrar():
    mensaje = ''
    msk = ''
    if request.method == "POST":
        if request.form['acceso'] == '':
            hashed_pw = generate_password_hash(
                request.form["password"], method="sha256")
            username = request.form["username"]
            password = hashed_pw
            nombreusuario = request.form["nombreusuario"]
            pin = request.form["pin"]
            casa = request.form["casa"]
            permanentes = request.form["permanentes"]
            time.sleep(.6)
            try:
                new_user = UsuariosSanAgustin(username=request.form["username"], password=hashed_pw, nombreusuario=request.form[
                                              "nombreusuario"],   pin=request.form["pin"], casa=request.form["casa"], permanentes=request.form["permanentes"])
                db.session.add(new_user)
                db.session.commit()
                mensaje = 'Te has registrado con exito'
            except Exception as e:
                mensaje = 'ERROR DE REGISTRO {} '.format(e)
                session.pop('id', None)
                session.pop('username', None)
        else:
            session["username"] = None
            session["id"] = None
            mensaje = 'El codigo de acceso no es correcto'
            return redirect(url_for(".login", mensaje=mensaje))
    else:
        mensaje = 'error de usuario'
        session["username"] = None
        session["id"] = None
    return redirect(url_for(".login", mensaje=mensaje))


@comentario.route("/registrar_visita_diaria_san_agustin", methods=["GET", "POST"])
def registrar_visita_diaria_san_agustin():
    mensaje = ''
    msk = ''
    try:
        if request.method == "POST":
            idactual = str(session["id"])
            nombreusuario = request.form["nombrevisita"]
            empresa = request.form["empresa"]
            hora = request.form["horahora"]

            fecha = datetime.datetime.now()
            time.sleep(.6)
            new_user = VisitasDiariasDB(
                idcondomino=idactual, nombrevisita=request.form["nombrevisita"],   empresa=request.form["empresa"], hora=request.form["horahora"], fecha=fecha)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('comentario.ver_mis_visitas'))

    except:
        session["username"] = None
        session["id"] = None

    return redirect(url_for('comentario.ver_mis_visitas'))


@comentario.route("/ver_mis_visitas", methods=["GET", "POST"])
def ver_mis_visitas():
    mensaje = ''
    msk = ''
    try:
        if "username" in session:
            idactual = str(session["id"])
            allxxx = VisitasDiariasDB.query.filter_by(idcondomino=idactual)
            allxxx = list(map(lambda x: x.serialize(), allxxx))

            arrayUno = []
            arrayDos = []
            for i in allxxx:
                for x in i:
                    arrayDos.append(i[x])
                arrayUno.append(arrayDos)
                arrayDos = []

            return render_template('miportafoliox/sanagustin/misvisitas.html', mensaje=mensaje, datos=arrayUno)
        else:
            mensaje = 'No podimos entrar a mis visitas'
    except Exception as e:
        mensaje = str(e)

        return redirect('comentario.home', mensaje=mensaje)


@comentario.route("/actualizar_perfil_condomino", methods=["GET", "POST"])
def actualizar_perfil_condomino():
    mensaje = ''
    msk = ''
    if request.method == "POST":
        idk = str(session["id"])
        nombrek = request.form["nombrek"]
        usernamek = request.form["usernamek"]
        passwordk = request.form["passwordk"]

        hashed_pw = generate_password_hash(
            request.form["passwordk"], method="sha256")
        passwordk = hashed_pw

        pink = request.form["pink"]
        casak = request.form["casak"]
        permanentesk = request.form["permanentesk"]

        actualizar_perfil_comentario = (sessionx.query(
            UsuariosSanAgustin).filter_by(id=idk).first())

        actualizar_perfil_comentario.username = usernamek
        actualizar_perfil_comentario.password = passwordk

        actualizar_perfil_comentario.nombreusuario = nombrek
        actualizar_perfil_comentario.pin = pink
        actualizar_perfil_comentario.casa = casak
        actualizar_perfil_comentario.permanentes = permanentesk
        sessionx.commit()
        mensaje = 'Se actualizó tu perfil'
        return redirect(url_for('comentario.home', mensaje=mensaje))

    else:
        session["username"] = None
        session["id"] = None
    return redirect(url_for('comentario.home'))


@comentario.route("/registrar_rancho_casa", methods=["GET", "POST"])
def registrar_rancho_casa():
    arrayUno = []
    arrayDos = []
    mensaje = ''
    try:
        if request.method == "POST":
            idactual = str(session["id"])
            etapa = request.form["etapa"]
            hora = request.form["horahora"]
            fecha = datetime.datetime.now()
            new_user = Ranchos(
                idcondomino=idactual, etapa=request.form["etapa"],   hora=request.form["horahora"], fecha=fecha)
            db.session.add(new_user)
            db.session.commit()
            mensaje = 'PISCINA APARTADA'

    except Exception as e:
        mensaje = str(e)
        print(str(e))

    try:
        if "username" in session:
            allxxx = Ranchos.query.all()
            allxxx = list(map(lambda x: x.serialize(), allxxx))
            arrayUno = []
            arrayDos = []
            for i in allxxx:
                for x in i:
                    arrayDos.append(i[x])
                arrayUno.append(arrayDos)
                arrayDos = []

            fecha = datetime.datetime.now()
            mensaje = 'Dia actual: {}'.format(fecha)
            print(arrayUno)
            return render_template('miportafoliox/sanagustin/ranchos.html', mensaje=mensaje, arrayUno=arrayUno)
        else:
            mensaje = 'No podimos entrar a mis visitas'
    except Exception as e:
        print(str(e))
        mensaje = str(e)
    return render_template('miportafoliox/sanagustin/ranchos.html', mensaje=mensaje, arrayUno=arrayUno)
