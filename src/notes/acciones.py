import notes.note as modelo



class Acciones:

    def NewNotes(self, Usuario):
        name = Usuario['name']
        lastname = Usuario['lastname']
        id = Usuario['_id']
        print(f' {name} {lastname} Add New Note')
        title = input('Title Note: ').capitalize()
        description = input('description Note: ').capitalize()

        note = modelo.Note(title, description, id )
        save = note.SaveNote()


    def ShowNotes(self, Usuario):
        name = Usuario['name']
        lastname = Usuario['lastname']
        id = Usuario['_id']
        print(f'Get All notes For User: {name} {lastname} ')
        note = modelo.Note(None, None, id)
        getAll = note.GetAllNotes()
    
    def DeleteNote(self,Usuario):
        print('We procced to Delete the Note please Write the Title')
        title = input('Escribe el Nombre de la nota que deseas Borrar: ').capitalize()
        note = modelo.Note(title, None, None)
        #confirm = input('Are you Sure?: ').lower()
        delete = note.DeleteOneNotes()