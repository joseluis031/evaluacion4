import os
import helpers


def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print("========================")
        print("  Bienvenido a Evaluacion 4  ")
        print("========================")
        print("[1] Ejercicio 1 ")
        print("[2] Ejercicio 2   ")
        print("[3] Ejercicio 3   ")
        print("[4] Cerrar programa")
        print("========================")

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Enunciado del ejercicio 1...\n")
            from Ej1.ejercicio1_1 import HuffmanTree

            dict ={'a':0.2,'f':0.17,"1":0.13,"3":0.21,"0":0.05,"M":0.09,"T":0.15}
            a = HuffmanTree(dict)
            a.get_code()
            print()
            print()
            from Ej1.apartefinal import codificar,decodificar,decimal

            a = input("¿que deseas codificar?")
            b = codificar(a)
            print(b)

            c = input("¿que deseas decodificar(en binario por favor)?")
            d = decodificar(c)
            print(d)

            



        elif opcion == '2':
            print("Enunciado del ejercicio 2...\n")


        elif opcion == '3':
            print("Enunciado del ejercicio 3...\n")


        
        elif opcion == '4':
            print("Saliendo del programa...\n")
            break

        input("\nPresiona ENTER para continuar...")
        
