# ==========================================================
# Ejemplo de conunicación bloqueada a un arreglo compartido
# Uso de candados (loks)
# ===========================================================
from multiprocessing import Process, Array, Lock
import time

def sumale100(numeros, candado):
    for i in range(100):
        time.sleep(0.01)
        # Usando candado
        for i in range(len(numeros)):
            # Lo que esté dentro de con candado no puede accderse
            #desde otro proceso al mismo tiempo 
            with candado:
                #hacer la operación
                numeros[i] += 1
                
if __name__ == "__main__":
    # --------------------------------------------------
    # Candado para evitar que dos procesos se empalmen
    # --------------------------------------------------
    candado = Lock()
    
    # Numero comun a los procesos, d de dobles
    numeros_compartidos = Array("d", [0.0, 100.0, 200.0])
    
    # : quiere decir todos los elementos
    print("Al principio vale = ", numeros_compartidos[:])

    # Dos procesos
    p1 = Process(target = sumale100, args=(numeros_compartidos, candado))
    p2 = Process(target = sumale100, args=(numeros_compartidos, candado))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print("Al final vale = ", numeros_compartidos[:])