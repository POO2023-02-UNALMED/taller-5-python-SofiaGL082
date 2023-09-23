from zooAnimales.animal import Animal

class Anfibio(Animal):

    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super._init_(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        self._listado.append(self)
    
    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel
    def getColorPiel(self):
        return self._colorPiel
    
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso
    def getVenenoso(self):
        return self._venenoso
    
    def crearRana(self, nombre, edad, genero):
        rana = Anfibio(nombre, edad, "selva", genero, "rojo", true)
        ranas += 1
        return rana

    def crearSalamandra(self, nombre, edad, genero):
        salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", false)
        salamandras += 1
        return salamandra
    
    @classmethod
    def cantidadAnfibios(self):
        return len(cls._listado)