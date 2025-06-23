import requests
from bs4 import BeautifulSoup
import Utils
import json
import time
import BaseDatos

def scrapear_noticias(fecha_noticias, cantidad_noticias):
  noticias = []
  noticias_info = Utils.obtener_contenido_link(f'https://api.crhoy.net/ultimas/{fecha_noticias}.json?v=3')
  noticias_info = json.loads(noticias_info)
  contador = 1
  for noticia_info in noticias_info['ultimas']:
    if contador > cantidad_noticias:
      break
    contador += 1
    link = noticia_info['url']
    if '/caricaturas/' in link or \
       '/la-frase-del-dia/' in link or \
       '/la-foto-del-dia/' in link:
       continue

    print('-' * 80)
    print('Durmiendo...')
    time.sleep(3)
    print('Procesando...')
    print(link)
    link_html = Utils.obtener_contenido_link(link)
    if link_html is None:
      continue
      
    titulo = obtener_titulo(link_html)
    contenido = obtener_contenido(link_html)
    noticia = Utils.construir_noticia('CRHoy', link, titulo, contenido, fecha_noticias)
    noticias.append(noticia)
  BaseDatos.agregar_noticias(noticias)

  # def obtener_noticias(, fecha):
  #   fechas_filtradas = .almacen.obtener_noticias('CRHoy', fecha)
  #   return fechas_filtradas
  
def obtener_titulo(html):
  soup = BeautifulSoup(html, 'html.parser')
  titulo_h1 = soup.select_one('article > div h1')
  titulo = titulo_h1.get_text(strip=True)
  return titulo
    

def obtener_contenido(html):
  soup = BeautifulSoup(html, 'html.parser')
  parrafos = soup.select('article > div > div > div p')
  textos = [p.get_text(strip=False) for p in parrafos]
  contenido = ' '.join(textos)
  contenido = contenido.replace('{{slide.text | html}}', '').replace('\xa0',' ')
  return contenido

