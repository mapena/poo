###-----------------------------
###Ejemplo: implementaci�n de la clase Gato
###-----------------------------

class Gato:

    #atributo de clase
    especie="mamifero"
 
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        self.alimentos=[] 
 
    def esAdulto(self):
        if self.edad>1:
            print(self.nombre, "es adulto")
        else:
            print(self.nombre, "es cachorro")

    def esAlimentoFavorito(self,alimento):
        return alimento in self.alimentos

#Instanciar un objeto Gato   
p=Gato("Pelusa",1)

#Imprimir un atributo
print(p.nombre)

#Cambiar un atributo e imprimir
p.nombre="Pelusita"
print(p.nombre)

#Agregar un atributo de forma din�mica e imprimirlo
p.raza="Siames"
print(p.raza)

#Agregar elementos a una lista que es atributo de un objeto�
p.alimentos.append("pescado")
p.alimentos.append("leche")
print(p.alimentos)

#Modificar la lista que es atributo de un objeto
p.alimentos=["leche", "galletas"]
print(p.alimentos)

#Invocar un m�todo de un objeto
p.esAdulto()
p.edad=2
p.esAdulto()
#Instanciar otro objeto de la misma clase
g=Gato("Cleo",3)

#Guardar una lista en un atributo
g.alimentos=["pescado","pan"]

#Invocar al mismo m�todo en distintos objetos
print(p.esAlimentoFavorito("leche"))
print(g.esAlimentoFavorito("leche"))

#Acceder a atributo de clase de un objeto
print(p.especie)

#Acceder a atributo de clase sin instanciar objetos
print(Gato.especie)
