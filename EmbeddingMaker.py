from sentence_transformers import SentenceTransformer, util
import BaseDatos

model = SentenceTransformer('distiluse-base-multilingual-cased-v2')

# noticias_crhoy = BaseDatos.obtener_noticias(sitio='CRHoy', columnas={'titulo': 1, 'contenido': 1})
# noticias_la_republica = BaseDatos.obtener_noticias(sitio='La Republica', columnas={'titulo': 1, 'contenido': 1})
print(f"Cargando noticias desde la base de datos.")
noticias = BaseDatos.obtener_noticias(columnas={'sitio': 1, 'titulo': 1, 'contenido': 1})
print(f"Noticias cargadas desde la base de datos.")
# noticias_asamblea = BaseDatos.obtener_noticias(sitio="Asamblea")

noticias_asamblea = [{'contenido': 'Fracasa intento de aplicar vía rápida a jornadas 4x3', 'fecha': '2025-05-19'},
                     {'contenido': 'Nuevos proyectos de ley buscan derribar barreas que enfrentan personas con discapacidad', 'fecha': '2025-05-19'},
                     {'contenido': 'Gerente financiero de la CCSS asegura que hubo incremento del 100% en ofertas con cooperativas', 'fecha': '2025-05-19'},
                     {'contenido': 'Diputada independiente lamenta falta de diálogo y negociación', 'fecha': '2025-05-19'},
                     {'contenido': 'Serie “Leyes que impactan”: Extradición de nacionales', 'fecha': '2025-05-20'},
                     {'contenido': 'Gilbert Jiménez: "aprobamos más de 30 leyes en seguridad, Gobierno está en deuda"', 'fecha': '2025-05-20'},
                     {'contenido': 'Antonio Ortega: el amante de Star Wars, fiel en defensa de las luchas sociales', 'fecha': '2025-05-20'},
                     {'contenido': 'Rodrigo Chaves ya no comparecerá en la Comisión de la Caja', 'fecha': '2025-05-20'},
                     {'contenido': 'Comisión preocupada por cumplimientos de seguridad en terminal de Moín', 'fecha': '2025-05-20'},
                     {'contenido': 'Instalan 4 comisiones ordinarias y dos especiales para último año legislativo', 'fecha': '2025-05-20'},
                     {'contenido': 'Serie “Leyes de impacto”: Útiles escolares', 'fecha': '2025-05-22'},
                     {'contenido': 'Nombran Directorios de 8 Comisiones Especiales', 'fecha': '2025-05-22'},
                     {'contenido': 'Eligen Magistrados suplentes de Sala Primera', 'fecha': '2025-05-22'},
                     {'contenido': 'Diputada espera dejar legislación para proteger los océanos', 'fecha': '2025-05-22'},
                     {'contenido': 'Rechazan aplicar vía rápida a proyecto sobre jornadas excepcionales', 'fecha': '2025-05-23'},
                     {'contenido': 'Propuestas para modificar retiro del ROP empiezan a tomar fuerza en el Congreso', 'fecha': '2025-05-23'},
                     {'contenido': 'Diputados cuestionan al Gobierno falta de propuestas para cancelar la deuda con la CCSS', 'fecha': '2025-05-23'}
                     ]

