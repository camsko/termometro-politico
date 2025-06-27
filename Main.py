from datetime import datetime, timedelta
from Scrappers import CRHoy, Asamblea, LaRepublica
import BaseDatos

# fecha_inicial = datetime(2025, 5, 18)
# fecha_final = datetime(2025, 6, 18)

# lista_de_fechas = []
# for dia in range((fecha_final - fecha_inicial).days + 1):
#   fecha = fecha_inicial + timedelta(days=dia)
#   fecha = fecha.strftime('%Y-%m-%d')
#   print(fecha)
#   lista_de_fechas.append(fecha)

# for fecha in lista_de_fechas:
#   noticias = CRHoy.scrapear_noticias(fecha)
#   noticias += LaRepublica.scrapear_noticias(fecha)
#   BaseDatos.agregar_noticias(noticias)

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

# BaseDatos.agregar_noticias(noticias_asamblea, True)
print(BaseDatos.obtener_noticias(sitio='Asamblea'))
