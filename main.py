#Creamos el archivo main.py que importaremos mas tarde dentro de clases
if __name__ == "__main__":

    from Clases.Logger import main_logger
    print ("El ejercicio Logger es el siguiente:")
    main_logger()
    print ("\n")

    from Clases.Puzzle import main_puzzle
    print ("El ejercicio Puzzle es el siguiente:")
    main_puzzle()
    print ("\n")

    from Clases.Palidromo_metodo_de_clase import main_palidromo_metodo_de_clase
    print ("El ejercicio Palidromo metodo de clase es el siguiente:")
    main_palidromo_metodo_de_clase()
    print ("\n")

    from Clases.Palidromo_metodo_de_instancia import main_palidromo_metodo_de_instancia
    print("El ejercicio Palidromo metodo de instancia es el siguiente:")
    main_palidromo_metodo_de_instancia()
    print("\n")