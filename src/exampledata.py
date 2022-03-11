from connect import get_database    #  Modulo Conexion a la Base de Datos


dbname = get_database() #   Llamar la conexion de la base de datos

# Create a new collection
collection_name = dbname["AppConsoleList"]

expiry_date = '2021-07-13T00:00:00.000Z'
item_3 = {
"item_name" : "Bread",
"quantity" : 2,
"ingredients" : "all-purpose flour",
}

collection_name.insert_one(item_3)