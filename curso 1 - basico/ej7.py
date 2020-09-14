
###-----------------------------
###Ejemplos: polimorfismo
###-----------------------------

#Strings, listas y otros contenedores implementan el "iterator protocol"
for elemento in "hola":
    print(elemento)

for elemento in [1,2,3,4]:
    print(elemento)

#El m�todo len es polim�rfico porque se aplica a distintos tipos de objetos 
len("hola")
len([1,2,3,4])

#Sobrecarga de operadores
"Hola"+" y adios"
1+2

#Sobrecarga de m�todo con valor por defecto
class Empleado:
    def __init__(self, nombre, legajo, sueldo):
        self.nombre=nombre
        self.legajo=legajo
        self.sueldoBruto=sueldo

    def calcularSueldo(self, descuentos):
        return self.sueldoBruto-descuentos

class Gerente(Empleado):
    def calcularSueldo(self, descuentos, bonificaciones=0):
        return self.sueldoBruto-descuentos+bonificaciones

marcos=Empleado("Marcos R�os", 221, 30000)
julia=Gerente("Julia Campos", 109, 60000)

print(marcos.calcularSueldo(3000))
print(julia.calcularSueldo(10000, 2000))