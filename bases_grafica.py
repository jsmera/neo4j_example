from sys import stdin
import os
clear = lambda: os.system('cls')
def menu_Votar2(id_user,id_ans):
    clear()
    v=[]
    print("Calificar")
    print("===========")
    print()
    print("Ingrese -1 para calificar afirmativamente o 1 positivamente")
    calificacion=input()
    print("Ingrese 1 si desea sensurar o 0 si no")
    censure=input()
    print("escriba (buena) o (pobre) segun como la desee calificar")
    calificacion2=input()
    #return (id_user,id_ans,censure, calificacion)
    v.append(id_user)
    v.append(id_ans)
    v.append(calificacion)
    v.append(censure)
    v.append(calificacion2)
    print()
    print("Voto realizado")
    menu_Preguntas(id_user)

def menu_Votar(id_user):
    clear()
    print("Estas son las respuestas hechas")
    print("================================")
    print()
    cnt=0
    for i in range(len(answers)):
        print(cnt,answers[i][2])  #muestra la pregunta
        cnt+=1
    print()
    print("Seleccione una respuesta")
    num=int(stdin.readline().strip())
    if(num<=cnt):
        id_ans=num  #para nuestro ejemplo, cambiar despues
        menu_Votar2(id_user,id_ans)
    else:
        menu_Votar(id_user)

def menu_Responder(id_user,id_question):
    clear()
    a=[]
    print("Responder")
    print("===========")
    print()
    print("Ingrese su respuesta")
    answer=input()
    fecha=datetime.now()
    #return (id_user,id_question,answer,fecha)
    #Guardar respuesta
    a.append(id_user)
    a.append(id_question)
    a.append(answer)
    a.append(fecha)
    answers.append(a)
    print()
    print("Respuesta posteada")
    menu_Opciones(id_user,id_question)

    
def menu_Opciones(id_user,id_question):
    clear()
    print("Seleccione una opcion para la pregunta")
    print("======================================")
    print()
    print("1. Responder la pregunta")
    print("2. Votar")
    num=int(stdin.readline().strip())
    if(num==1):
        menu_Responder(id_user,id_question)
    elif(num==2):
        menu_Votar(id_user)
    else:
        print("Opcion no valida")
        menu_Opciones(id_user,id_question)
    

def menu_Visualizar(id_user):
    clear()
    print("Estas son las preguntas hechas")
    print("===============================")
    print()
    cnt=0
    for i in range(len(questions)):
        print(cnt,questions[i][2])  #muestra la pregunta
        cnt+=1
    print()
    print("Seleccione una pregunta")
    num=int(stdin.readline().strip())
    if(num<=cnt):
        id_question=num  #para nuestro ejemplo, cambiar despues
        menu_Opciones(id_user,id_question)
    else:
        menu_visualizar(id_user)
        

def menu_Generar(id_user):
    clear()
    q=[]
    print("Realizar una pregunta")
    print("=======================")
    print()
    print("Ingrese topic")
    topic=stdin.readline()
    print("Ingrese la pregunta")
    question=stdin.readline()
    fecha=datetime.now()
    print()
    print("Pregunta generada exitosamente")
    #Guardar en base de datos, por ahora en un arreglo
    q.append(id_user)
    q.append(topic)
    q.append(question)
    q.append(fecha)
    questions.append(u)
    menu_Preguntas(id_user)


def menu_Preguntas(name):
    clear()
    id_user=name
    print("Bienvenido a las preguntas")
    print("==============================")
    print()
    print("Seleccione una opcion")
    print("1. Visualizar preguntas")
    print("2. Generar pregunta")
    print("3. Salir")
    print()
    num=int(stdin.readline().strip())
    if(num==1):
        menu_Visualizar(id_user)
    elif(num==2):
        menu_Generar(id_user)
    elif(num==3):
        menu_Principal()
    else:
        print("Opcion no valida")
        menu_Preguntas()
    

def menu_Ingresar():
    clear()
    print("Ingresar a la seccion")
    print("=======================")
    print()
    print("Ingrese nombre de usuario")
    name=stdin.readline()
    print("Ingrese contraseña")
    contraseña=stdin.readline()
    #checkear con estas dos cosas en la base de datos
    #Si es valido hago:
    menu_Preguntas(name)
    

def menu_Registrarse():
    clear()
    u=[]
    print("Registrese a continuacion")
    print("===========================")
    print()
    print("Ingrese el nombre completo")
    name=stdin.readline()
    u.append(name)
    print("Ingrese el nombre de usuario")
    user=stdin.readline()
    u.append(user)
    print("Ingrese la contraseña")
    password=stdin.readline()
    u.append(password)
    print("Ingrese el correo electronico")
    email=stdin.readline()
    u.append(email)
    print("Ingrese su rol(Estudiante, profesor, etc..)")
    rol=stdin.readline()
    u.append(rol)
    usuarios.append(u)
    print()
    print("Usted ha sido registrado exitosamente")
    menu_Principal()
    

def menu_Principal():
    clear()
    print("Bienvenido a la Base De Datos")
    print("==============================")
    print()
    print("Seleccione una opcion")
    print("1. Registrarte")
    print("2. Ingresar")
    print("3. Salir")
    print()
    num=int(stdin.readline().strip())
    if(num==1):
        menu_Registrarse()
    elif(num==2):
        menu_Ingresar()
    elif(num==3):
        return 0
    else:
        print("Opcion no valida")
        menu_Principal()
    

def main():
    global usuarios,questions,answers,votos
    usuarios=[]
    questions=[]
    answers=[]
    votos=[]
    menu_Principal()
    
main()
