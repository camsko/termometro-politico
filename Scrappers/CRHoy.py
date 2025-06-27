import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
import Utils
import json
import time
import BaseDatos

def procesar_link(link, fecha_noticias):
    if '/nacionales/' not in link:
        return None

    link_html = Utils.obtener_contenido_link(link)
    if link_html is None:
        return None

    titulo = obtener_titulo(link_html)
    contenido = obtener_contenido(link_html)
    return Utils.construir_noticia('CRHoy', link, titulo, contenido, fecha_noticias)

def scrapear_noticias(fecha_noticias, cantidad_noticias = -1):
  noticias = []
  noticias_info = Utils.obtener_contenido_link(f'https://api.crhoy.net/ultimas/{fecha_noticias}.json?v=3')
  noticias_info = json.loads(noticias_info)
  links = []
  for noticia_info in noticias_info['ultimas']:
    link = noticia_info['url']
    print(link)
    if cantidad_noticias != -1 and len(links) >= cantidad_noticias: break
    links.append(link)

  links = BaseDatos.filtrar_links('CRHoy', links)
  
  if len(links) == 0: return []
  
  with ThreadPoolExecutor(max_workers=10) as executor:
        futuros = [executor.submit(procesar_link, link, fecha_noticias) for link in links]
        for future in as_completed(futuros):
            resultado = future.result()
            if resultado:
                noticias.append(resultado)
  return noticias
  
def obtener_titulo(html):
  soup = BeautifulSoup(html, 'html.parser')
  titulo_h1 = soup.select_one('article > div h1')
  titulo = titulo_h1.get_text(strip=True)
  return titulo
    

def obtener_contenido(html):
  soup = BeautifulSoup(html, 'html.parser')
  parrafos = soup.select('article > div > div > div p')
  textos = []
  for p in parrafos:
    textos.append(p.get_text(strip=False))
  contenido = ' '.join(textos)
  contenido = contenido.replace('{{slide.text | html}}', '').replace('\xa0',' ')
  return contenido

