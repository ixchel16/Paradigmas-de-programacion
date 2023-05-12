# ============================================================================
#                        PROGRAMACION ORIENNTADA A OBJETOS
# ============================================================================

# --------------------------------------
# Una clase para un objeto vacio
# NO está tan vacío, necesita
# la palabra pass = pasar
# -------------------------------------
class ObjetoVacio:
    pass


# ---------------------------------
#     Nada es un objeto vacio
# --------------------------------
nada = ObjetoVacio()
print(type(nada))



# =================================
#           La clase llanta
# =================================
class Llanta:
    # ---------------------------------------
    # Variable que cuenta es de toda la clase
    # ---------------------------------------
    cuenta = 0
    # ---------------------------------------------
    #   Funciom constructora es de toda la clase
    #   _init_ es una funcion reservada
    #   comienza en uno mismo: self
    #   pero puede ser otro nombre (mi)
    #   parámaetros de entrada = default
    # ---------------------------------------------
    def __init__(mi, radio = 50, ancho = 30, presión = 1.5):
        # variable de la estructura completa Llanta
        Llanta.cuenta += 1
        # variables exclusivas de cada objeto
        mi.radio = radio
        mi.ancho = ancho
        mi.presión = presión


# ============================
#    Objetos (instanciados)
# ============================

llanta1 = Llanta(50, 30, 1.5)
llanta2 = Llanta(presión = 1.2)
llanta3 = Llanta()
llanta4 = Llanta(40, 30, 1.6)


# ------------------------------------------
#     Objetos que contienen otros objetos
# ------------------------------------------
class Coche:
    def __init__(mi, ll1, ll2, ll3, ll4):
        mi.llanta1 = ll1
        mi.llantta2 = ll2
        mi.llanta3 = ll3
        mi.llanta4 = ll4

micoche = Coche(llanta1, llanta2, llanta3, llanta4)

print("Total de llantas: ", Llanta.cuenta) #Variable local de la clase
print("Presión de la llanta 4 = ", llanta4.presión)  #presion de la llanta4
print("Radio de la llanta 4= " , llanta4.radio)
print("Radoio de la llanra de 3 = ", llanta3.radio)
print("Presion de la llanta 1 de mi coche", micoche.llanta1.presión)



# =======================================
#               Encapsulamiento
# =======================================

# ---------------------------------------------------------------------
#   Uso de la cuncion de python property para poner y obtener atributos
# ---------------------------------------------------------------------

class Estudiante:
    def __init__(mi):
        mi._nombre = ''
    def ponerme_nombre(mi, nombre):
        print('Se llamó a ponerme nombre')
        mi._nombre = nombre
    def obtener_nombre(mi):
        print('Se llamó a obtener_nombre')
        return mi._nombre
    nombre = property(obtener_nombre, ponerme_nombre)


# --------------------------------------
#   Crear objeto estudiante sin nombre
# --------------------------------------
estudiante = Estudiante()


# ---------------------------------------------------------------------------
#   Ponerle nombre usando la propiedad de nombre y el metodo ponerme_nombre
#   (Sin tener que llamar explicitamente a la función obtener_nombre)
# ---------------------------------------------------------------------------
estudiante.nombre = "Diego"


# ----------------------------------------------------------------
# Obtener el nombre con el método obtener_nombre
# _nombre es una variable encapsulada (no visible desde fuera)
# (Sin tener que llamar explicitamente a la función obtener_nombre)
# -----------------------------------------------------------------
print(estudiante.nombre)


# Esto no funciona
# print(estudiante._nombre)


# ==============================================
#               Herencia de clases
# ==============================================

class Cuadrilatero:
    def __init__(mi, a, b, c, d):
        mi.lado1 = a
        mi.lado2 = b
        mi.lado3 = c
        mi.lado4 = d

    def perimetro(mi):
        p = mi.lado1 + mi.lado2 +  mi.lado3 + mi.lado4
        print("Perimetro = ", p)
        return p
