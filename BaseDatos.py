from dotenv import find_dotenv, load_dotenv
import os
from pymongo import MongoClient

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")
connection_string = f'mongodb+srv://root:{password}@cluster0.rj4w0vv.mongodb.net/linktree_node_typescript'

cliente = MongoClient(connection_string)
db = cliente.Noticias
noticieros_coleccion = db.Noticieros
asamblea_coleccion = db.Asamblea

def agregar_noticia(noticia, para_asamblea = False):
  if para_asamblea:
    asamblea_coleccion.insert_one(noticia)
  else:
    noticieros_coleccion.insert_one(noticia)

def agregar_noticias(noticias, para_asamblea = False):
  if para_asamblea:
    asamblea_coleccion.insert_many(noticias)
  else:
    noticieros_coleccion.insert_many(noticias)