# Entrega_por_Parejas_Codigo_Uml

Este trabajo ha sido realizado por Paula Naranjo y Miguel Ángel Guerra. Hemos realizado ejercicios de clases de POO y sus respectivos UML.

Nuestra dirección de GitHub para este repositorio es la siguiente: https://github.com/paulaanb/Entrega_por_Parejas_Codigo_Uml.git

# Ejercicio 1: 
 UML: ![Palindromo_clase](https://user-images.githubusercontent.com/100090620/159370293-4e6db728-e536-4c51-b2c7-bc62aaf1ca92.png)

Enunciado: crear una clase Palindromo que contenga un método de clase esPalindromo(), que devuelve un valor booleano que indica si una cadena de caracteres pasada como argumento es un palíndromo. Un palíndromo es una cadena que se puede leer de izquierda a derecha o de derecha a izquierda. Se tienen en cuenta los caracteres no alfanuméricos.

```
frase = str(input('Introduce la frase: '))
sum = 0
max = 0
letras = []
n = int(len(frase))
for i in range(0,n):
  if(frase[i: i + 1]!=' '):
    letras.append(frase[i: i + 1])
    max = max + 1
while(letras[sum]==letras[max - 1 - sum] and sum<max/2):
  print(str(sum) + letras[sum] + letras[max-1-sum])
  sum = sum + 1
  if(sum==int(max/2)):
    print('La frase es palíndromo')
  else:
    print('La frase no es palídormo')
```
```
#Codigo alternativo
#Definimos la clase palindromo
class palindromo():
  def __init__(self,palabra):
    self.palabra=palabra
  def comprobacion(self):
    palabra=input("Por favor, introduzca la palabra que desea comprobar.")
    if palabra == " ".join(reversed(palabra)).
      print("True")
    else:
      print("False")
print(palindromo.comprobacion("palabra"))
```
# Ejercicio 2: 
UML: ![Palindromo_instancia](https://user-images.githubusercontent.com/100090620/159371948-a0e1a2b4-4131-4c25-a950-e03938d9810a.png)


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
Enunciado: adivina qué mensajes se muestran mediante el siguiente código voluntariamente poco comprensible:

```
#Definimos la clase que vamos a utilizar
class A: 
    def z(self): 
        return self
 
    def y(self, t): 
        return len(t) 

#Definimos la funcion importada desde main.py
    a = A 
    y = a.z
    print(y(a))
    aa = a()
    print(aa is a())
    z = aa.y
    print(z(()))
    print(a().y((a,))) 
    print(A.y(aa, (a,z)))
    print(aa.y((z,1,'z')))

#Los resultados que van a quedar quedan definimos por la funcion importada desde el main.py
#El primer print da como resultado "class '__main__.A" debido al self que definimos anteriormente en z
#El segundo print da como resultado "False", pues la condicion introducida no es verdadera
#El tercer print da como resultado 0, puesto que no hemos establecido la longuitud correctamente dentro de z
#El cuarto print da como resultado 1, puesto que dentro de len(a) hay un elemento
#El quinto print da como resultado 2, puesto que dentro de len(a,z) hay 2 elementos
#El sexto y ultimo print da como resultado 3, puesto que dentro de len(Z,1,'z') hay 3 elementos
