import tkinter as tk
#from PIL import ImageTk, Image
import os
from tkinter import font
from typing import Container, cast
import Scraper
from tkcalendar import Calendar
from PIL import ImageTk, Image
from urllib.request import urlopen
from io import BytesIO
from resizeimage import resizeimage

creds = 'tempfile.temp'


def iniciar_sesion():
    global usernameL
    global passwordL
    global login

    login = tk.Tk()
    login.title('Iniciar Sesion')
    login.geometry('320x180')
    center(login)
    icon = tk.PhotoImage(file="logo.PNG")
    login.iconphoto(False, icon)
    login.config(bd=10, background="#3b6978")
    #login.resizable(False, False)
    instruction = tk.Label(
        login, text='Ingrese sus credenciales\n', fg='white', font=("calibri", 16))
    instruction.config(background="#3b6978")
    instruction.grid(sticky=tk.E, columnspan=2)

    nameL = tk.Label(login, text='Usuario: ',
                     fg='white', font=("calibri", 12))
    nameL.config(background="#3b6978", bd=10)
    pwordL = tk.Label(login, text='Contraseña: ',
                      fg='white', font=("calibri", 12))
    pwordL.config(background="#3b6978", bd=10)
    nameL.grid(row=1, sticky=tk.W)
    pwordL.grid(row=2, sticky=tk.W)

    usernameL = tk.Entry(login, width=30)
    passwordL = tk.Entry(login, show='*', width=30)
    usernameL.grid(row=1, column=1, columnspan=2)
    passwordL.grid(row=2, column=1, columnspan=2)

    iniciar_sesionB = tk.Button(
        login, text='iniciar_sesion', command=verificar_credenciales)
    iniciar_sesionB.grid(columnspan=3, sticky=tk.E)

    login.mainloop()


def verificar_credenciales():
    with open(creds) as f:
        data = f.readlines()
        uname = data[0].rstrip()
        pword = data[1].rstrip()

    if usernameL.get() == uname and passwordL.get() == pword:
        ventana_inicio()
    else:
        fail = tk.Tk()
        fail.title('D:')
        fail.geometry('150x50')
        rlbl = tk.Label(fail, text='\n[! Datos incorrectos')
        rlbl.pack()
        fail.mainloop()


def ventana_inicio():
    cerrar_ventana(login)
    global inicio
    global fecha_in
    global fecha_sal
    global num_adultos
    global num_niños

    inicio = tk.Tk()
    inicio.protocol("WM_DELETE_WINDOW", inicio.iconify)
    inicio.bind('<Escape>', lambda e: inicio.destroy())
    inicio.title('Inicio')
    inicio.geometry('740x370')
    center(inicio)
    icon = tk.PhotoImage(file="logo.PNG")
    inicio.iconphoto(False, icon)
    inicio.config(bd=10, background="#3b6978")
    inicio.resizable(False, False)
    instruction = tk.Label(
        inicio, text='Ingrese los parametros de busqueda\n', fg='white', font=("calibri", 22))
    instruction.config(bd=10, background="#3b6978")
    instruction.grid(sticky=tk.E, columnspan=3)

    fecha_in = tk.StringVar()
    fecha_sal = tk.StringVar()
    num_adultos = tk.IntVar()
    num_niños = tk.IntVar()

    cal = Calendar(inicio, selectmode='day',
                   year=2021, month=10,
                   day=11, date_pattern="y-mm-dd")

    cal.grid(row=1, sticky=tk.E, padx=15, columnspan=2, rowspan=4)

    entrada = tk.Label(inicio, text='Fecha de ingreso: ',
                       fg='white', font=("calibri", 18))
    entrada.config(bd=5, background="#3b6978")
    salida = tk.Label(inicio, text='Fecha de salida: ',
                      fg='white', font=("calibri", 18))
    salida.config(bd=5, background="#3b6978")
    adultos = tk.Label(inicio, text='personas: ')
    adultos.config(bd=5, background="#3b6978",
                   fg='white', font=("calibri", 18))
    niños = tk.Label(inicio, text='niños: ')
    niños.config(bd=5, background="#3b6978",
                 fg='white', font=("calibri", 18))

    entrada.grid(row=1, column=2, sticky=tk.W)
    salida.grid(row=2, column=2, sticky=tk.W)
    adultos.grid(row=3, column=2, sticky=tk.W)
    niños.grid(row=4, column=2, sticky=tk.W)

    entrada = tk.Entry(
        inicio,
        textvariable=fecha_in
    )
    salida = tk.Entry(
        inicio,
        textvariable=fecha_sal
    )
    adultos = tk.Entry(
        inicio,
        validate="key",
        validatecommand=(inicio.register(validar_entrada), "%S"),
        textvariable=num_adultos
    )
    niños = tk.Entry(
        inicio,
        validate="key",
        validatecommand=(inicio.register(validar_entrada), "%S"),
        textvariable=num_niños
    )

    entrada.grid(row=1, column=4, columnspan=2)
    salida.grid(row=2, column=4, columnspan=2)
    adultos.grid(row=3, column=4, columnspan=2)
    niños.grid(row=4, column=4, columnspan=2)

    buscar_btn = tk.Button(inicio, text='Buscar precios',
                           command=buscar_precios)
    buscar_btn.grid(column=6, padx=15)

    def set_entrada():
        entrada.insert(0, cal.get_date())

    def set_salida():
        salida.insert(0, cal.get_date())
        # salida.split('/')

    entrada_btn = tk.Button(inicio, text='seleccionar fecha',
                            command=set_entrada).grid(row=1, column=6, padx=15)
    salida_btn = tk.Button(inicio, text='seleccionar fecha',
                           command=set_salida).grid(row=2, column=6, padx=15)

    inicio.mainloop()


