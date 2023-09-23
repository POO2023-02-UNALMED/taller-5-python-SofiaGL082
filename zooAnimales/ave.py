from zooAnimales.animal import Animal

class Ave(Animal):

    _listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        self._listado.append(self)
    
    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas
    def getColorPlumas(self):
        return self._colorPlumas

    def crearHalcon(nombre, edad, genero):
        halcon = Ave(nombre, edad, "montanas", genero, "café glorioso")
        Ave.halcones += 1
        return halcon
    
    def crearAguila(nombre, edad, genero):
        aguila = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        Ave.aguilas += 1
        return aguila
    
    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)