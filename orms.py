from enum import unique
from operator import truediv
from re import A
from unicodedata import name
from peewee import *  # ForeignKeyField, SqliteDatabase, Model, CharField

# if __name__ == '__main__':
#    pass
# else:
#    print('modulo orms importado con éxito')

db = SqliteDatabase('DataBase.db')


class User(Model):
    name = CharField(50, unique=True)
    email = CharField(50, unique=True)
    password = CharField(50)

    class Meta:
        database = db


class Brand(Model):
    name = CharField(50)

    class Meta:
        # primary_key=CompositeKey('name')
        database = db


class Modelo(Model):
    modelID = AutoField(primary_key=True)
    brand = ForeignKeyField(Brand, backref='brand')
    name = CharField(50)

    class Meta:
        database = db


class Energy(Model):
    modelID = ForeignKeyField(Modelo, backref='modelID')
    energy = IntegerField()

    class Meta:
        database = db


class Client(Model):
    user = ForeignKeyField(User, backref='user')
    name = CharField(50)
#    brand=ForeignKeyField(Brand, backref='brand')
#    model=ForeignKeyField(Modelo, backref='modelo')

    class Meta:
        database = db


class Session(Model):
    session_id = IntegerField()
    user = CharField(50)  # ForeignKeyField(User, backref='user')
    client = ForeignKeyField(Client, backref='client')
    brand = ForeignKeyField(Brand, backref='brand')
    modelo = ForeignKeyField(Modelo, backref='modelo')

    class Meta:
        database = db


class DID_Status(Model):
    status_id = IntegerField()
    battery = IntegerField()
    lineConnection = BooleanField(default=False)
    statusUpdated = BooleanField(default=False)

    class Meta:
        database = db


db.connect()
db.create_tables([User, Brand, Modelo, Client, Session, DID_Status])


def ConexionDB(parametros):
    def funcion_c(**args):
        db = SqliteDatabase('DataBase.db')
        db.connect
        parametros()
        db.close

    return funcion_c


@ConexionDB
def Add_brand():

    name = input("ingrese nueva marca de desfibrilador: ")

    # verifica si el nombre de marca ya exixte.
    try:
        Brand.get(Brand.name == name)
        print('La marca', name, 'ya existe')

    # si la marca no existe, la crea.
    except:
        Brand.create(name=name)
        print('marca', name, 'creada')

    data = Brand.get(Brand.name == name)
    print(data.name)


@ConexionDB
def Add_modelo():
    brand = input("ingrese la marca del desfibrilador: ")

    # verifica si el nombre de marca ya exixte.
    try:
        Brand.get(Brand.name == brand)
    # si la marca no existe ofrece crearla.
    except:
        if input('La marca no existe. ¿Desea agregarla? (y/n): ') == "y":
            Brand.create(name=brand)
            print('marca', brand, 'creada')
        else:
            return None

    name = input('ingrese nuevo modelo de la marca de desfibrilador: ')

    # verifica si el nombre de modelo ya existe.
    try:
        Modelo.get((Modelo.name == name) & (Modelo.brand == brand))
        print('El modelo', name, 'de la marca', brand, 'ya existe.')

    # si el modelo no existe, lo crea.
    except:
        Modelo.create(brand=brand, name=name)
        print('modelo', name, 'de la marca', brand, 'creada.')


@ConexionDB
def Add_energy():
    brand = input("ingrese la marca del desfibrilador: ")

    # verifica si el nombre de marca ya exixte.
    try:
        Brand.get(Brand.name == brand)
    # si la marca no existe ofrece crearla.
    except:
        if input('La marca no existe. ¿Desea agregarla? (y/n): ') == "y":
            Brand.create(name=brand)
            print('marca', brand, 'creada')
        else:
            return None

    modelo = input("ingrese el modelo del desfibrilador: ")

    # verifica si el nombre de modelo ya exixte.
    try:
        Modelo.get(Modelo.name == modelo)
    # si el modelo no existe ofrece crearlo.
    except:
        if input('El modelo no existe. ¿Desea agregarlo? (y/n): ') == "y":
            Modelo.create(name=modelo)
            print('marca', brand + ', modelo', modelo, 'creado')
        else:
            return None

    modelID = Modelo.get(Modelo.name == modelo)
    energy = input('ingrese nueva energia en Jules del desfibrilador: ')

    # verifica si la energia del modelo ya existe.
    try:
        Energy.get((Energy.modelID == modelID) & (Energy.energy == energy))
        print('La energia', energy, 'del modelo',
              modelo+', marca', brand, 'ya existe.')

    # si no existe, lo crea.
    except:
        Energy.create(modelID=modelID, energy=energy)
        print('Energía', energy, 'Jules, del modelo',
              modelo, 'de la marca', brand, 'creada.')


@ConexionDB
def Add_session_1():
    try:
        Session.get(Session.session_id == 1)
    except:
        Session.create(session_id=1, user='', client='', brand='', modelo='')


@ConexionDB
def Add_DID_Status_1():
    try:
        DID_Status.get(DID_Status.status_id == 1)
    except:
        DID_Status.create(status_id=1, battery=55, lineConnection=False)


@ConexionDB
def Ask_DID_Status():
    return DID_Status.get(DID_Status.status_id == 1)


@ConexionDB
def Add_user():
    # if name=='' or email =='' or password == '':
    name = input('Ingrese nombre de usuario: ')
    email = input('Ingrese email: ')
    password = input('Ingrese contraseña: ')
    # verifica si el nombre de usuario ya existe.
    try:
        User.get(User.name == name)
        print('El usuario', name, 'ya existe')
        return False

    # si el usuario no existe, lo crea.
    except:
        print(name)
        print(email)
        print(password)
        User.create(name=name, email=email, password=password)
        print('Usuario', name, 'creado')
        return True


@ConexionDB
def Add_client():

    user = input('Ingrese el usuario: ')

    if User.get_or_none(User.name == user) == None:
        print('Usuario no existe')
        return

    name = input("ingrese nuevo cliente: ")

    # verifica si el nombre de cliente ya exixte.
    try:
        Client.get((Client.name == name) & (Client.user == user))
        print('El cliente', name, 'del usuario', user, 'ya existe')

    # si el cliente no existe, lo crea.
    except:
        Client.create(name=name, user=user)
        print('cliente', name, 'del usuario', user, 'creado')


Add_session_1()
Add_DID_Status_1()
db.close

if __name__ == '__main__':
    respuesta = input('¿Qué desea agregar?: Nuevo ')
    if respuesta == 'modelo':
        Add_modelo()
    elif respuesta == 'usuario':
        Add_user()
    elif respuesta == 'marca':
        Add_brand()
    elif respuesta == 'sesion':
        Add_session_1()
    elif respuesta == 'cliente':
        Add_client()
