# =================
#  Uso de filtros
# =================

# -------------------------------------------------------
# Hacer una lista de los numeros por arriba del promedio 
# -------------------------------------------------------

# Modulo de estadística
import statistics

bigdata = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
promedio = statistics.mean(bigdata)
print(promedio)


# --------------------------------------------------------------
# Hzme un alista de elementos que cumplan la condicion x > promedio
# filter(condicion, datos)
# -------------------------------------------------------------
print(list(filter(lambda x: x > promedio, bigdata)))

# -----------------------
#  Limpiar los datos
# ----------------------
paises = ["", "Argentina", "", "Brasil", "", "Chile" "",  "México","",  "colombia", "", "", "Cuba", "Venezuela"]

# ------------------------------
# Filtra lo que no contiene nada
# ------------------------------
print(list(filter(None, paises)))


