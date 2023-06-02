# ===================
#  Funcion pura x**2
# ===================
def alcuadrado(x):
    return x*x

# ===================
#  Funcion pura x**3
# ===================
def alcubo(x):
    return x*x*x

# ===========================
#  Mapeo de una función pura
# ===========================
def mapeo(func, lista_numeros):
    resultado = []

    for i in lista_numeros:
        resultado.append(func(i))
    return resultado

cuadrados = mapeo(alcuadrado, [2,5,2,3,8,1,2,6,6,1j,7,8])
cubos = mapeo(alcubo, [1, 2, 3, 4, 5, 6, 7, 8])
print(cuadrados)
print(cubos)

# ================================
#   Funciones dentro de funciones 
# ================================
def en_mayusculas(texto):
    return texto.upper()

def en_minusculas(texto):
   return texto.lower()

def saludar(func):
    saludo = func("Hola, ‚¿qué tal?")
    print(saludo)

# ===========
# Con strings
# ===========
saludar(en_mayusculas)
saludar(en_minusculas)

# ----------------------------------------
# Funciones abstractas dento de funciones 
#  su resultado es otra función
# ----------------------------------------
def divisor(x):
    def dividiendo(y):
        return y/x
    return dividiendo

# ..................................
#   Primero generamos la funcion Y2
# ----------------------------------
división = divisor(2)

# ----------------------------------
# Primero generamos la funcion y/2
# ---------------------------------
división = divisor(2)

# --------------------------------
# La usamos para calcular 3/2
# -----------------------------
print(división(3))


# ------------------------------------
# Uso de la funcion map con una lista
# ------------------------------------

# -------------------------------------
# Lista de ciudaddes y su temperatura 
# -------------------------------------
temps = [("Berlín", 29), ("Cairo", 36), ("Buenos aires", 19), ("Los Angeles", 26), ("Tokyo", 27), ("Nueva York", 28), ("Londres ", 22), ("Pekín", 32), ("México Tenochtitlan", 23)]

C_a_F = lambda datos: (datos[0], (9/5)*datos[1]+32)
print(list(map(C_a_F, temps)))


