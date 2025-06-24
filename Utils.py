import requests

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