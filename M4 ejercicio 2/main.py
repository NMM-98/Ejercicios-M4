if __name__ == '__main__':

    class Personal_Universitario():
        id = None
        nombre = None
        email = None

        def __init__(self, id, nombre, email):
            self.id = id
            self.nombre = nombre
            self.email = email
        def informacion(self):
            print("Objeto Personal Universitario: id: {}, nombre: {}, email: {}".format(
                self.id, self.nombre, self.email
            ))


    class Oficina(Personal_Universitario):
        puesto = None
        def __init__(self, puesto, id, nombre, email):
            self.puesto = puesto
            Personal_Universitario.__init__(self, id, nombre, email)

        def informacion(self):
            print("Objeto oficina puesto: {}".format(
                self.puesto, Personal_Universitario.informacion(self)
            ))


    class Profesor(Personal_Universitario):
        especializacion = None
        def __init__(self, especializacion, id, nombre, email):
            self.especializacion = especializacion

            Personal_Universitario.__init__(self, id, nombre, email)

        def informacion(self):
            print("Objeto profesor puesto: {}".format(
                self.especializacion, Personal_Universitario.informacion(self)
            ))

    class Alumno(Personal_Universitario):
        creditosAprobados = None
        def __init__(self, creditosAprobados, id, nombre, email):
            self.creditosAprobados = creditosAprobados

            Personal_Universitario.__init__(self, id, nombre, email)
        def informacion(self):
            print("Objeto alumno puesto: {}".format(
                self.creditosAprobados, Personal_Universitario.informacion(self)
            ))

    oficina1 = Oficina("Boss", 43456, "Nel", "223ggg@gmail.com")
    oficina1.informacion()
    profesor1 = Profesor("Matemáticas", 3331, "Manuel", "2220manuel@gmail.com")
    profesor1.informacion()
    alumno1 = Alumno(5, 222, "Rodolfo", "soyalumno1@gmail.com")
    alumno1.informacion()








