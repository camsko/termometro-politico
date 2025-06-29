import ollama
import BaseDatos

client = ollama.Client()

model = "llama3.1"

noticias = BaseDatos.obtener_noticias(link="https://www.larepublica.net/noticia/ex-arquero-de-turrialba-rompe-el-silencio-sobre-propuesta-de-amano")

for i in range(len(noticias)):
  noticia = noticias[i]
  prompt = "Resume el siguiente texto, y no agregues texto adicional aparte del resumen:\n\n"
  prompt += noticia['contenido']
  resumen = client.generate(model=model, prompt=prompt).response
  BaseDatos.actualizar_resumen_noticias("Asamblea", noticia["link"], resumen)
  print(f"{i + 1} de {len(noticias)} resúmenes generados ({100 * (i + 1)/len(noticias):.2f}%)")
