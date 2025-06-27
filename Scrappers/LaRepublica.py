from bs4 import BeautifulSoup
from urllib.parse import urljoin
from datetime import date
import BaseDatos
import Utils

def scrapear_noticias(fecha, cantidad_noticias = -1):
  noticias = []
  links = []
  links_totales = []
  pagina = 0
  links_nuevos, detener_busqueda = obtener_links(fecha, pagina)
  links_totales += links_nuevos
  while not detener_busqueda:
    pagina += 1
    links_nuevos, detener_busqueda = obtener_links(fecha, pagina)
    links_totales += links_nuevos

  for link in links_totales:
    if cantidad_noticias != -1 and len(links) >= cantidad_noticias: break
    print(link)
    links.append(link)

  links = BaseDatos.filtrar_links('La Republica', links)
  for link in links:
    contenido_html_noticia = Utils.obtener_contenido_link(link)
    if not contenido_html_noticia:
      continue
    titulo = obtener_titulo(contenido_html_noticia, link)
    contenido = obtener_contenido(contenido_html_noticia, link)
    noticia = Utils.construir_noticia('La Republica', link, titulo, contenido, fecha)
    noticias.append(noticia)
  return noticias
      
def obtener_links(fecha_deseada, pagina):
  url = 'https://www.larepublica.net/seccion/ultima-hora'
  if pagina > 0:
    url = f'{url}/page/{pagina}'
  contenido_html = Utils.obtener_contenido_link(url)
  soup = BeautifulSoup(contenido_html, 'html.parser')

  div_principal = soup.find('div', class_='main-content-1')

  links = []

  if div_principal:
    articulos = div_principal.find_all('article')
      
    for articulo in articulos:
      a_tag = articulo.find('a', class_='link')
      if a_tag and a_tag.has_attr('href'):
        url_completa = urljoin('https://www.larepublica.net/', a_tag['href'])
        fecha_div = a_tag.find('div', class_='date')
        fecha_span = fecha_div.find('span')
        fecha, menor_a_fecha_deseada = obtener_fecha_formateada(fecha_span.get_text(strip=True), fecha_deseada)
        if menor_a_fecha_deseada:
          return links, True
        else:
          if fecha is not None:
            links.append(url_completa)
  return links, False

def obtener_fecha_formateada(fecha_sin_formato, fecha_deseada):
    fecha_formateada = fecha_sin_formato.lower().split(',')[1].strip().split(' ')
    meses = {'enero': '01', 'febrero': '02', 'marzo': '03', 'abril': '04',
             'mayo': '05', 'junio': '06', 'julio': '07', 'agosto': '08',
             'septiembre': '09', 'octubre': '10', 'noviembre': '11', 'diciembre': '12'
    }

    dia = fecha_formateada[0].zfill(2)
    mes = meses.get(fecha_formateada[1])
    anio = fecha_formateada[2]
    
    if not mes:
        return None, False
    
    fecha_para_comparar = date(int(anio), int(mes), int(dia))
    fd_partes = fecha_deseada.split('-')
    fecha_deseada_para_comparar = date(int(fd_partes[0]), int(fd_partes[1]), int(fd_partes[2]))
    if fecha_para_comparar < fecha_deseada_para_comparar:
        return None, True
    elif fecha_para_comparar > fecha_deseada_para_comparar:
      return None, False
    
    fecha_formateada = f'{anio}-{mes}-{dia}'
    return fecha_formateada, False

def obtener_titulo(html, link):
  if not html:
    print(f"Este link falla: {link}")
  soup = BeautifulSoup(html, 'html.parser')
  titulo_div = soup.find('div', class_='title')
  titulo_h1 = titulo_div.find('h1')
  titulo = titulo_h1.get_text(strip=False)
  titulo = titulo.replace('{{slide.text | html}}', '').replace('\xa0',' ')
  return titulo
  
def obtener_contenido(html, link):
  soup = BeautifulSoup(html, 'html.parser')
  contenido_div = soup.find('div', class_='post-content-wrapper')
  contenido_section = contenido_div.find('section')
  if not contenido_section:
    print(f"Problemas con el contenido en el link {link}")
    contenido_section = contenido_div.find('div', class_='classic-content-wrapper')
  
  if not contenido_section:
    print(f"Mayores problemas con el contenido en el link {link}")

  parrafos = contenido_section.find_all('p')
  parrafos += contenido_section.find_all('li')
  parrafos += contenido_section.find_all('div')
  textos = []
  for p in parrafos:
    textos.append(p.get_text(strip=False))
  contenido = ' '.join(textos)
  contenido = contenido.replace('{{slide.text | html}}', '').replace('\xa0',' ')
  return contenido