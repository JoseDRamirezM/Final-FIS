import sqlite3

from sqlite3 import Error

def sql_connection():

    try:

        con = sqlite3.connect('mydatabase.db')

        return con

    except Error:

      return None

def sql_table(con):

    try:

      cursorObj = con.cursor()

      cursorObj.execute("CREATE TABLE precios(id integer PRIMARY KEY, nombre_hotel text, ubicacion text, tipo_habitacion text, precio text, rating_numero text, rating text)")

      con.commit()

    except Error:

        return None

def sql_insert(con, entities):

    try:

      cursorObj = con.cursor()
      
      cursorObj.execute('INSERT INTO precios(id, nombre_hotel, ubicacion, tipo_habitacion, precio, rating_numero, rating) VALUES(?, ?, ?, ?, ?, ?, ?)', entities)
      
      con.commit()

    except Error:

        return None
