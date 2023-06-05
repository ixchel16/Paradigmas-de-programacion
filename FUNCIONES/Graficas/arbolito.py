# ==================================================
#   Gráfico usando la tortuga que pinta al caminar
# ==================================================
import turtle
tortuga = turtle.Turtle()
tortuga.left(90)           # Giro a la izquierda de 90 grados
tortuga.speed(500)         # velocidad de la tortuga


# ------------------------------------
#    Con ángulos de 90 es un árbol H
# ------------------------------------
angulo:float = 90


# ===========================================
#   El arbol se construye con recursividad
# ==========================================
def arbol(i:float, angulo:float):
    if i < 10.0:
        return
    else:
        tortuga.forward(i) # camina i
        tortuga.left(angulo) # gira a la izquierda 90 grados
        arbol(3.0*i/4.25, angulo) # Pide otro arbol y cambia la longitud del paso
        tortuga.right(2*angulo) # gira a la derecha 180
        arbol(3.0*i/4.25, angulo)
        tortuga.left(angulo)
        tortuga.backward(i)


arbol(100, angulo)
turtle.done()




