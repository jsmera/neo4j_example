from sys import stdin
from main import Connection
from datetime import datetime
import os

cc = Connection()
clear = lambda: os.system('clear')
id_user = None


def menu_Votar2(answer):
  clear()
  print("Calificar")
  print("===========")
  print()
  print("Ingrese -1 para calificar afirmativamente o 1 positivamente")
  calificacion = input()
  print("Ingrese 1 si desea sensurar o 0 si no")
  censure = input()
  print("Escriba (buena) o (pobre) segun como la desee calificar")
  calificacion2 = input()
  print()
  cc.make_vote(calificacion, id_user, answer.id, censure, calificacion2)
  print("Voto realizado")
  return 0

def menu_Votar(question):
  clear()
  print("Estas son las respuestas hechas")
  print("================================")
  print()
  cnt = 1
  answers = cc.list_answers_to_question(question.id)
  for a in answers:
    print(cnt, a.get("answer"))  #muestra la pregunta
    cnt += 1
  print()
  print("Seleccione una respuesta")
  print("{}. Para volver".format(cnt))
  num = int(stdin.readline().strip())
  while not (1 <= num<= cnt):
    print("Seleccione una respuesta")
    num = int(stdin.readline().strip())
  if num < cnt:
    answer = answers[num-1]  #para nuestro ejemplo, cambiar despues
    if menu_Votar2(answer) == 0:
      menu_Votar(question)
  else:
    return 0

def menu_Responder(id_question):
  clear()
  print("Responder")
  print("===========")
  print()
  print("Ingrese su respuesta")
  answer = input()
  fecha = datetime.now()
  print()
  cc.make_a_answer(id_user, id_question, answer, fecha)
  print("Respuesta posteada")
  return 0

    
def menu_Opciones(question):
  clear()
  print("Seleccione una opcion para la pregunta")
  print("======================================")
  print()
  print(question.get("question"))
  print(question.get("date"))
  print()
  print("1. Responder la pregunta")
  print("2. Votar respuestas")
  print("3. Volver")
  num = int(stdin.readline().strip())
  while not (1 <= num <= 3):
    print("Seleccione una opcion para la pregunta")
    num = int(stdin.readline().strip())

  if num==1:
    if menu_Responder(question.id) == 0:
      menu_Opciones(question)
  elif num==2:
    if menu_Votar(question) == 0:
      menu_Opciones(question)
  else:
    return 0
    

def menu_Visualizar():
  clear()
  print("Estas son las preguntas hechas")
  print("===============================")
  print()
  questions = cc.list_questions()
  cnt = 1
  for q in questions:
    print(cnt, q.get('question'))  #muestra la pregunta
    cnt += 1
  print()
  print("Seleccione una pregunta")
  print("{}. Para volver".format(cnt))
  num = int(stdin.readline().strip())
  while not (1 <= num<= cnt):
    print("Seleccione una pregunta")
    num = int(stdin.readline().strip())
  if num < cnt:
    question = questions[num-1]  #para nuestro ejemplo, cambiar despues
    if menu_Opciones(question) == 0:
      menu_Visualizar()
  else:
    return 0


def menu_Generar():
  clear()
  print("Realizar una pregunta")
  print("=======================")
  print()
  print("Ingrese topic")
  topic = stdin.readline().strip()
  print("Ingrese la pregunta")
  question = stdin.readline().strip()
  fecha = datetime.now()
  print()
  cc.make_a_question(id_user, topic, question, fecha)
  print("Pregunta generada exitosamente")
  #Guardar en base de datos, por ahora en un arreglo
  return 0


def menu_Preguntas():
  clear()
  print("Bienvenido a las preguntas")
  print("==============================")
  print()
  print("Seleccione una opcion")
  print("1. Visualizar preguntas")
  print("2. Generar pregunta")
  print("3. Salir")
  print()
  num = int(stdin.readline().strip())
  while not (1<= num <= 3):
    print("Opcion no valida")
    print("Seleccione una opcion")
    num=int(stdin.readline().strip())

  if(num==1):
    if menu_Visualizar() == 0:
      menu_Preguntas()
  elif(num==2):
    if menu_Generar() == 0:
      menu_Preguntas()
  else:
    return 0

def menu_Ingresar():
  global id_user
  clear()
  print("Ingresar a la seccion")
  print("=======================")
  print()
  print("Ingrese nombre de usuario")
  name=stdin.readline().strip()
  print("Ingrese contraseña")
  contraseña=stdin.readline().strip()
  id_user = cc.login(name, contraseña)
  if id_user is None:
    print("Credenciales invalidas")
    return 0
  if menu_Preguntas() == 0:
    return 0
    

def menu_Registrarse():
  global id_user
  clear()
  u=[]
  print("Registrese a continuacion")
  print("===========================")
  print()
  print("Ingrese el nombre completo")
  name=stdin.readline().strip()
  u.append(name)
  print("Ingrese el nombre de usuario")
  user=stdin.readline().strip()
  u.append(user)
  print("Ingrese la contraseña")
  password=stdin.readline().strip()
  u.append(password)
  print("Ingrese el correo electronico")
  email=stdin.readline().strip()
  u.append(email)
  print("Ingrese su rol(Estudiante, profesor, etc..)")
  rol=stdin.readline().strip()
  u.append(rol)
  print()
  print("Usted ha sido registrado exitosamente")
  id_user = cc.create_user(u[0], u[1], u[3], u[2], u[4])
  return 0
    

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
  while not (1 <= num <= 3):
    print("Opcion no valida")
    print("Seleccione una opcion")
    num=int(stdin.readline().strip())

  if num==1:
    if menu_Registrarse() == 0:
      menu_Principal()
  elif num==2:
    if menu_Ingresar() == 0:
      menu_Principal()
  else:
    return 0
    

def main():
  menu_Principal()
    
main()
