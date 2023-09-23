class Zoologico:

    _Zonas = []
    _sumaAnimalesZonas = 0

    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion

    def setNombre(self, nommbre):
        self._nombre = nombre
    def getNombre(self):
        return self._nombre
    
    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion
    def getUbicacion(self):
        return self._ubicacion

    @classmethod
    def cantidadTotalAnimales(self):
        for i in Zoologico._Zonas:
            Zoologico._sumaAnimalesZonas += len(i)
        return Zoologico._sumaAnimalesZonas
        #Devuelve la cantidad de animales de todas las zonas
    
    def agregarZonas(self, zona):
        self._Zonas.append(zona)
