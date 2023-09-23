class Animal:

    _totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        Animal._totalAnimales += 1
    
    def setNombre(self, nombre):
        self._nombre = nombre
    def getNombre(self):
        return self._nombre
    
    def setEdad(self, edad):
        self._edad = edad
    def getEdad(self):
        return self._edad
    
    def setHabitat(self, habitat):
        self._habitat = habitat
    def getHabitat(self):
        return self._habitat
    
    def setGenero(self, genero):
        self._genero = genero
    def getGenero(self):
        return self._genero
    
    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales
    
    def totalPorTipo(self):
        return ("Mamiferos: ", Mamifero.cantidadMamiferos(), "\nAves: ", Ave.cantidadAves(), "\nReptiles: ", Reptil.cantidadReptiles(), "\nPeces: ", Pez.cantidadPeces(), "\nAnfibios: ", Anfibio.cantidadAnfibios(), sep="") 

    def toString(self):
        if zoo == null:
            return ("Mi nombre es ", self._nombre, ", tengo una edad de ", self._edad, ", habito en ", self._habitat, " y mi genero es ", self._genero, sep="")
        else:
            return ("Mi nombre es ", self._nombre, ", tengo una edad de ", self._edad, ", habito en ", self._habitat, " y mi genero es ", self._genero, ", la zona en la que me ubico es ",self._zona, ", en el zoo ", self._zoo, sep="")