# --------------------------------------
#   Su hijo rectángulo
#   Rectángulo es hijo de Cuadrilátero
#   Rectángulo(cuadrilatero)
# -------------------------------------

class Rectangulo(Cuadrilatero):
    def __init__ (self, a, b):
        # -------------------------
        #  Constructor de su madre
        # --------------------------
        super().__init__(a, b, a, b)

# ------------------------
#   Su nieto Cuadradp
#   HIjo de Rectangulo
# -----------------------
class Cuadrado(Rectangulo):
    def __init__(self, a):
        super().__init__(a,a)

    def area(self):
        area = self.lado1**2
        return area

    # self perimetro (self):
    # p = 4.0 * Self.lado1
    # print("Perimetro =", p)
    # return p

# ----------------------
#   Crear un cuadrado 
# ----------------------
cuadrado1 = Cuadrado(5)


# -------------------------------------------------------
#   Llamar al método perímetro de su abuelo Cuadrilátero
# ------------------------------------------------------
perimetro1 = cuadrado1.perimetro()


# --------------------------------
# Llamar a su propio método área
# -------------------------------
area1 = cuadrado1.area()

print("Perimetro = ", perimetro1)
print("Area = ", area1)

# ==================================================================
# SObre escribir un método de su madre o abuela o tatarabuela ...
# Es volver a definir una función ya existente
# ===================================================================



# ============================================================================
#                           PARTE DOS LABORATORIO 4
# ============================================================================


# ---------------------------------------
#  La clase A tiene tres números reales
# ---------------------------------------
class A:
    _a: float = 0.0
    _b: float = 0.0
    _c: float = 0.0

    def __init__(self, a:float, b:float, c:float):
        self.a = a
        self.b = b
        self.c = c

# -----------------------------------------
#   La clase B tiene dos números reales
# ----------------------------------------
class B:
    _d: float = 0.0
    _e: float = 0.0

    def __init__(self, d:float, e:float):
        self.d = d
        self.e = e

    # ---------------------------------------
    # Método sumar todo (internos + externos)
    # ---------------------------------------
    def sumar_todo(self, aa:float, bb:float):
        x: float = self.d + self.e + aa + bb
        return x


# =================================
#           ASOCIACIÓN 
# =================================

# Usando objetos independientes
objetoA = A(1.0, 2.0, 3.0)
objetoB = B(4.0, 5.0)

print(objetoB.sumar_todo(objetoA.a, objetoA.b))

# --------------------------------------------
# EL objeto C tiene dos reales y un objeto A
# El objeto A se instancia dentro de C
# --------------------------------------------

class C:
    _d: float = 0.0
    _e: float = 0.0
    _Aa: A = None

    def __init__(self, d:float, e:float):
        self.d = d
        self.e = e
        # A está instanciado adentro
        self.Aa = A(1.0, 2.0, 3.0)

    def sumar_todo(self):
        x: float = self.d + self.e + self.Aa.a + self.Aa.b
        return x


# ================================
#           COMPOSICIÓN
#   Contiene otro objeto dentro
# ================================
objetoC = C(4.0, 5.0)
print(objetoC.sumar_todo())


# ------------------------------------------------
#	Objeto D tiene dos reales un objeto A
#	Definido por fuera
# ------------------------------------------------
class D:
    __d: float = 0.0
    __e: float = 0.0
    __Aa: A = None

    def __init__(self, d:float, e:float, Aa:A):
        self.d = d
        self.e = e
        self.Aa= Aa

    def sumar_todo(self):
        x: float = self.d + self.e + self.Aa.a + self.Aa.b
        return x


# ==========================================
#                AGREGACIÓN
#    Construye el objeto agregado por fuera
# ==========================================
objetoD = D(4.0, 5.0, objetoA)
print(objetoD.sumar_todo())
