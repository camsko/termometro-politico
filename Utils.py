import requests
import numpy as np
from datetime import datetime

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36"
}

def obtener_contenido_link(link):
  response = requests.get(link.strip(), headers=headers)
  if response.status_code != 200:
     print(f'Hubo un error con el link. Código de error: {response.status_code}')
     return None
  return response.text

def construir_noticia(noticiero, link, titulo, contenido, fecha):
   noticia = {'sitio': noticiero, 'link': link, 'titulo': titulo, 'contenido': contenido, 'fecha': fecha}
   return noticia

def similitud(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)

    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)

    if norm1 == 0 or norm2 == 0:
        return 0

    return dot_product / (norm1 * norm2)

def separar_texto(texto, max_len=200):
    words = texto.split()
    chunks = []
    for i in range(0, len(words), max_len):
        chunk = " ".join(words[i:i+max_len])
        chunks.append(chunk)
    return chunks

def dias_entre(fecha1, fecha2):
    formato = "%Y-%m-%d"
    f1 = datetime.strptime(fecha1, formato)
    f2 = datetime.strptime(fecha2, formato)
    print(f1)
    print(f2)
    return (f1 - f2).days

def ocurre_antes(fecha1, fecha2):
    formato = "%Y-%m-%d"
    f1 = datetime.strptime(fecha1, formato)
    f2 = datetime.strptime(fecha2, formato)
    return f1 < f2

def quien_hablo_antes(noticia, noticia_asamblea):
   fecha1 = noticia['fecha']
   fecha2 = noticia_asamblea['fecha']
   dias_entre_fechas = dias_entre(fecha1, fecha2)
   if dias_entre_fechas > 1:
      print(f"{noticia['sitio']} habló de este tema {dias_entre_fechas} días después que la Asamblea")
   elif dias_entre_fechas == 1:
      print(f"{noticia['sitio']} habló de este tema {dias_entre_fechas} día después que la Asamblea")
   elif dias_entre_fechas == 0:
      print(f"{noticia['sitio']} habló de este tema el mismo día que la Asamblea")
   elif dias_entre_fechas == -1:
      print(f"La Asamblea habló de este tema {-dias_entre_fechas} día después que {noticia['sitio']}")
   elif dias_entre_fechas < -1:
      print(f"La Asamblea habló de este tema {-dias_entre_fechas} días después que {noticia['sitio']}")