if __name__ == '__main__':

    class Abuelo():
        nombre = None
        apellido = None

        def __init__(self, nombre, apellido):
            self.nombre = nombre
            self.apellido = apellido

        def informacion(self):
            print("Abuelo: Nombre: {}, Apellido: {}".format(
                self.nombre, self.apellido
            ))

    class Padre(Abuelo):
        trabajo = None

        def __init__(self, trabajo, nombre, apellido):
            self.trabajo = trabajo
            Abuelo.__init__(self, nombre, apellido)

        def informacion(self):
            print("Padre: trabajo {}".format(self.trabajo, Abuelo.informacion(self)))


    class Madre(Abuelo):
        casa = False

        def __init__(self, casa, nombre, apellido):
            self.casa = casa
            Abuelo.__init__(self, nombre, apellido)

        def informacion(self):
            print("Madre: trabajo {}".format(self.casa, Abuelo.informacion(self)))

    class Hijo(Padre, Madre):
        juguetes = None

        def __init__(self, juguetes, trabajo, casa, nombre, apellido):
            self.juguetes = juguetes
            Padre.__init__(self, trabajo, nombre, apellido)
            Madre.__init__(self, casa, nombre, apellido)

        def informacion(self):
            print("Hijo: juguetes {}".format(self.juguetes, Padre.informacion(self),
                                            Madre.informacion(self)))


    class Hija(Padre, Madre):
        juguetes = None

        def __init__(self, juguetes, trabajo, casa, nombre, apellido):
            self.juguetes = juguetes
            Padre.__init__(self, trabajo, nombre, apellido)
            Madre.__init__(self, casa, nombre, apellido)

        def informacion(self):
            print("Hija: juguetes {}".format(self.juguetes, Padre.informacion(self),
                                            Madre.informacion(self)))

abuelonum1 = Abuelo("Francisco", "Mariano")
abuelonum1.informacion()
padrenum1 = Padre("carpintero", "Guille", "Barrabás")
padrenum1.informacion()
madrenum1 = Madre("Tiene propiedades", "Eva", "Suesenaguer")
madrenum1.informacion()
hijonum1 = Hijo("5 juguetes", "Sin trabajo", "Vive con sus padres", "Espenser", "Benzema")
hijonum1.informacion()
hijanum1 = Hija("9 juguetes", "Sin trabajo", "Vive con sus padres", "Prinsa", "Rois")
hijanum1.informacion()

