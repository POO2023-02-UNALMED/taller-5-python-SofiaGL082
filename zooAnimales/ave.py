from zooAnimales.animal import Animal

class Ave(Animal):

    _listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)
    
    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas
    def getColorPlumas(self):
        return self._colorPlumas

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        halcon = cls(nombre, edad, "montanas", genero, "café glorioso")
        cls.halcones += 1
        return halcon
    
    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        aguila = cls(nombre, edad, "montanas", genero, "blanco y amarillo")
        cls.aguilas += 1
        return aguila
    
    @staticmethod
    def cantidadAves():
        return len(Ave._listado)