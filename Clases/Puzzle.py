#Enunciado: adivina qué mensajes se muestran mediante el siguiente código voluntariamente poco comprensible:
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