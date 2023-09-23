class Zona:

    _Animales = []

    def__init__(self, nombre, zoo):
        self._nombre = nombre
        self._zoo = zoo
    
    def setNombre(self, nombre):
        self._nombre = nombre
    def getNombre(self):
        return self._nombre

    def setZoo(self, zoo):
        self._zoo = zoo
    def getZoo(self):
        self._zoo
    
    def agregarAnimales(self, animal):
        self._Animales.append(animal)
    
    def cantidadAnimales(self):
        return len(self._Animales)
    
    