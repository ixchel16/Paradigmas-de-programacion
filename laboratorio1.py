'''ESTE ES UN SUPERCOMENTARIO 
   DE INICIO A NUESTRO RESUMEN
'''
#===================================
# PARA PONER EL CODIGO CON COLOR ES:
# :syntax on
#================================


#===================
# Operaciones básicas
#==================

print   (2+3)
print   (2*3)
print   (2/3)
print   (2**10)
print   (2**0.5)    #raíz cuadrada 
print   (10%2)
print   (10%0.1)    #exclusivo en python



#=========================================
# Para saber el tipo de objeto se usa type
#=========================================

t = 0
print   (type(t))  #entero

t = 3.6
print   (type(t))  #real (float)

t = True
print   (type(t))  # boleano (bool)



#====================
# Mensajes a Pantalla
#====================

print   ("Este es un comando de python. ", "Este es otro enuncioado. ", t)
print   ('id: ', 1)
print   ('First Name: ', 'Jobs')
print   ('Vamos a sumar esto' + 'con esto otro')



#============================================
#Continuar una instruccion en varios renglones
#============================================

if 100 > 999 and \
    200 <= 300 and \
    True != False:
    print('Hello world!')


#======================================
#Comandos diferentes en la misma linea
#=====================================

print ('Hola ');  print ("tú!");  #se considera mala practica 


#==============================================
# Usando parentesis redonodos, cuadrados o llaves
# se puede escribir en varios renglones
#==============================================

list = [1, 2, 3, 4, 
        5, 6, 7, 8, 
        9, 10, 11, 12]

matriz = [[1,2,3,4], [5,6,7,8], [9, 10, 11, 12]]

print (list)
print (matriz)


#================================================================
# Identación estricta para procesos dependientes de: (dos puntos) con dos puntos misma identacion
#================================================================
if 10>5:
    print ("diez es mayor que cinco")
    print ("otra identación")

for i in list:
        print (i)
        print("ok")

if 10>5: 
    print ("verdadero")

if 10<20:
    print ("verdadero")

elif 5>3: #comienza segundo condicional
    print ("Esto no se imprimirá")

else:
  print ("Aquí nunca llega")

#==========
# FUnciones
#==========

def say_hello(name):
    print ("hello", name)
    print ("welcome to python Tutorials")

say_hello("Julián")


#==================================================================================================
#                                                PARTE 2 VIDEO UNO
#==================================================================================================

#--------------------------------------------------
# Input permite obtener datos del usuario en prompter
#---------------------------------------------------
nombre = input("Dame tu nombre: ")
print("Hola como estás? ", nombre)

#--------------------------------------
# Los enteros son de precisión limitada
#--------------------------------------
y = 5000000000000000000000000000000000
print(y)

#----------------------------------------------------------
# Se puede delimitar números con guion bajo pero no con coma
#----------------------------------------------------------
y = 5_000_000
print(y)

#---------------------------------------------------
# La función int() cambia strings y floats a enteros
#--------------------------------------------------
numero = int(input("Dame tu edad: "))
type(numero)

#--------------------------------------------------
# La notacion cientifica de flotantes utiliza e o E
#--------------------------------------------------

# 1.2 x10^{0.9}

y = 1.2E-09

#-------------------------------------------------------
# la funcón float() convierte strings y enteros a floats
#-------------------------------------------------------
y = float("14.3")
print(y)


# ==================================================
# Los complejos se escriben con la raíz de menos uno
# j siempre con un número como prefijo
# no acepta la j suelta
# ===================================================

z = 1 + 1j

# suma + 
# resta - 
# multiplicación *
# divison /
# módulo %
# exponente **
# // función piso
# Funciones para transformar números de int() float() complex()
# Iperaciones abs() round() pow()

print (round(3.14159,4))

#==========================
# String de varias lineas
#==========================
parrafo = """ En el bosque de la china

la chinita se perdió """

print (parrafo)


# --------------------------------------------
#La funcion len() obtiene el tamaño del string
#---------------------------------------------
n = len(parrafo)
print(n)

#------------------------------------------------------------
# Las letras de un string ocupan lugares como en un arreglo
# (también de atrás para adeltante comenzamos en -l el último)
#-------------------------------------------------------------
palabra = "hola"
print(palabra[0])
print(palabra[-4])


#============================================
#		CONDICIONLAES
#============================================

precio = 50

#-------------
# Si esto.....
#--------------

if precio < 50:
  print("El precio es menor a 50")

#-----------------------------
# Sí no..... si otro otro....
#-----------------------------

elif precio > 50:
	print("El precio es mayor a 50")

#------------------------------
# Si nada de lo anterior .......
#------------------------------

else:
  print("El precio es 50")


precio = 50
cantidad = 5
total = precio*cantidad

#========================
# Condicionlaes anidados
#=======================
if total > 100:
    if total > 500:
	print("Total es mayor que 500")
    else:
	if total < 500 and total > 400:
	    print("Total es menor que 500 pero mayor que 400")
	elif total < 500 and total > 300:
	    print("Total entre 300 y 500")
	else:
	    print("Total entre 100 y 300")

#--------------------------------------
#	Condicional de igualdad ==
#--------------------------------------
elif total == 100:
    print("Total es 100")

else:
    print ("Total menor que 100")


#=======================================================
#	Contador mientras la condicion sea verdadera
#=======================================================

num = 0
while num < 5:
    num = num + 1
    print("Num = ", num)

num = 0

while num < 5:
    num+=1

# num += 1 Es lo mismo que num = num + 1


