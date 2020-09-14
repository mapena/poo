###-----------------------------
###Ejemplo: herencia de clases
###-----------------------------

class Empleado:

    def __init__(self, nombre, edad, legajo, sueldo):
        self.nombre=nombre
        self.edad=edad
        self.legajo=legajo
        self.sueldoBase=sueldo
    
    def calcularSueldo(self, descuentos, bonos):
        return self.sueldoBase-descuentos+bonos
    

class AgenteVentas(Empleado):
    #Reimplementaci�n de m�todo __init__ en la subclase
    def __init__(self, mostrador):
        self.numeroMostrador=mostrador

#Instanciar objeto de subclase
pedro=AgenteVentas(4)
print(pedro.numeroMostrador)

#Atributo de superclase no existe
print(pedro.nombre)

#Reimplementaci�n de m�todo __init__ llamando al de la superclase
class AgenteVentas(Empleado):
    def __init__(self, nombre, edad, legajo, sueldo, mostrador):
        self.numeroMostrador=mostrador
        super().__init__(nombre, edad, legajo, sueldo)

#Instanciar objeto de subclase
pedro=AgenteVentas("Pedro Martinez", 32, "A120", 55000, 4)

#Atributo heredado de la superclase
print(pedro.nombre)

#M�todo heredado de la superclase
print(pedro.calcularSueldo(100, 3000))

#Subclase con m�todo propio
class Tripulante(Empleado):        
    def mostrarRenovacionLicencia():
        if self.edad<50:
            print("Renueva su licencia cada 1 a�o")
        else:
            print("Renueva su licencia cada 6 meses")

lucas=Tripulante("Lucas Gutierrez", "H618", 60000, 40)
print(lucas.mostrarRenovacionLicencia())
