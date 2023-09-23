class Mamifero(Animal):

    _listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super._init_(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        self._listado.append(self)

    def setPelaje(self, pelaje):
        self._pelaje = pelaje
    def getPelaje(self):
        return self._pelaje
    
    def setPatas(self, patas):
        self._patas = patas
    def getPatas(self):
        return self._patas

    def crearCaballo(self, nombre, edad, genero):
        caballo = Mamifero(nombre, edad, "pradera", genero, true, 4)
        caballos +=1
        return caballo
    
    def crearLeon(self, nombre, edad, genero):
        leon = Mamifero(nombre, edad, "selva", genero, true, 4)
        leones += 1
        return leon
    
    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)

    