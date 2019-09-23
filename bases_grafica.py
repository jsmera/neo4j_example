from sys import stdin
from datetime import datetime

def menu_Registrarse():
    print("Registrese a continuacion")
    print("--------------------------")
    print("Ingrese")


def Ingresar():
		print("Ingresar a la seccion")
		print("--------------------------")
		print("Ingrese nombre de usuario")
		name=input()
		print("--------------------------")
		print("Ingrese contraseña")
		contraseña = input()
		print("--------------------------")
		#checkear con estas dos cosas en la base de datos		
		return (name,contraseña)

def preguntas():
		if login == True:
				print("Realizar una pregunta")
				print("--------------------------")
				print("Ingrese topic")
				topic=input()
				print("Ingrese la pregunta")
				question = input()
				fecha=datetime.now()
				return (topic,question,fecha)

def menu_secundario():
    print("Bienvenido a las preguntas")
    print("==============================")
    print()
    print("Seleccione una opcion")
    print("1. Visualizar preguntas")
    print("2. Generar pregunta")
    print()

def menu_Principal():
    print("Bienvenido a la Base De Datos")
    print("==============================")
    print()
    print("Seleccione una opcion")
    print("1. Registrarte")
    print("2. Sistema de preguntas")
    print()
    

def main():
    menu_Principal()
    num=int(stdin.readline().strip())
    while(num!=0):
        if(num==1):
            
        num=int(stdin.readline().strip())


    
main()
