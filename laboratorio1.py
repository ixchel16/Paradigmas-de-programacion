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

lista = [1, 2, 3, 4, 
        5, 6, 7, 8, 
        9, 10, 11, 12]

matriz = [[1,2,3,4], [5,6,7,8], [9, 10, 11, 12]]

print (lista)
print (matriz)


#================================================================
# Identación estricta para procesos dependientes de: (dos puntos) con dos puntos misma identacion
#================================================================
if 10>5:
    print ("diez es mayor que cinco")
    print ("otra identación")

for i in lista:
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



# ==========================================================
#		CONJUNTO DE python
# ==========================================================

even_nums = {2, 4, 6, 8, 10}	# Conjunto de número pares
print(even_nums)

# El bool no es parte del conjunto 
emp = {1, 'Steve', 10.5, True}  # El conjunto de diferentes objetos
print(emp)

nums = {1, 2, 2, 3, 4, 4, 5, 5}
print(nums)


# -------------------------------------
# Convertir secuencia a un conjunto
# NO lo genera en orden
# -------------------d = {1:'One', 2: 'Two'}
s = set('Hello')
print(s)
s = set((1,2,3,4,5)) # tupla a conjunto
print(s)

s.add(100)
print(s)  # Imprime (1, 2, 100)

s.remove(100)
print(s)

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

su = s1|s2   # UNION
print(su)

s = set('Hello')
print(s)
s = set((1, 2, 3, 4, 5))  # tupla a conjunto 
print(s)


# =============================================
# De diccionario a conjunto : Conjunto de llaves
# ==============================================

d = {1:'One', 2: 'Two'}
s = set(d)
print(s)    # Imprime (1, 2)

s.add(100)
print(s)    # Imprime (1, 2, 100)

s.remove(100)
print(s)    # Imprime (1, 2)

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

su = s1|s2   # UNION
print(su)

si = s1&s2    # INTERSECCION
print(si)

sr = s1-s2    # Diferencia de conjuntos
print(sr)

sp = s2 - s1 
print(sp)

ss = s1^s2      # Diferencia simétrica
print(ss)


# =================================================
# 		USO DE DICCIONARIOS
# =================================================
capitals = {"USA": "Washingto D.C", "France": "Paris", "India": "New Delhi"}
print(capitals)


# ------------------------
#	Llave : valor
# ------------------------

# Diccionario vacío
d = {}

# Llave entera, valor string
numNames={1: "One", 2: "Two", 3: "Three"}

# Lave real, valor string
decNames={1.5: "One and half", 2.5 : "Two and half", 3.5: "Three and half"}

#Llave tupla, valor string
items={("parker", "Reynolds", "Camlin"): "pen", ("LG", "Wirlpool", "Samsung"): "Refrigerator"}

# Lave string, valor int
romanNums = {'I': 1, 'II':2, 'III': 3, 'IV': 4, 'V': 5}
print(romanNums)
print(romanNums["I"])

print(capitals.get("India"))
print(capitals.get("india"))

# Reportar llave y valor 
for k in capitals:
    print("key = " + k + ", Value = " + capitals[k])

#Nuevo dato para el diccionario
capitals["Mexico"] = "CDMX"
print(capitals)

# Borrar dato del diccionario
del capitals["Mexico"]
print(capitals)


# Borrar todo el diccionario
del capitals

# Reportar llaves
print(romanNums.keys())


# Reportar valores
print(romanNums.values())

# Juicio de llave (Está o no está la llave en el diccionario)
print("I" in romanNums)
print("X" in romanNums)
print("XX" not in romanNums)


# =================================================
#			LISTAS
# =================================================

# Las listas puedes ser de objetos diferentes

miprimeralista = []   # Es una lista vacía
print(miprimeralista)

# ------------------------------------------------
# 		Llenado de lista
# ------------------------------------------------

miprimeralista = [1, "Javier", 1.34, "Bosco", "Angel", "Abigail", True]
print(miprimeralista)

# -----------------------------------------------
# list : hacer una lista
# range(i, j): Secuencia de i hasta j-1
# --------------------------------------------

nums = list(range(1,61))

for i in nums:
    print(i)


# ------------------------------------
# Incluir nuevos elementos en la lista
# ------------------------------------

nums.append(61)
nums.append(52)
nums.append(61)
print(nums)

# ------------------------------------
# Quitar elementos de la lista
# ------------------------------------

nums.remove(61)
print(nums)


# ------------------------------
# Quitar elementos con índice i
# ------------------------------

i = 61
del nums[i]
print(nums)


# --------------------------------
# BORRAR  la lista
# ---------------------------------
del nums



# -----------------------------
# Sumar listas
# ----------------------------
L1 = [1, 2, 3]
L2 = [4, 5, 6]
print(L1+L2)


# -------------------------------
# 	LLENADO A MANO
# ---------------------------------

potencial = []
for i in range(0,10000):
    potencial.append(float(i))
print(potencial[100])


# ---------------------------------------
#	Generar una tupla con la lista
# ----------------------------------------
potencial = tuple(potencial)
print(potencial[100])


#==========================================
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
	num += 1		# num += 1 Es lo mismo que num = num + 1
	print("num = ", num)
	if num == 3:
		break		# break  Condicion antes de salir del bucle


