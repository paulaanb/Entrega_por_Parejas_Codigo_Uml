#Enunciado: escriba una clase Logger, cuyo objetivo sea escribir un mensaje dado como parámetro en un archivo cada vez que se llame al método log(mensaje). La primera línea del archivo debe ser "--Start log--", seguida de los mensajes recibidos por el método log en la parte superior de un mensaje por línea, y la última línea del archivo, escrita cuando se destruye la instancia de Logger, debe ser "--End log: x log (s) -" donde x es el número de llamadas al método log. Esta clase Logger se utilizará en un método llamada() de una clase Test.
#Empezamos a definir las clases
class Test:
    def mensaje(self, string, file):
        file.write("{}".format(string))

#Definimos la funcion que importamos desde el main.py y el archivo cat log.txt para su modificacion
def main_logger():
    file = open("cat log.txt", "w")
    file.write("--Start log--\n")