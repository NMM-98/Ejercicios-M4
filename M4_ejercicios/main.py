if __name__ == '__main__':

    class Vehiculos():
        marca = None
        modelo = None

        def __init__(self, marca, modelo):
            self.marca = marca
            self.modelo = modelo
            print("El vehículo se ha creado con éxito")

        def repostar(self):
            print("Este vehiculo tiene que repostar gasolina")

    class VElectricos():
        marca = None
        modelo = None
        autonomia = None

        def __init__(self, marca, modelo, autonomia):
            self.marca = marca
            self.modelo = modelo
            self.autonomia = autonomia

        def repostar(self):
            print("Este vehiculo tiene que repostar electricidad")

    class BicicletaElectrica(VElectricos, Vehiculos):

        def __init__(self, marca, modelo, autonomia):
            VElectricos.__init__(self, marca, modelo, autonomia)

    class Quad(Vehiculos, VElectricos):
        def __init__(self, marca, modelo):
            Vehiculos.__init__(self, marca, modelo)

bicielectrica1 = BicicletaElectrica("smx", 20, 1000)
quad1 = Quad("rex", 1998)
bicielectrica1.repostar()
quad1.repostar()










