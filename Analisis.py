import matplotlib.pyplot as plt
import numpy as np
import BaseDatos
import Utils

columnas1 = {"_id": 0, "sitio": 1, "link": 1, "titulo": 1, "contenido": 1, "fecha": 1, "resumen": 1}
columnas2 = {"_id": 0, "link": 1, "titulo": 1, "contenido": 1, "fecha": 1, "resumen": 1}

relaciones = Utils.cargar_embeddings("Relaciones.jsonl")

fechas_barra = (
    "17/05", "18/05", "19/05", "20/05", "21/05", "22/05", "23/05", "24/05", 
    "25/05", "26/05", "27/05", "28/05", "29/05", "30/05", "31/05", "01/06", 
    "02/06", "03/06", "04/06", "05/06", "06/06", "07/06", "08/06", "09/06", "10/06", 
    "11/06", "12/06", "13/06", "14/06", "15/06", "16/06", "17/06", "18/06",
    "19/06", "20/06", "21/06", "22/06", "23/06", "24/06", "25/06", "26/06"
)

fechas = [
    "17/05", "18/05", "19/05", "20/05", "21/05", "22/05", "23/05", "24/05", 
    "25/05", "26/05", "27/05", "28/05", "29/05", "30/05", "31/05", "01/06", 
    "02/06", "03/06", "04/06", "05/06", "06/06", "07/06", "08/06", "09/06", "10/06", 
    "11/06", "12/06", "13/06", "14/06", "15/06", "16/06", "17/06", "18/06",
    "19/06", "20/06", "21/06", "22/06", "23/06", "24/06", "25/06", "26/06"
]

fechas_para_comparar = []
for fecha in fechas:
  fecha_transformada = fecha.split("/")
  fecha_transformada = f"2025-{fecha_transformada[1]}-{fecha_transformada[0]}"
  fechas_para_comparar.append(fecha_transformada)

asamblea_cantidad_noticias = [0] * 41
crhoy_cantidad_noticias = [0] * 41
la_republica_cantidad_noticias = [0] * 41

print("Test 2")
links_visitados = []

for i in range(len(fechas_para_comparar)):
  fecha = fechas_para_comparar[i]
  print(fecha)
  for relacion in relaciones:
    link1 = relacion['link_noticiero']
    link2 = relacion['link_asamblea']
    fecha1 = relacion['fecha_noticiero']
    fecha2 = relacion['fecha_asamblea']
    sitio = relacion['sitio']
    if fecha1 == fecha and link1 not in links_visitados:
      links_visitados.append(link1)
      if sitio == "CRHoy":
        crhoy_cantidad_noticias[i] += 1
      else:
        la_republica_cantidad_noticias[i] += 1
    if fecha2 == fecha and link2 not in links_visitados:
      links_visitados.append(link2)
      asamblea_cantidad_noticias[i] += 1
       
       
       

pesos = {
    "Asamblea": asamblea_cantidad_noticias,
    "CRHoy": crhoy_cantidad_noticias,
    "La República": la_republica_cantidad_noticias
}
width = 0.5

fig, ax = plt.subplots()
bottom = np.zeros(41)

for noticiero, peso in pesos.items():
    p = ax.bar(fechas_barra, peso, width, label=noticiero, bottom=bottom)
    bottom += peso

xtick_indices = list(range(0, len(fechas_barra), 5))
ax.set_xticks(xtick_indices)
ax.set_xticklabels([fechas_barra[i] for i in xtick_indices], rotation=45)

ax.set_title("Cantidad de noticias sobre Poder Judicial")
ax.legend(loc="upper right")

plt.show()