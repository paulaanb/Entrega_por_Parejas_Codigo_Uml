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