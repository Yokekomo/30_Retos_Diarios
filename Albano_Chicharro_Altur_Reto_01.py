# Albano Chicharro Altur
# Reto 1
# 30 retos diarios

"""
Lenguaje: Python
IDE recomendado: PyCharm
Nivel: Inicial

Enunciado: Dado un fichero excel con nombres y correos (columna nombre y columna email),
realiza un script en Python que devuelva los mails únicos de la columna email.
Consideraciones: Utiliza la librería pandas para procesar el fichero Excel (.xls).
"""

import pandas as pd

emails = pd.read_excel("nombre_emails.xlsx", usecols=["Emails"])

print(emails.drop_duplicates())
