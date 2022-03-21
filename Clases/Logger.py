#Enunciado: adivina qué mensajes se muestran mediante el siguiente código voluntariamente poco comprensible:

#Empezamos a definir las clases
class Descodificación:
    def mensaje(self, string, file):
        file.write("{}".format(string))