def buscar_precios():
    try:
        parametros = {
            'ingreso': [int(e) for e in fecha_in.get().split('-')],
            'salida': [int(e) for e in fecha_sal.get().split('-')],
            'adultos': num_adultos.get(),
            'niños': num_niños.get()
        }
        if parametros['ingreso'] and parametros["salida"] != []:
            if parametros['adultos'] > 0:
                ventana_resultados(parametros)
            else:
                print('Rellene todo')
        else:
            print('Rellene todo')
    except:
        print("Parece que algo anda mal!")


def validar_entrada(texto):
    return texto.isdecimal()


def ventana_resultados(parametros):
    ventana = tk.Toplevel()
    ventana.title('Buscador de precios')
    ventana.geometry('700x400')
    center(ventana)
    iconvp = tk.PhotoImage(file="logo.PNG")
    ventana.iconphoto(False, iconvp)
    ventana.config(bd=10, background="#3b6978")
    rlbl = tk.Label(ventana, text='Resultados de la búsqueda',
                    fg='white', font=("calibri", 22))
    rlbl.config(bd=10, background="#3b6978")
    rlbl.pack()

    frame = tk.Frame(ventana, padx=40, background="#3b6978")
    frame.pack(expand=1, fill=tk.BOTH)
    canvas = tk.Canvas(frame, bg='yellow')
    canvas.pack(side=tk.LEFT, expand=1, fill=tk.BOTH)
    cont_frame = tk.Frame(canvas, bg="blue")
    can_frame = canvas.create_window((0, 0), window=cont_frame, anchor=tk.NW)
    vbar = tk.Scrollbar(canvas, orient=tk.VERTICAL)
    vbar.config(command=canvas.yview)
    vbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.config(yscrollcommand=vbar.set)

    frame.bind('<Configure>', lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")))

    canvas.bind('<Configure>', lambda e: canvas.itemconfig(
        can_frame, width=e.width))

    scraper = Scraper.Scraper()
    # tomar resultados de la otra ventana
    while scraper.get_resultado() == []:
        
        soup = scraper.get_soup(scraper.definir_parametros(
            parametros["ingreso"], parametros["salida"], parametros["adultos"], parametros["niños"], 'booking'))
        scraper.proceso_booking(soup)
    hoteles = scraper.get_resultado()
    for hotel in scraper.get_resultado():
        cont = tarjeta_hotel(hotel, cont_frame)
        cont.pack(expand=1, fill=tk.BOTH)

    reporte_btn = tk.Button(
        ventana, text='Generar reporte', command=lambda: scraper.guardar_datos(scraper.get_resultado()))
    reporte_btn.pack(side=tk.RIGHT, pady=15)
    ordenar_btn = tk.Button(
        ventana, text='Ordenar por precio', command=lambda:ordenar(scraper, hoteles ,cont_frame))
    ordenar_btn.pack(side=tk.LEFT, pady=15)
    ventana.update()
    ventana.mainloop()

def ordenar(scraper, hoteles, frame):
  scraper.ordenar_resultado(hoteles)
  for hotel in scraper.get_resultado():
      cont = tarjeta_hotel(hotel, frame)
      cont.pack(expand=1, fill=tk.BOTH)
  frame.update()


def tarjeta_hotel(hotel, ven):
    contenedor = tk.LabelFrame(ven, pady=20, padx=20)
    u = urlopen(hotel.habitacion.imagen)
    raw_data = u.read()
    u.close()
    im = Image.open(BytesIO(raw_data))
    im = resizeimage.resize_cover(im, [220, 220])
    photo = ImageTk.PhotoImage(im, master=contenedor)

    img = tk.Label(contenedor, text='**imagen**',
                   bd=2, relief='raised', image=photo)
    img.image = photo

    texto = tk.Label(contenedor, bd=2, padx=10, relief='raised',
                     text=f'Hotel: {hotel.nombre}\nCalificación:  {hotel. rating_numero}\nValoración: {hotel.rating}\nUbicación: {hotel.ubicacion}\nHabitacion:\nPrecio:{hotel.habitacion.precio}\nTipo:\n{hotel.habitacion.tipo}')

    img.pack(side=tk.LEFT)
    texto.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
    return contenedor


def cerrar_ventana(ventana):
    ventana.destroy()


def ver_habitacion(habitacion):
    pass


def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
