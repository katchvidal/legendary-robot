from connect import get_database
import pymongo
from datetime import datetime
from pprint import pprint

#   Acceder a la Conexion Database
dbname = get_database()

#   Crear Coleccion
collection_name = dbname["NoteAppConsole"]

class Note:

    def __init__(self, title, description, id) :
        self.title = title
        self.description = description
        self.id = id

    def SaveNote(self):
        fecha = datetime.now() #    Fecha
        AddNewNote = {
            "title" : self.title,
            "description" : self.description,
            "usuario_id" : self.id,
            "date" : fecha
        }
        id = collection_name.insert_one(AddNewNote)
        identifier = id.inserted_id
        if identifier != None:
            print('Haz Creado una Nota Correctamente')
        else:
            print('Something Were Wrong Please Contact to Admin')
    
    def GetAllNotes(self):
        NotesFound = { 'usuario_id' : self.id}
        response = collection_name.find(NotesFound)
        for r in response:
            print('\n ###       ---------     ###')
            pprint(r)

    
    def DeleteOneNotes(self):
        NoteOne = { 'title' : self.title }
        response = collection_name.delete_one(NoteOne)
        Identifier = response.deleted_count
        if Identifier == 1:
            print(f'La Nota con el titulo: {self.title} Ha sido eliminado Correctamente ')
        else:
            print('Something Were Wrong Plase Contact Admin')