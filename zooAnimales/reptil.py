from zooAnimales.animal import Animal

class Reptil(Animal):

    _listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        self._listado.append(self)
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
    def getColorEscamas(self):
        return self._colorEscamas

    def setLargoCola(self, largoCola):
        self._largoCola = largoCola
    def getLargoCola(self):
        return self._largoCola

    def crearIguana(nombre, edad, genero):
        iguana = Reptil(nombre, edad, "humedal", genero, "verde", 3)
        Reptil.iguanas += 1
        return iguana
    
    def crearSerpiente(nombre, edad, genero):
        serpiente = Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        Reptil.serpientes += 1
        return serpiente

    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)