noticias_asamblea += [
    {"contenido": "Aprueban primer presupuesto extraordinario del 2025", "fecha": "2025-06-24"},
    {"contenido": "Reclaman a jerarca de AyA por problemas de agua en La Carpio y Hatillos", "fecha": "2025-06-24"},
    {"contenido": "Aprueban informe sobre la no entrega de equipo tecnológico a estudiantes en vulnerabilidad", "fecha": "2025-06-24"},
    {"contenido": "Piden cuentas a Director de Innovación de la Caja sobre plataforma digital ERP", "fecha": "2025-06-24"},
    {"contenido": "Entrevista diputada Gloria Navas: “Apertura parlamentaria es fundamental en una democracia”", "fecha": "2025-06-24"},
    {"contenido": "Serie Leyes de impacto: Reformas a libertad condicional", "fecha": "2025-06-24"},
    {"contenido": "Piden cuentas a Vicepresidente por destitución de Junta Directiva del Banco Nacional", "fecha": "2025-06-23"},
    {"contenido": "Resaltan informe de Comisión de Financiamiento en acusación de la Fiscalía a Presidente Chaves", "fecha": "2025-06-23"},
    {"contenido": "Debate: Crucitas requiere respuestas urgentes", "fecha": "2025-06-23"},
    {"contenido": "Podcast Voces del Congreso: Asesores Legislativos: “es falso que nos pagan teléfono, viáticos, salarios millonarios, gasolina”", "fecha": "2025-06-23"},
    {"contenido": "Podcast Conozca al diputado: Gilberto Campos, el repartidor de pan, amante del judo y de la cocina que llegó a una curul", "fecha": "2025-06-23"},
    {"contenido": "Continúa análisis sobre remoción de la Junta Directiva del Banco Nacional", "fecha": "2025-06-23"},
    {"contenido": "Inicia investigación por destitución de Junta Directiva del Banco Nacional", "fecha": "2025-06-20"},
    {"contenido": "Buscan frenar estafas desde centros penitenciarios", "fecha": "2025-06-20"},
    {"contenido": "Tres mujeres más integrarán el Salón de Honor del Congreso", "fecha": "2025-06-20"},
    {"contenido": "Cuestionan a CNE manejo de recursos del crédito para atención de emergencias", "fecha": "2025-06-20"},
    {"contenido": "Cierre del Ministerio de Gobernación divide criterios en la Comisión de Reforma del Estado", "fecha": "2025-06-20"},
    {"contenido": "Culminan audiencias en investigación sobre migrantes en el Catem", "fecha": "2025-06-20"},
    {"contenido": "Cuestionan desalojo en Pavones de Golfito", "fecha": "2025-06-20"},
    {"contenido": "Entrevista diputada Priscilla Vindas: Vindas preocupada por situación en Crucitas", "fecha": "2025-06-20"},
    {"contenido": "Avanza proyecto que elimina la doble postulación", "fecha": "2025-06-19"},
    {"contenido": "Canciller deberá dar explicaciones sobre viaje de funcionarios de la DIS a Taiwán", "fecha": "2025-06-19"},
    {"contenido": "Rechazan proyecto para regular vapeadores", "fecha": "2025-06-19"},
    {"contenido": "Comisión pide explicaciones a Ministro sobre medidas arancelarias establecidas por Estados Unidos", "fecha": "2025-06-19"},
    {"contenido": "Resaltan importancia de proteger al consumidor financiero", "fecha": "2025-06-19"},
    {"contenido": "Colegio de Abogados avala reforma al Código Procesal Agrario", "fecha": "2025-06-19"},
    {"contenido": "Entrevista diputada Vanessa Castro: Diputada duda de proyecto de mega cárcel", "fecha": "2025-06-19"},
    {"contenido": "Comisión de Nombramientos continúa con entrevistas para recomendar magistrado de la Sala III", "fecha": "2025-06-19"},
    {"contenido": "Cámara de Turismo achaca caída en el sector, a variación del tipo de cambio", "fecha": "2025-06-19"},
    {"contenido": "Exigen alto inmediato al fuego entre Israel y Gaza", "fecha": "2025-06-18"},
    {"contenido": "Avalan presupuesto extraordinario para ampliar línea férrea y compra de chalecos en el Poder Judicial", "fecha": "2025-06-18"},
    {"contenido": "Servicios técnicos recomienda que Presidente Chaves comparezca a Comisión Investigadora de la CCSS", "fecha": "2025-06-18"},
    {"contenido": "Vecinos denuncian que problemas con abastecimiento de agua siguen en La Carpio y Hatillo", "fecha": "2025-06-18"},
    {"contenido": "Hacienda reconoce efecto fiscal positivo de regular exploración y explotación minera", "fecha": "2025-06-18"},
    {"contenido": "INDER y MAG presentan dudas a reforma del Código Procesal Agrario", "fecha": "2025-06-18"},
    {"contenido": "Podcast Voces del Congreso. Entrevista diputado Luis Fernando Mendoza: “Este gobierno está en deuda con Guanacaste”", "fecha": "2025-06-18"},
    {"contenido": "Podcast Conozca al diputado. Entrevista diputada Rocío Alfaro: La diputada que desde la cuna forma parte de la izquierda de Costa Rica", "fecha": "2025-06-18"},
    {"contenido": "Reportaje: Crucitas, tierra de nadie", "fecha": "2025-06-18"},
    {"contenido": "Apoyan proyecto para certificar empresas que promuevan personal en exclusión social", "fecha": "2025-06-18"},
    {"contenido": "Diputados visitan Crucitas para buscar soluciones en la zona", "fecha": "2025-06-17"},
    {"contenido": "Asociación de Desarrollo de Crucitas está a favor de exploración de oro", "fecha": "2025-06-17"},
    {"contenido": "Diputado oficialista rinde cuentas sobre labor legislativa", "fecha": "2025-06-17"},
    {"contenido": "Aumenta preocupación por penetración del crimen organizado en el país", "fecha": "2025-06-17"},
    {"contenido": "Cinthya Córdoba: “este gobierno no tiene agenda en materia ambiental”", "fecha": "2025-06-09"},
    {"contenido": "Pedro Rojas, el político formado en las orillas del río Sarapiquí", "fecha": "2025-06-09"},
    {"contenido": "Comisión analiza impacto para Cartago y Paraíso por amenazas del AyA", "fecha": "2025-06-09"},
    {"contenido": "Aprefloflas está en contra de proyecto minero en Cutris", "fecha": "2025-06-09"},
    {"contenido": "Cuestionan actuar de la DIS por posible persecución de diputados", "fecha": "2025-06-09"},
]

