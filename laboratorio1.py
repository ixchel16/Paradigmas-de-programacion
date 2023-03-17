'''ESTE ES UN SUPERCOMENTARIO 
   DE INICIO A NUESTRO RESUMEN
'''

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

if 100 > 999 and \ # \ es para saltar la linea y seguir la misma instruccion#
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
# Identación estricta para procesos dependientes de: (dos puntos)
#================================================================
if 10>5;
    print ("diez es mayor que cinco")
    print ("otra identación")

for i in list:
        print (i)
        print("ok")

if 10>5; 
    print ("verdadero")
