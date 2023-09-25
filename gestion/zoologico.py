class Zoologico:
    _zonas = []

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
    def setZona(cls, zonas):
        cls._zonas = zonas

    @classmethod
    def getZona(cls):
        return cls._zonas

    @classmethod
    def cantidadTotalAnimales(cls):
        sumaAnimalesZonas = 0
        for i in cls._zonas:
            sumaAnimalesZonas += len(i)
        return sumaAnimalesZonas
    
    def agregarZonas(self, zona):
        self._zonas.append(zona)
