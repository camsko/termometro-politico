import json
from sentence_transformers import SentenceTransformer
import numpy as np
import BaseDatos
import Utils

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

def embedding_de_texto_largo(texto):
    chunks = Utils.separar_texto(texto)
    embeddings = [model.encode(chunk) for chunk in chunks]
    mean_embedding = np.mean(embeddings, axis=0)
    return mean_embedding.astype(float).tolist()

def generar_embedding_noticia(noticia):
  titulo_embedding = embedding_de_texto_largo(noticia['titulo'])
  contenido_embedding = embedding_de_texto_largo(noticia['contenido'])
  resumen_embedding = embedding_de_texto_largo(noticia['resumen'])
  noticia_embedding = {"link": noticia['link'], "titulo": titulo_embedding, "contenido": contenido_embedding, "resumen": resumen_embedding}
  return noticia_embedding

def generar_embedding_de_noticias(noticias):
  noticias_embeddings = []
  for i in range(len(noticias)):
    noticia = noticias[i]
    noticia_embedding = generar_embedding_noticia(noticia)
    noticias_embeddings.append(noticia_embedding)
    print(f"{i + 1} de {len(noticias)} noticias ({100 * (i + 1)/len(noticias):.2f}%)")
  return noticias_embeddings

noticias = BaseDatos.obtener_noticias()
noticias_asamblea = BaseDatos.obtener_noticias("Asamblea")

noticias_embeddings = generar_embedding_de_noticias(noticias)
noticias_asamblea_embeddings = generar_embedding_de_noticias(noticias_asamblea)

with open("NoticierosEmbeddings.jsonl", "w", encoding="utf-8") as f:
  for noticia_embed in noticias_embeddings:
    json.dump(noticia_embed, f)
    f.write("\n")

with open("AsambleaEmbeddings.jsonl", "w", encoding="utf-8") as f:
  for noticia_embed in noticias_asamblea_embeddings:
    json.dump(noticia_embed, f)
    f.write("\n")
