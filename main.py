BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

import time 

import random
puntaje = random.randint (0,10)

iniciar_trivia= True
intentos=0

print (BLUE+"Bienvenido a mi trivia sobre Spiderman"+RESET)
for numero_carga in range (5,0,-1):
  print(numero_carga)
time.sleep(1)
print (GREEN+"Pondremos a prueba tu conocimiento. Debes responder las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta."+RESET)

time.sleep(1)
print(GREEN+"\nTen en cuenta que al equivocarte tendrás puntaje en contra!"+RESET)
print (GREEN+"Comenzarás con: ", puntaje, "puntos"+RESET)

time.sleep(2)
nombre = input(BLUE+ "Ingresa tu nombre y presiona 'enter': "+RESET)

while iniciar_trivia==True:
  intentos+=1
  puntaje=0

  print("\nIntento número: ", intentos)
  input("Presiona Enter para continuar")

  

  print (GREEN+"\nHola", nombre, ".Responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"+RESET)
  time.sleep(2)
  
  # Pregunta 1
  print (BLUE+"1) ¿En que año se estrenó la última película de Spiderman?"+RESET)
  print (GREEN+"a) 2019"+RESET)
  print (GREEN+"b) 2020"+RESET)
  print (GREEN+"c) 2021"+RESET)
  print (GREEN+"d) 2022"+RESET)

# Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_1 = input(BLUE+"\nTu respuesta: "+RESET)

  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input(BLUE+"Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "+RESET)
  if respuesta_1 == "a":
    puntaje -= 10
    print(GREEN+"\nIncorrecto!", nombre, "La última película de Spiderman no se estrenó en el 2019",".Tu puntaje actual es:",puntaje,"."+RESET)
  elif respuesta_1 == "b":
    puntaje -= 10
    print(GREEN+"\nIncorrecto!", nombre, "La última película de Spiderman no se estrenó en el 2020",".Tu puntaje actual es:",puntaje,"."+RESET)
  elif respuesta_1 == "d":
    puntaje -= 10
    print(GREEN+"\nIncorrecto!", nombre, "La última película de Spiderman no se estrenó en el 2022",".Tu puntaje actual es:",puntaje,"."+RESET)
  else:
    puntaje += 25
    print(GREEN+"\nMuy bien", nombre, "!",".Tu puntaje actual es:",puntaje,"."+RESET)

  time.sleep(2)  

  #pregunta 2
  print(BLUE+"\n2) ¿Cómo se llama el actor principal de la última película de Spiderman"+RESET)
  print (GREEN+"a) Andrew Garfield"+RESET)
  print (GREEN+"b) Tom Holland"+RESET)
  print (GREEN+"c) Jacob Batalon"+RESET)
  print (GREEN+"d) Tom Hardy"+RESET)
  respuesta_2 = input(BLUE+"\n Tu respuesta: "+RESET)

  while respuesta_2 not in ("a", "b", "c", "d","xx"):
    respuesta_2 = input(GREEN+"Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "+RESET)
  
  if respuesta_2 == "a":
    puntaje -= 10
    print(GREEN+"\nIncorrecto!", nombre, "Andrew Garfield no es el actor principal de la última película de Spiderman",".Tu puntaje actual es:",puntaje,"."+RESET)
  elif respuesta_2 =="xx":
    puntaje += 50
    print (GREEN+"Obtienes 50 puntos por encontrar el mensaje secreto",".Tu puntaje actual es:",puntaje,"."+RESET)
  elif respuesta_2 == "c":
    puntaje -= 10
    print(GREEN+"\nIncorrecto!", nombre, "Jacob Batalon no es el actor principal de la última película de Spiderman",".Tu puntaje actual es:",puntaje,"."+RESET)
  elif respuesta_2 == "d":
    puntaje -= 10
    print(GREEN+"\nIncorrecto!", nombre, "Tom Hardy no es el actor principal de la última película de Spiderman",".Tu puntaje actual es:",puntaje,"."+RESET)
  else:
    puntaje += 25
    print(GREEN+"\nMuy bien", nombre, "!",".Tu puntaje actual es:",puntaje,"."+RESET)

  time.sleep(2)  

  #pregunta 3
  print(BLUE+"\n3) ¿A quién le pide ayuda Peter para que las personas olvidaran que él es Spiderman?"+RESET)
  print (GREEN+"a) Ned Leeds"+RESET)
  print (GREEN+"b) Doctor Stange"+RESET)
  print (GREEN+"c) Hulk"+RESET)
  print (GREEN+"d) MJ"+RESET)

  respuesta_3 = input(BLUE+"\n Tu respuesta: "+RESET)

  while respuesta_3 not in ("a", "b", "c", 
 "d"):
    respuesta_3 = GREEN+input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "+RESET)

  if respuesta_3 == "a":
    puntaje -= 10
    print(GREEN+"\nIncorrecto!", nombre, "Peter no le pide ayuda a Ned Leeds para que las personas se olvidaran que él es Spiderman",".Tu puntaje actual es:",puntaje,"."+RESET)
  elif respuesta_3 == "c":
    puntaje -= 10
    print(GREEN+"\nIncorrecto!", nombre, "Peter no le pide ayuda a Hulk para que las personas se olvidaran que él es Spiderman",".Tu puntaje actual es:",puntaje,"."+RESET)
  elif respuesta_3 == "d":
    puntaje -= 10
    print(GREEN+"\nIncorrecto!", nombre, "Peter no le pide ayuda a MJ para que las personas se olvidaran que él es Spiderman",".Tu puntaje actual es:",puntaje,"."+RESET)
  else:
    puntaje += 25
    print(GREEN+"\nMuy bien", nombre, "!",".Tu puntaje actual es:",puntaje,"."+RESET)


  time.sleep(2)
  
   #pregunta 4
  print(BLUE+"\n4) ¿Cómo se llama el sistema de realidad aumentada, seguridad y defensa, al que Tony le da acceso a Peter ?"+RESET)
  print (GREEN+"a) S.O.S"+RESET)
  print (GREEN+"b) E.L.V.A"+RESET)
  print (GREEN+"c) E.D.I.T.H"+RESET)
  print (GREEN+"d) E.M.M.A"+RESET)

  respuesta_4 = input(BLUE+"\n Tu respuesta: "+RESET)
  while respuesta_4 not in ("a", "b", "c", "d"):
    respuesta_4 = GREEN+input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "+RESET)

  if respuesta_4 == "a":
    print( GREEN+"Totalmente incorrecto", nombre,",tu puntaje se divide a la mitad..."+RESET)
    puntaje=puntaje/2
  
  elif respuesta_4 == "b":
    print(GREEN+"Incorrecto..."+RESET)
    puntaje = puntaje - 15
  elif respuesta_4 == "d":
    print(GREEN+"Incorrecto..."+RESET)
    puntaje = puntaje - 15
  else:

    print(GREEN+"\nCorrecto", nombre, "!","Esta era la pregunta más dificil, se duplica tu puntaje !"+RESET)
    puntaje = puntaje *2 

    time.sleep(2)
  


  print(BLUE+"\nGracias", nombre, "por jugar mi trivia, alcanzaste", puntaje, "puntos"+RESET)

  print("\n ¿Deseas intentar la trivia nuevamente?")
  repetir_trivia=input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

  if repetir_trivia!="si":
    print("\nEspero", nombre, "que lo hayas pasado bien, hasta pronto.")
    iniciar_trivia= False 
