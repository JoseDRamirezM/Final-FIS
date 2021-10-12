from bs4 import BeautifulSoup
from Hotel import Hotel
from Habitacion import Habitacion
import DB
import requests

class Scraper():
  
  resultado = []

  def __init__(self):
    pass

    # Función que realiza el proceso de scraping y retorna un resultado con tarifas
    # por cada hotel

  def consultar_tarifas(ULRS):
    pass

    # Función que genera el reporte de los resultados obtenidos en el scraping
  def generar_reporte(resultado):
    pass

  '''
  Función que guarda en una base de datos SQLite3 los datos recogidos
  
  '''

  def guardar_datos(self, resultado):
    con = DB.sql_connection()
    if (resultado and resultado != []):
      i = 0
      entities = []
      if con:
        for item in resultado:
          entities.append(
          {'index':i, 'nombre': f'{item.nombre}', 'ubicacion':f'{item.ubicacion}', 'tipo_habitacion':f'{item.habitacion.tipo}', 'precio':f'{item.habitacion.precio}', 'rating_numero':f'{item.rating_numero}', 'rating':f'{item.rating}'
          })
          
          i += 1
        for hotel in entities:
          entity = (hotel['index'], hotel['nombre'], hotel['ubicacion'], hotel['tipo_habitacion'], hotel['precio'], hotel['rating_numero'], hotel['rating'])
            
          DB.sql_table(con)
          DB.sql_insert(con, entity)
          print('Guardado en DB')
    
  headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}

  

  #URL Booking

  URL2 = "https://www.booking.com/searchresults.en-gb.html?aid=306395&label=bogota-Two7ruYijzWOPKEOtd23oQS549403576231%3Apl%3Ata%3Ap1700%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-169717479%3Alp1003659%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YZVcNNsENnH02-pWD53qm9c&lang=en-gb&sid=3148d568b8e7b2d96e1535f7bdddb22b&sb=1&sb_lp=1&src=city&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fcity%2Fco%2Fbogota.en-gb.html%3Faid%3D306395%3Blabel%3Dbogota-Two7ruYijzWOPKEOtd23oQS549403576231%253Apl%253Ata%253Ap1700%253Ap2%253Aac%253Aap%253Aneg%253Afi%253Atikwd-169717479%253Alp1003659%253Ali%253Adec%253Adm%253Appccp%253DUmFuZG9tSVYkc2RlIyh9YZVcNNsENnH02-pWD53qm9c%3Bsid%3D3148d568b8e7b2d96e1535f7bdddb22b%3Binac%3D0%26%3B&ss=Bogot%C3%A1&is_ski_area=0&ssne=Bogot%C3%A1&ssne_untouched=Bogot%C3%A1&city=-578472&checkin_year=2021&checkin_month=10&checkin_monthday=13&checkout_year=2021&checkout_month=10&checkout_monthday=20&group_adults=3&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1"

  URL_tripadvisor = "https://www.tripadvisor.co/Hotels-g294074-Bogota-Hotels.html"


  '''
  Función que sustituye los parámetros definidos por el usuario en la URL del
  proveedor seleccionado

  Las fechas de entrada y salida se definen como listas con el formato:

  [YYYY, MM, DD]

  Y se utiliza esta información dependiendo del proveedor

  '''
  def definir_parametros(self, fechaEntrada, fechaSalida, adultos, ninos, proveedor):
    if (proveedor == 'booking'):
      return (f"https://www.booking.com/searchresults.en-gb.html?aid=306395&label=bogota-Two7ruYijzWOPKEOtd23oQS549403576231%3Apl%3Ata%3Ap1700%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-169717479%3Alp1003659%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YZVcNNsENnH02-pWD53qm9c&lang=en-gb&sid=3148d568b8e7b2d96e1535f7bdddb22b&sb=1&sb_lp=1&src=city&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fcity%2Fco%2Fbogota.en-gb.html%3Faid%3D306395%3Blabel%3Dbogota-Two7ruYijzWOPKEOtd23oQS549403576231%253Apl%253Ata%253Ap1700%253Ap2%253Aac%253Aap%253Aneg%253Afi%253Atikwd-169717479%253Alp1003659%253Ali%253Adec%253Adm%253Appccp%253DUmFuZG9tSVYkc2RlIyh9YZVcNNsENnH02-pWD53qm9c%3Bsid%3D3148d568b8e7b2d96e1535f7bdddb22b%3Binac%3D0%26%3B&ss=Bogot%C3%A1&is_ski_area=0&ssne=Bogot%C3%A1&ssne_untouched=Bogot%C3%A1&city=-578472&checkin_year={fechaEntrada[0]}&checkin_month={fechaEntrada[1]}&checkin_monthday={fechaEntrada[2]}&checkout_year={fechaSalida[0]}&checkout_month={fechaSalida[1]}&checkout_monthday={fechaSalida[2]}&group_adults={adultos}&group_children={ninos}&no_rooms=1&b_h4u_keep_filters=&from_sf=1")
    elif (proveedor == 'tripadvisor'):
      pass
    else:
      return None

  def get_soup(self, url):
    #Hacer una petición GET para obtener la información en formato HTML
    r = requests.get(self.URL2, headers=self.headers)
    print(r.status_code)
    # Retornamos el objeto que va a permitir la manipulación del documento HTML
    return BeautifulSoup(r.text,'html.parser')


  
  """
  Función que asigna los valores extraidos a un diccionario
  con las propiedades para cada hotel

  """
  def extraer_info(self, nombre_hotel, rating_numero, rating, imagen, precio, tipo_habitacion, ubicacion):
    habitacion = Habitacion(precio, tipo_habitacion, imagen)

    head, sep, tail = ubicacion.partition('Show on map')
    ubicacion = head.replace('\n', '')

    hotel = Hotel(nombre_hotel, rating_numero, rating, ubicacion, habitacion)
    
    
    self.resultado.append(hotel)


  def get_resultado(self):
      return self.resultado
  
  '''
  Función que realiza el proceso de scraping para el proveedor booking.com

  '''
  def proceso_booking(self, soup):
    for item in soup.select('.sr_property_block'):
      try:
        print('---------------------------')
        #nombre hotel
        nombre_hotel = item.select('.sr-hotel__name')[0].get_text().strip()
        
        print(nombre_hotel)
        #print(item.select('.hotel_name_link')[0]['href'])
        #rating numero
        rating_numero = item.select('.bui-review-score__badge')[0].get_text().strip()
        
        print(rating_numero)
        #print(item.select('.bui-review-score__text')[0].get_text().strip())
        #rating palabra
        rating = item.select('.bui-review-score__title')[0].get_text().strip()
        
        print(rating)
        #Imagen hotel
        imagen = item.select('.hotel_image')[0]['data-highres']
        
        print(imagen)
        #Precio
        precio = item.select('.bui-price-display__value')[0].get_text().strip()
        
        print(precio)
        #Tipo de habitacion
        tipo_habitacion = item.select('.room_link')[0].get_text().strip()
        
        print(tipo_habitacion)
        #ubicacion
        ubicacion = item.select('.sr_card_address_line')[0].get_text().strip()
        
        print(ubicacion)
        
        print('---------------------------')

        self.extraer_info(nombre_hotel, rating_numero, rating, imagen, precio, tipo_habitacion, ubicacion)
        
      except Exception as e:
        #raise e
        print('salio mal', e)


  '''
  Función que realiza el proceso de scraping para el proveedor tripadvisor.com

  '''
  def ordenar_resultado(self, hoteles):
    if hoteles:
      print(hoteles, 'ordenarScraper')
      hoteles.sort(key=lambda x: x.rating_numero, reverse=True)
      print(hoteles)
    

