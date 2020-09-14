###-----------------------------
###Ejemplo: ocultamiento de atributos
###-----------------------------

#Ejemplo en que se accede a un atributo p�blico y se crea una nueva referencia a �l
copia=ing.materias
print(len(ing.materias)

#Mediante la nueva referencia, se modifica la colecci�n contenida en el objeto
copia[999]=quimica
print(len(ing.materias))

class Carrera:
    def __init__(self, nombre):
        self.nombre=nombre
 #Atributo oculto
     self.__materias={}
     
 def agregarMateria(self, materia, codigo):
        self.__materias[codigo]=materia
 
#El atributo es inaccesible mediante su nombre 
copia=ing.__materias