noticias_asamblea += [
    {"contenido": "Acuerdan sesionar en Nicoya por cuarto año consecutivo", "fecha": "2025-06-05"},
    {"contenido": "Continua preocupación por situación de migrantes deportados", "fecha": "2025-06-05"},
    {"contenido": "Analiza primer presupuesto extraordinario del 2025", "fecha": "2025-06-05"},
    {"contenido": "Leyes de impacto: relaciones impropias", "fecha": "2025-06-05"},
    {"contenido": "Experto afirma que áreas protegidas se ven afectadas por actividades del narcotráfico", "fecha": "2025-06-05"},
    {"contenido": "Buscan dar alivio a los vecinos del Paraíso de Cartago", "fecha": "2025-06-05"},
    {"contenido": "Hacen llamado a continuar con el diálogo para resolver problema de agua en Paraíso de Cartago", "fecha": "2025-06-04"},
    {"contenido": "Cuestionan capacidad y modelo de albergues del PANI", "fecha": "2025-06-04"},
    {"contenido": "Padres con hijos autistas denuncian violación de derechos humanos de esta población", "fecha": "2025-06-04"},
    {"contenido": "Jurado del Galardón Ambiental Legislativo fue juramentado", "fecha": "2025-06-04"},
    {"contenido": "Analizan proyecto para regular criptoactivos", "fecha": "2025-06-04"},
    {"contenido": "Critican falta de planificación en el INCOFER", "fecha": "2025-06-04"},
    {"contenido": "Exfuncionario de la DIS asegura que los cuerpos policiales 'trabajan con las uñas'", "fecha": "2025-06-04"},
    {"contenido": "Diputados con dudas de manejo de sesiones de Junta Directiva en la CCSS", "fecha": "2025-06-03"},
    {"contenido": "Consultan sobre nueva cárcel prometida por el Gobierno", "fecha": "2025-06-03"},
    {"contenido": "Aprobaron traspaso de terreno a Iglesia católica en Desamparados", "fecha": "2025-06-03"},
    {"contenido": "Leyes de impacto: Puentes", "fecha": "2025-06-03"},
    {"contenido": "Cuestionan capacidad y modelo de albergues del PANI", "fecha": "2025-06-03"},
    {"contenido": "Yonder Salas: 'adultos mayores han sido abandonados por este Gobierno'", "fecha": "2025-06-03"},
    {"contenido": "Aprueban reforma a impuestos municipales del cantón central de Cartago", "fecha": "2025-06-03"},
    {"contenido": "Discuten oposición del Parlamento Cívico Ambiental sobre proyecto en Crucitas", "fecha": "2025-06-02"},
    {"contenido": "Legisladora cuestiona política ambiental del Gobierno", "fecha": "2025-06-02"},
    {"contenido": "Leyes de impacto: Ley que persigue delitos de corrupción y evita la impunidad por prescripción", "fecha": "2025-05-30"},
    {"contenido": "Delegación visitará zona de Crucitas", "fecha": "2025-05-30"},
    {"contenido": "Cuestionan retención de recursos a Seguridad y no contratación de plazas en cárceles", "fecha": "2025-05-29"},
    {"contenido": "Buscan modernizar y agilizar los procedimientos judiciales en materia agraria", "fecha": "2025-05-29"},
    {"contenido": "Legisladora pide madurez política para avanzar con discusión de 4x3", "fecha": "2025-05-29"},
    {"contenido": "Serie 'Leyes de impacto': Préstamos gota a gota", "fecha": "2025-05-27"},
    {"contenido": "Danny Vargas: 'jornadas 4x3 debe aprobarse, pero requiere actualizarse'", "fecha": "2025-05-27"},
    {"contenido": "“Loco”, atrevido, amante del deporte y enamorado de sus hijos, así se describe el liberal Diego Vargas", "fecha": "2025-05-27"},
    {"contenido": "Continua preocupación por la no implementación del Sistema de Planificación de Recursos Empresariales en la Caja", "fecha": "2025-05-27"},
    {"contenido": "Familias de Barras del Caribe afirman que reglamento de arrendamiento en finca de JAPDEVA es inconstitucional", "fecha": "2025-05-27"},
    {"contenido": "Definen directorios de comisiones", "fecha": "2025-05-27"},
    {"contenido": "Asamblea Legislativa no discutirá levantamiento de inmunidad de diputado", "fecha": "2025-05-26"},
    {"contenido": "Comisión apoyaría propuesta para cambiar distribución de ingresos por extracción de oro", "fecha": "2025-05-26"},
    {"contenido": "Lanamme y auditoría del MOPT advierten incumplimientos en proyecto Taras La Lima en Cartago", "fecha": "2025-05-26"},
    {"contenido": "Legisladora insiste en allanamientos las 24 horas los 7 días de la semana", "fecha": "2025-05-26"},
]


