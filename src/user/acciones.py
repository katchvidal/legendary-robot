import user.user as modelo
import pymongo
import notes.acciones as notesModelo

class Acciones:

    def REGISTRO(self):
        print('\n Comenzando el REGISTRO Rellena el Siguiente Formulario ')
        name = input('\n Cual es tu Nombre: ')
        lastname = input('\n Cual es tu Apellido: ')
        email = input('\n Cual es tu Email: ')
        password = input('\n Cual es tu Contraseña: ')

        if email == "" or password == "":
            print('Email or Password are Empty please fill the Field')
        else:
            usuario = modelo.User(name, lastname, email, password)  #   Pasamos los datos al Constructor
            usuario.REGISTER()   #   Llamos a la Accion

        
    
    def LOGIN(self):
        print('\n Comenzando el LOGIN Rellena el Siguiente Formulario ')
        email = input('\n Cual es tu Email: ')
        password = input('\n Cual es tu Contraseña: ')
        print('-----    VALIDANDO INFORMACION   -----')

        if email == "" or password == "":
            print('Email or Password are Empty please fill the field') 
        else:
            usuario = modelo.User(None, None, email, password)
            Usuario = usuario.LOGIN()
            nameUser = Usuario['name']
            lastnameUser = Usuario['lastname']
            print(f'Bienvenido {nameUser} {lastnameUser}')
            self.NextActions(Usuario)
    
    def NextActions(self, Usuario ):
        print('''
            Acciones Disponibles:
            -   CREAR UNA NOTA (CREAR)
            -   MOSTRAR TUS NOTAS (MOSTRAR)
            -   ELIMINAR NOTA (ELIMINAR)
            -   SALIR (SALIR)
        ''')

        accion =    input('Que deseas Hacer? : ').lower()
        doit = notesModelo.Acciones()

        if accion == 'crear':
            print('Crear Nota')
            doit.NewNotes(Usuario)
            self.NextActions(Usuario)
        elif accion == 'mostrar':
            print('Mostrar Nota')
            doit.ShowNotes(Usuario)
            self.NextActions(Usuario)
        elif accion == 'eliminar':
            print('Eliminar Nota')
            doit.DeleteNote(Usuario)
            self.NextActions(Usuario)
        elif accion == 'salir':
            exit()