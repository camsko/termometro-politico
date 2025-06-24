from Scrappers import CRHoy, Asamblea, LaRepublica

noticias = CRHoy.scrapear_noticias('2025-06-15', 5)
noticias += LaRepublica.scrapear_noticias('2025-06-22', 5)

for noticia in noticias:
  print(f"Sitio: {noticia['sitio']}")
  print(f"Titulo: {noticia['titulo']}")