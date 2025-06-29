import json
import numpy as np
import BaseDatos
import Utils

noticias_emb = []
noticias_asamblea_emb = []

noticias = BaseDatos.obtener_noticias()
noticias_asamblea = BaseDatos.obtener_noticias("Asamblea")

noticias_por_link = {}
noticias_asamblea_por_link = {}

for noticia in noticias:
  noticias_por_link[noticia['link']] = {'sitio': noticia['sitio'], 'titulo': noticia['titulo'], 'contenido': noticia['contenido'], 'fecha': noticia['fecha']}

for noticia in noticias_asamblea:
  noticias_asamblea_por_link[noticia['link']] = {'titulo': noticia['titulo'], 'contenido': noticia['contenido'], 'fecha': noticia['fecha']}

with open("NoticierosEmbeddings.jsonl", "r", encoding="utf-8") as f:
  for linea in f:
    noticia = json.loads(linea)
    noticias_emb.append(noticia)

with open("AsambleaEmbeddings.jsonl", "r", encoding="utf-8") as fi:
  for linea in fi:
    noticia = json.loads(linea)
    noticias_asamblea_emb.append(noticia)

tipos_de_comparacion = ["contenido", "contenido", "resumen"]
relaciones = []

for a in range(len(noticias_emb)):
  for b in range(len(noticias_asamblea_emb)):
    for i in range(1):
      embedding1 = noticias_emb[a][tipos_de_comparacion[i]]
      embedding2 = noticias_asamblea_emb[b][tipos_de_comparacion[i]]
      sim = Utils.similitud(embedding1, embedding2)
      if sim >= 0.7:
        relaciones.append((noticias_emb[a], noticias_asamblea_emb[b], tipos_de_comparacion[i], tipos_de_comparacion[i], sim))
  print(a + 1)

relaciones.sort(key=lambda x: x[4], reverse=False)

for relacion in relaciones:
  noticia = noticias_por_link[relacion[0]['link']]
  noticia_asamblea = noticias_asamblea_por_link[relacion[1]['link']]
  tipo_comp1 = relacion[2]
  tipo_comp2 = relacion[3]
  sim = relacion[4]
  print("-" * 80)
  print(f"Noticia de {noticia['sitio']}: {noticia['titulo']}")
  print(f"Link: {relacion[0]['link']}")
  print(f"Noticia de Asamblea: {noticia_asamblea['titulo']}")
  print(f"Link: {relacion[1]['link']}")
  print(f"Tipo de comparación: {tipo_comp1} - {tipo_comp2}")
  print(f"Similitud: {sim}")
  Utils.quien_hablo_antes(noticia, noticia_asamblea)
  print("-" * 80)
print(len(relaciones))