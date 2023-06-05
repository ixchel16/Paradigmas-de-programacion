import multiprocessing as mp
import numpy as np
import time

def my_function(i, param1, param2, param3):
    # Calcula un polinomio
    result = param1**2 + param2 + param3
    # se hace tonta 2 segundos
    time.sleep(2)
    return (i, result)

def get_result(result):
    # Se inscriben en la lista global
    # (mal estilo de programacion)
    global results
    results.append(result)


# =========================
#    Programa principal
# ========================
if __name__ == "__main__":
    
    # Matriz de 10x3 números al azar
    params = np.random.random((10,3))*100.0
    results = []
    ts = time.time()

    # Un grupo de procesos (pool)
    pool = mp.Pool(mp.cpu_count())
   
    # loop de primera dimensión del arreglo
    for i in range(0, params.shape[0]):
        # Correr asincronicamente my_fuction con argumentos args y cuando termine corriendo get_result
        pool.apply_async(my_function, args = (i, params[i, 0], params[i, 1], params[i, 2]), callback = get_result)
        
        # Cerrar el grupo
        pool.close()
  
        # esperar que termine el grupo
        pool.join()

        print("Tiempo en paralelo = ", time.time()-ts)
        print(results)
