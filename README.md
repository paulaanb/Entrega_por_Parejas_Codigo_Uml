# Entrega_por_Parejas_Codigo_Uml

Este trabajo ha sido realizado por Paula Naranjo y Miguel Ángel Guerra. Hemos realizado ejercicios de clases de POO y sus respectivos UML.

Nuestra dirección de GitHub para este repositorio es la siguiente: https://github.com/paulaanb/Entrega_por_Parejas_Codigo_Uml.git

# Ejercicio 1: 


# Ejercicio 2: 


# Ejercicio 3: 
Enunciado: escriba una clase Logger, cuyo objetivo sea escribir un mensaje dado como parámetro en un archivo cada vez que se llame al método log(mensaje). La primera línea del archivo debe ser "--Start log--", seguida de los mensajes recibidos por el método log en la parte superior de un mensaje por línea, y la última línea del archivo, escrita cuando se destruye la instancia de Logger, debe ser "--End log: x log (s) -" donde x es el número de llamadas al método log. Esta clase Logger se utilizará en un método llamada() de una clase Test.

```#Empezamos a definir las clases
class Test:
    def llamada(self, string, file):
        file.write("{}".format(string))

#Definimos la funcion que importamos desde el main.py y el archivo cat log.txt para su modificacion
def main_logger():
    file = open("cat log.txt", "w")
    file.write("--Start log--\n")

#Ahora hacemos uso de la instancia como en el codigo del palindromo y utilizamos un bucle para sobreescribir el archivo cat log.txt(aunque a Ruben no le sea de mucho agrado)
    test = Test()
    for i in range(1,6): 
        if i == 1: 
            test.llamada("Primera llamada\n", file) 
        else:
                test.llamada("{}ª llamada\n".format(i), file) 
                #Creamos una orden para terminar el cat log.txt cuando obtengamos el ultimo mensaje
                if i == 5:
                    file.write("--End log: {} log(s)--".format(i))
                    file.close()
```


# Ejercicio 4: 
