import json
import numpy as np
import BaseDatos
import Utils
import random
import csv

noticias_emb = []
noticias_asamblea_emb = []

noticias = BaseDatos.obtener_noticias()
noticias_asamblea = BaseDatos.obtener_noticias("Asamblea")

noticias_por_link = {}
noticias_asamblea_por_link = {}

asamblea_links_chosen = [
    "https://www.youtube.com/watch?v=nwi2h2_qMu0",
    "https://www.youtube.com/watch?v=BW4vErObIbk&t=131s",
    "https://www.youtube.com/watch?v=ybqq4yJdlC0",
    "https://www.youtube.com/watch?v=Mfr8snWW7G4",
    "https://www.youtube.com/watch?v=SnGMoV-Xdw0",
    "https://www.youtube.com/watch?v=1v2nJeN-3BY",
    "https://www.youtube.com/watch?v=vPL3KwcCF-o&t=1s",
    "https://www.youtube.com/watch?v=8m3Oi3C69j0",
    "https://www.youtube.com/watch?v=Xba9MZML4w4",
    "https://youtu.be/JyacpODpMmY"
]
noticias_link_chosen = [
    "https://www.larepublica.net/noticia/ingreso-de-turistas-cae-en-mayo-un-47-segun-el-ict",
    "https://www.crhoy.com/nacionales/allanan-11-puntos-contra-banda-vinculada-con-narco-y-homicidios-en-zona-norte/",
    "https://www.crhoy.com/nacionales/diputados-catalogan-de-autoritaria-decision-de-chaves-sobre-junta-del-banco-nacional/",
    "https://www.crhoy.com/nacionales/diputados-rechazan-mocion-para-extender-debate-y-conocer-veto-a-plan-de-vuelos-baratos/",
    "https://www.crhoy.com/nacionales/ejecutivo-envia-primer-presupuesto-extraordinario-con-rebaja-de-%e2%82%a115-000-millones/",
    "https://www.crhoy.com/nacionales/informe-de-ee-uu-costa-rica-sigue-entre-los-paises-de-mayor-transito-de-droga-hacia-norteamerica-y-europa/",
    "https://www.crhoy.com/nacionales/hombre-resulto-herido-en-intercambio-de-balas-contra-oficiales-de-fuerza-publica/",
    "https://www.crhoy.com/nacionales/diputados-de-alajuela-evaluan-explotacion-minera-en-crucitas/",
    "https://www.crhoy.com/nacionales/homicidios-narco-y-femicidios-empanan-las-promesas-de-rodrigo-chaves/",
    "https://www.larepublica.net/noticia/pilar-cisneros-advierte-que-proyecto-de-jornadas-4x3-puede-ser-enterrado-hoy-si-no-se-aprueba-via-rapida"
]

for noticia in noticias:
  if(noticia['link'] in noticias_link_chosen):
      noticias_por_link[noticia['link']] = {'sitio': noticia['sitio'], 'titulo': noticia['titulo'], 'contenido': noticia['contenido'], 'fecha': noticia['fecha']}

for noticia in noticias_asamblea:
  if(noticia['link'] in asamblea_links_chosen):
    noticias_asamblea_por_link[noticia['link']] = {'titulo': noticia['titulo'], 'contenido': noticia['contenido'], 'fecha': noticia['fecha']}

print("length{}".format(len(noticias_por_link)))
print("length{}".format(len(noticias_asamblea_por_link)))

with open("NoticierosEmbeddings.jsonl", "r", encoding="utf-8") as f:
  for linea in f:
    noticia = json.loads(linea)
    if(noticia['link'] in noticias_link_chosen):
      noticias_emb.append(noticia)
with open("AsambleaEmbeddings.jsonl", "r", encoding="utf-8") as fi:
  for linea in fi:
    noticia = json.loads(linea)
    if(noticia['link'] in asamblea_links_chosen):
      noticias_asamblea_emb.append(noticia)


tipos_de_comparacion = ["contenido", "contenido", "resumen"]
relaciones = []

for a in range(len(noticias_emb)):
  for b in range(len(noticias_asamblea_emb)):
    for i in range(1):
      embedding1 = noticias_emb[a][tipos_de_comparacion[i]]
      embedding2 = noticias_asamblea_emb[b][tipos_de_comparacion[i]]
      sim = Utils.similitud(embedding1, embedding2)
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


titulos_asamblea = [noticias_asamblea_por_link[n['link']]['titulo'] for n in noticias_asamblea_emb]
titulos_noticias = [noticias_por_link[n['link']]['titulo'] for n in noticias_emb]

matriz_similitudes = [] 

for a in range(len(noticias_emb)):
    fila = []
    titulo_noticia = noticias_por_link[noticias_emb[a]['link']]['titulo']
    fila.append(titulo_noticia)

    for b in range(len(noticias_asamblea_emb)):
        for i in range(1):  # only using first comparison type
            embedding1 = noticias_emb[a][tipos_de_comparacion[i]]
            embedding2 = noticias_asamblea_emb[b][tipos_de_comparacion[i]]
            sim = Utils.similitud(embedding1, embedding2)
            fila.append(sim)
    matriz_similitudes.append(fila)
    print(a + 1)

with open('similitudes_test.csv', mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)

    writer.writerow([''] + titulos_asamblea)

    for fila in matriz_similitudes:
        writer.writerow(fila)