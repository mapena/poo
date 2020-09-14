# -----------------------------
# Ejemplo: herencia de clases
# -----------------------------

class Empleado:

    def __init__(self, nombre, edad, legajo, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.legajo = legajo
        self.sueldoBase = sueldo

    def calcularSueldo(self, descuentos, bonos):
        return self.sueldoBase-descuentos+bonos


class AgenteVentas(Empleado): # Empleado entre() se le esta indicando que AgenteVentas herede los metodos de la
                              # de la clase Empleado.
    # Reimplementacion de metodo __init__ en la subclase
    def __init__(self, mostrador):
        self.numeroMostrador = mostrador


# Instanciar objeto de subclase
pedro = AgenteVentas(4) # se le pasa x parametro el nro de mostrador.
print(pedro.numeroMostrador)
# Atributo de superclase no existe

####
#print(pedro.nombre)  # esta linea deberia cancelar por q el campo nombre no existe en la clase
                     # a continuacion se redefine el constructor __init__ de AgenteVentas
                     # pasandole ademas el nombre,edad,legajo,sueldo
####
#-------------------------------------------------------------------------------------------------------------

# Reimplementacion de metodo __init__ llamando al de la superclase
class AgenteVentas(Empleado):
    def __init__(self, nombre, edad, legajo, sueldo, mostrador): # se definie todos los paramtros que entran a la clase
                                                                 # tanto mostrador como los parametros de la clase padre
        self.numeroMostrador = mostrador       # aca se setea el mostrador
        super().__init__(nombre, edad, legajo, sueldo) #aca se le manda los paramtros a la clase padre
                                                       #super se utiliza para indicarle que se le manda los paramtros
                                                       # a la clase padre.


# Instanciar objeto de subclase
pedro = AgenteVentas("Pedro Martinez", 32, "A120", 55000, 4)

# Atributo heredado de la superclase
print(pedro.nombre)

# M�todo heredado de la superclase
print(pedro.calcularSueldo(100, 3000))
#----------------------------------------------------------------------------------------------------------
# Subclase con metodo propio
 
class Tripulante(Empleado):
    def mostrarRenovacionLicencia(self):
        if self.edad < 50:
            print("Renueva su licencia cada 1 año")
        else:
            print("Renueva su licencia cada 6 meses")


lucas = Tripulante("Lucas Gutierrez", 40,"H618", 60000)
lucas.mostrarRenovacionLicencia()
