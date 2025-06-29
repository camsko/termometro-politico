import json
import matplotlib.pyplot as plt
import BaseDatos
import Utils

columnas = {"_id": 0, "sitio": 1, "link": 1, "titulo": 1, "contenido": 1, "fecha": 1, "resumen": 1}
noticias = BaseDatos.obtener_noticias(columnas=columnas)
columnas = {"_id": 0, "link": 1, "titulo": 1, "contenido": 1, "fecha": 1, "resumen": 1}
noticias_asamblea = BaseDatos.obtener_noticias("Asamblea", columnas=columnas)

noticias_emb = Utils.cargar_embeddings("NoticierosEmbeddings.jsonl")
noticias_asamblea_emb = Utils.cargar_embeddings("AsambleaEmbeddings.jsonl")

def calcular_relaciones(noticiero_comparacion, asamblea_comparacion, umbral):
  relaciones = []
  umbrales = {}
  noticias_habladas = []
  magnitud = 5
  for i in range(10 * magnitud, -10 * magnitud, -1):
    i = i/(10 * magnitud)
    umbrales[str(i)] = 0
  porcentaje_contador = int(0.1 * len(noticias_asamblea_emb))
  for a in range(len(noticias_asamblea_emb)):
    total_sim = 0
    for b in range(len(noticias_emb)):
      embedding1 = noticias_emb[b][noticiero_comparacion]
      embedding2 = noticias_asamblea_emb[a][asamblea_comparacion]
      sim = Utils.similitud(embedding1, embedding2)
      # total_sim += sim
      truncated_sim = str(int(10 * sim * magnitud)/(10 * magnitud))
      if truncated_sim not in umbrales:
        umbrales[truncated_sim] = 1
      else:
        umbrales[truncated_sim] += 1
      if sim >= umbral:
        relaciones.append((noticias[b], noticias_asamblea[a], noticiero_comparacion, asamblea_comparacion, sim))
        total_sim += 1
    
    noticias_habladas.append((noticias_asamblea[a], total_sim))
    if a + 1 > porcentaje_contador:
      porcentaje_contador += int(0.1 * len(noticias_asamblea_emb))
      print(f"{a + 1} de {len(noticias_asamblea_emb)} noticias ({int(100 * (a + 1)/len(noticias_asamblea_emb))}%)")
  return relaciones, umbrales, noticias_habladas

relaciones, umbrales, noticias_habladas = calcular_relaciones("contenido", "contenido", 0.7)
relaciones.sort(key=lambda x: x[4], reverse=True)

Utils.imprimir_relaciones(relaciones)

noticias_habladas.sort(key=lambda x: x[1], reverse=True)
noticias_menos_habladas = noticias_habladas[109:]
noticias_mas_habladas = noticias_habladas[:5]

print("Noticias más habladas:")
for noticia in noticias_mas_habladas:
  print("-" * 80)
  print(f"Titulo: {noticia[0]['titulo']}")
  print(f"Similitud total: {noticia[1]}")
  print("-" * 80)

print("Noticias menos habladas:")
for noticia in noticias_menos_habladas:
  print("-" * 80)
  print(f"Titulo: {noticia[0]['titulo']}")
  print(f"Similitud total: {noticia[1]}")
  print("-" * 80)

data_para_jsonl = []
for relacion in relaciones:
  data = {"link_noticiero": relacion[0]['link'], "link_asamblea": relacion[1]['link'], "similitud": relacion[4]}
  data_para_jsonl.append(data)
with open("Relaciones.jsonl", "w", encoding="utf-8") as f:
  for data in data_para_jsonl:
    json.dump(data, f)
    f.write("\n")

x = []
y = []
for key, value in umbrales.items():
  y.append(value)
  x.append(float(key))

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()