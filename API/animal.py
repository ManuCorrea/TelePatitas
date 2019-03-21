from collections import defaultdict

class Animal():
    def __init__(self, grupo, foto, nombre, edad,
     raza, peso, tipoPienso = 0, cantidadPienso = 0, racionesDia = 0,
     racionActual = 0, piensosPermitidos = dict(), comederosPermitidos = set(),
     registrosUso = defaultdict(list)):

     # Características animal
     self.grupo = grupo
     self.foto = foto
     self.nombre = nombre
     self.edad = edad
     self.raza = raza
     self.peso = peso
     # Parámetros alimentacion
     self.tipoPienso = tipoPienso
     self.cantidadPienso = cantidadPienso
     self.racionesDia = racionesDia
     self.racionActual = racionActual
     self.piensosPermitidos = piensosPermitidos
     # Comederos a los que tiene acceso y los registros generados por los mismos
     self.comederosPermitidos = comederosPermitidos
     self.registrosUso = registroUso

    def añadirComedero(comedero):
        self.comedero = self.comedero.add(comedero)
        
    def eliminarComedero(comedero)
        self.comedero = self.comedero.remove(comedero)

    def añadirRegistro(comedero, registro):
        # Separamos los registros según el comedero al que estén asociados
        self.registrosUso[comedero].append(registro)
