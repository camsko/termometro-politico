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

def agregar_noticias(noticias, para_asamblea = False):
  if len(noticias) == 0:
    return
  if para_asamblea:
    asamblea_coleccion.insert_many(noticias)
  else:
    noticieros_coleccion.insert_many(noticias)

def obtener_noticias(sitio = None, link = None, fecha = None, columnas = None):
  restricciones = {}
  if sitio is not None and sitio != "Asamblea":
    restricciones['sitio'] = sitio
  if link is not None:
    restricciones['link'] = link
  if fecha is not None:
    restricciones['fecha'] = fecha

  coleccion = noticieros_coleccion
  if sitio == 'Asamblea':
    coleccion = asamblea_coleccion
  
  noticias = []
  if columnas:
    noticias = coleccion.find(restricciones, columnas)
  else:
    noticias = coleccion.find(restricciones)
  return list(noticias)

def filtrar_links(sitio, links):
  links_guardados = obtener_noticias(sitio=sitio, columnas={'_id': 0, 'link': 1})
  solo_links = [item['link'] for item in links_guardados]
  nuevos_filtrados = []
  for link in links:
    if link not in solo_links:
      nuevos_filtrados.append(link)
  return nuevos_filtrados

def actualizar_resumen_noticias(sitio, link, resumen):
  actualizaciones = {
    "$set": {"resumen": resumen}
  }
  if sitio == "Asamblea":
    asamblea_coleccion.update_one({"link": link}, actualizaciones)
  else:
    noticieros_coleccion.update_one({"link": link}, actualizaciones)
