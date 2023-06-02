# =======================================
#   	Recursividad y memorizacion
# =======================================

# ==================================
#    Herramienta para memorización
# ==================================
from functools import lru_cache

def fibonacci_lento(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n>2:
        return fibonacci_lento(n-1) + fibonacci_lento(n-2)

for i in range(1,36):
    print(str(i) + ":", fibonacci_lento(i))


# =========================================================
#   Optimzación 2: uso de conjuntos para gurardar valores
# ========================================================

# -----------------------
#  Conjunto de fibonaccis 
# -----------------------
fibonaccis = {}
def fibonacci(n):
    
    # --------------------------------------
    # Revisa si ya existe y regresa el valor
    # --------------------------------------
    if n in fibonaccis:
        return fibonaccis[n]

    if n == 1:
        valor = 1
    elif n == 2:
        valor = 1
    elif n > 2:
        valor = fibonacci(n-1) + fibonacci(n-2)

    # ------------
    #   Guardalo
    # ------------
    fibonaccis[n] = valor
    return valor

for i in range(1, 10001):
    print(str(i) + ":", fibonacci(i))

# ------------------------------------
#  Uso de decoradores pra memorizacion 
#  maxsizw: es cuentas anteriores guarde
# ---------------------------------------
@lru_cache(maxsize = 3)
def nfibonacci(n):
    if type(n) != int:
        raise TypeError("n debe ser entero positivo")
    if n<1:
        raise ValueError("n debe ser entero positivo")

    if n == 1:
        return 1

    elif  n == 2:
        return 1
    
    elif n > 2:
        return nfibonacci(n-1) + nfibonacci(n-2)

for i in range(1, 10001):
    print(str(i)+ ":", nfibonacci(i))



