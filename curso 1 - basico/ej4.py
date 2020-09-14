
###-----------------------------
###Ejemplo: ocultamiento de la implementaci�n
###-----------------------------

class Carrera:
    def __init__(self, nombre):
        self.nombre=nombre
        self.materias={}
     
    #Ocultar la implementaci�n de una colecci�n implementando un m�todo propio para agregar elementos
    def agregarMateria(self, materia, codigo):
        self.materias[codigo]=materia

class Materia:
    def __init__(self, nombre, profesor):
        self.nombre=nombre
        self.profesor=profesor
    

algebra=Materia("�lgebra", "Ricardo Quinteros")
fisica=Materia("F�sica", "Margarita Gomez")
quimica=Materia("Qu�mica", "Lorena R�os")
ing=Carrera("Ingenier�a")

#Ejemplo donde agregar elemento implica conocer la implementaci�n de la colecci�n
ing.materias[134]=algebra
ing.materias[412]=fisica

#Ejemplo donde se oculta la implementaci�n de la colecci�n
ing.agregarMateria(algebra, 134)
ing.agregarMateria(fisica, 412)

