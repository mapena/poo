
###-----------------------------
###Ejemplo: property y setter para atributos privados
###-----------------------------

class Materia:
    def __init__(self, nombre, profesor, fecha):
        self.nombre=nombre
        self.profesor=profesor
 self.fechaInicioDictado=fecha  #no puede ser anterior a 2006
    
    @property
    def fechaInicioDictado(self):
        print("Se est� accediendo mediante property")
        return self._fechaInicioDictado

    @fechaInicioDictado.setter
    def fechaInicioDictado(self, fecha):
        if fecha<2006:
            self._fechaInicioDictado=2006
        else:
            self._fechaInicioDictado=fecha

#Instanciar objetos asignando valores al atributo mediante su setter
algebra=Materia("�lgebra", "Ricardo Quinteros", 2010)
fisica=Materia("F�sica", "Margarita Gomez", 2015)
quimica=Materia("Qu�mica", "Lorena R�os", 2005)

#Acceder a atributos mediante property
print(algebra.fechaInicioDictado)
print(fisica.fechaInicioDictado)
print(quimica.fechaInicioDictado)

