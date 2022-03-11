#   Conexion a la Base de Datos MongoDB
from datetime import datetime
import hashlib
from connect import get_database
import pymongo
from bson.objectid import ObjectId

dbname = get_database()

#   Crear Coleccion
collection_name = dbname["UserAppConsole"]

class User:

    def __init__(self, name, lastname, email, password):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password

    def REGISTER(self):
        fecha = datetime.now() #    Fecha
        hashpassword = hashlib.sha256() #   Metodo de Encryptacion
        hashpassword.update(self.password.encode('utf8'))   #   Encryptar Contraseña
        UserRegister = {
            "name" : self.name,
            "lastname" : self.lastname,
            "email" : self.email,
            "password" : hashpassword.hexdigest(),  #   Guardar hexadecimal de Encryptado
            "date" : fecha
        }
        id = collection_name.insert_one(UserRegister)
        identifier = id.inserted_id

        if identifier != None:
            print(f"Te haz Registrado Correctamente, {identifier} ")
        else:
            print('No te haz Podido Registrar Intentalo de Nuevo')


    def LOGIN(self):
        UserFound = { 'email' : self.email}
        try:
            response = collection_name.find_one(UserFound)
            return response

        except:
            return print(' User has not found ')