num = 0
while num < 5:
	num += 1
	if num > 3:
		continue	# Evitar lo que sigue y continuar iteracion

print("num = ", num)

# ==================================
#	 BUCLE SOBRE LISTA
# =================================

nums = [10, 20, 30, 40, 50]

for i in nums:
    print(i)


# ==================================
#        BUCLE SOBRE UN STRING
# ==================================
for char in 'Hello':
    print (char) 	# Imprime caracter por caracter


# ========================================
#        BUCLE SOBRE UN DICCIONARIO
#		items = elementos
# =========================================

numNames = {1:'One', 2: 'Two', 3: 'Three'}
for pair in numNames.items():
    print(pair)			# Imprime tipo (1, 'One')


# =====================================================================
# INICIO DE SEGUNDA PARTE DEL TERCER VIDEO
# ====================================================================

# ================================================
#            F U N C I O N E S
# ===============================================


# ------------------------------------------
#   Primera funcion
# ------------------------------------------

def saludo():
    # ---------------------------------
    # Documentacion rapida de la funcion
    # ----------------------------------
    """ Esta funcion saluda """
    print(' ¡Quiúboles!, ¿cómo estás?')

#
# Llamado de la funcion
# -----------------------
saludo()


# ---------------------------
# Se ejecuta pero no se asigna
# ----------------------------
salida = saludo()

# ----------------
# Esto no funciona
# ----------------
print(salida)


# --------------------
# Mostrar documentacion
# ----------------------
# help(saludo)


# -------------------------
#   Funcion con argumento
# -------------------------
def salu2(nombre):
    "Esta funcion te saluda por tu nombre"
    print('Que onda ese', nombre, "!")
salu2("Julian")
salu2("Ángel")


# =======================================
# ahorra el trabajo del interprete
# nombre : str ls variable nombre es un str
# ========================================
def saludos(nombre:str):
    "Esta funcion te salluda por tu nombre estrictamente"
    print("Que onda ese", nombre, "!")
saludos("Julian")
a = 123
print(type(a))
saludos(a)

# ==================================
#   Función con muchos argumentos
# =================================

def saludos_multiples(nombre1, nombre2, nombre3):
    "Esta función saluda a 3 personas al mismo tiempo"
    print("Hola", nombre1,",", nombre2, "y", nombre3)
saludos_multiples("Hugo", "Paco", "Luis")

# ===========================================
# Funcion con cualquier número de argumentos
# ===========================================

def muchos_saludos(*nombres):
    "Esta funcion saluda a todos los que quieras"
    i = 0
    # ------------------------------------
    # end= es para ponerlo de corrido
    # -----------------------------------
    print("Hola ", end="")
    while len(nombres) > i:
        # Ultimo nombre
        if (i == len(nombres)-1):
            print(nombres[i])
        else:
            # Cualquier otro nombre
            print(nombres[i], end= ", ")
        i+=1

muchos_saludos("Bosco", "Angel", "David", "Tamara", "MIli", "Edwin", "Lev", "Luis", "Abigail")

def greet(firstname, lastname):
    print("Hello", firstname, lastname)

# ------------------------------------------------
#   Llamar a la funcion con argumentos en desorden
# ------------------------------------------------
greet(lastname='Jobs', firstname='Steve') # Se puede especificar las variables en 

# --------------------------------------------------
#        Funcion con argumentos escondidos **
# --------------------------------------------------

def greet(**person):
    # ---------------------------------------------------
    #  persona tiene características firstname y lastname
    # ---------------------------------------------------
    print('Hello', person['firstname'], person['lastname'])

greet(firstname= 'Steve', lastname= 'Jobs')
greet(lastname= 'Jobs', firstname= 'Steve')
greet(firstname= 'Bill', lastname= 'Gates', age =55) #Se pueden pasar mas parametros de los necesarios

# -------------------------------------
#    Funcion con valores por defecto
# -------------------------------------
def greet(name = "Guest"):
    print('Hello', name)

greet() #se utiliza el valor dado de antemano
greet('Steve')

# ----------------------------------
#        Funcion con resultado
# ----------------------------------
def suma(a,b):
    return a + b

# ---------------------------------------
#          Programacion funcional 
#     Se pueden funciones en funciones
# ----------------------------------------
total = suma(5, suma(10,20))
print(total)


# ---------------------------------------------------
#                     Cálculo de lambda
#   nombre de la función = lambda variable : función
# ---------------------------------------------------
x_al_cuadrado = lambda x : x * x
al = x_al_cuadrado(5)
print(al)


# ------------------------------------------
#       Lambda de varias variables
# ------------------------------------------
suma = lambda x1, x2, x3: x1+x2+x3
print(suma(99,98,97))

sumas = lambda *x: x[0] + x[1] + x[2] + x[3]
print(sumas(100, 200, 300, 400))

# -----------------------------------------
#         Uso de una función anonima
#  El argumento va afuera entre parentesis
# ------------------------------------------
print((lambda x: x*x)(6)) #Función anónima


# ---------------------------------
#   Función con variable global
#        EVITE EL EXCESO !!!!
# --------------------------------
name = 'Steve'
def greet():
    global  name #para utiilizar ua variable global (que viene del bloque)
    name = 'Bill'
    print('Hello ', name)

greet()


