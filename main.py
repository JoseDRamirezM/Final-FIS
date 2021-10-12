#Clase main.py

import Scraper
import os
from Interfaz import iniciar_sesion

creds = 'tempfile.temp'

if os.path.isfile(creds):
	iniciar_sesion()
else:
	print("Ocurrio un error en el sistema, contacte a Arjosoft!") 


# Inicializamos el objeto para web scraping con los parámetros del URL
# según el proveedor
''' scraper = Scraper.Scraper()

soup = scraper.get_soup(scraper.definir_parametros([2021, 10, 13], [2021, 10, 20], 2, 0, 'booking'))

scraper.proceso_booking(soup)
print(scraper.resultado) '''
