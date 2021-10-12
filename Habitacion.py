class Habitacion():
    
    def __init__(self, precio, tipo, imagen ):
        self.precio = precio
        self.tipo = tipo
        self.imagen = imagen
    
    # Función que retorna la información de la habitación en un string
    def get_info(self):
      return (f'Habitación {self.tipo} a ${self.precio} la noche')