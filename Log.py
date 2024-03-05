#Nombre:Log
#Autor:Álvaro Villar Val
#Fecha:05/03/24
#Versión:1.0.0
#Descripción: Creamos una clase para que gestione el log de la aplicación
#########################################################################################################################
class Log:
    def __init__(self):

        self.fichero="log.txt"

    def injeErr(self,error):
        f = open("log.txt", "a")
        f.write(error)
        f.close
    def limpiarLog(self):
        f = open("log.txt", "w")
        f.write("")
        f.close