def extraer_oraciones(texto):
  oraciones = texto.split('.')
  if oraciones[-1] == '':
    oraciones.pop()
  for i in range(len(oraciones)):
    oraciones[i] = oraciones[i].strip()
  return oraciones

textos_noticias = []
textos_asamblea = []
for noticia in noticias:
  texto = noticia['contenido']
  textos_noticias.append([texto])
for noticia in noticias_asamblea:
  texto = noticia['contenido']
  textos_asamblea.append(texto)

def generar_embeddings_asamblea(textos):
  embeddings = []
  for texto in textos:
    embeddings.append(model.encode(texto))
  return embeddings

def generar_embeddings(textos):
  contador = 0.01
  embeddings_texto = []
  for texto in textos:
    embedding_oraciones = []
    for oracion in texto:
      embedding_oracion = model.encode(oracion)
      embedding_oraciones.append(embedding_oracion)
    if len(embeddings_texto) > contador * len(textos):
      print(f"{int(100 * len(embeddings_texto)/len(textos))}%")
      contador += 0.01
    embeddings_texto.append(embedding_oraciones)
  return embeddings_texto

def similitud(embedding1, embedding2):
  sim = util.cos_sim(embedding1, embedding2)
  return sim.tolist()[0][0]

print(f"Generando embeddings de noticias.")
embeddings_noticias = generar_embeddings(textos_noticias)
print(f"Generando embeddings de noticias de la Asamblea.")
embeddings_asamblea = generar_embeddings_asamblea(textos_asamblea)

relaciones = []

for i in range(len(embeddings_noticias)):
  for j in range(len(embeddings_asamblea)):
    mejor_similitud = -1
    for k in range(len(embeddings_noticias[i])):
      sim_cos = similitud(embeddings_noticias[i][k], embeddings_asamblea[j])
      if sim_cos > mejor_similitud:
        mejor_similitud = sim_cos
    relaciones.append((noticias[i]['sitio'], noticias[i]['titulo'], noticias_asamblea[j]['contenido'], mejor_similitud))
  print(f"({i + 1}) de {len(embeddings_noticias)}")

for relacion in relaciones:
  # print(f"Noticia de CRHoy: {relacion[0]}")
  # print(f"Noticia de la Asamblea: {relacion[1]}")
  if relacion[3] >= 0.6:
    print(f"Noticia de {relacion[0]}: {relacion[1]}")
    print(f"Noticia de la Asamblea: {relacion[2]}")
    print(f'MUCHA RELACION')
    print(f"Similitud: {relacion[3]}")
  # elif relacion[2] < 0.6 and relacion[2] >= 0.3:
  #   # print(f'POCA RELACION')
  # else:
    # print(f'NULA RELACION')
  # print(f"Similitud: {relacion[2]}")


