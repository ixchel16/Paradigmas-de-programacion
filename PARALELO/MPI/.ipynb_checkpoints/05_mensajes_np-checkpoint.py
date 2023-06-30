# ---------------------------------------------
# Uso de MPI optimizado para cálculos numéricos
# ----------------------------------------------
from mpi4py import MPI
import numpy as np

class Mensaje:
    def __init__(self, rank):
        # -----------------------------
        # Arreglo de numpy (optimizado)
        # -----------------------------
        self.x = np.array([float(x+rank) for x in range(10)])
        self.p = "Vengo del proceso " + str(rank)
        
# ========================
#    PROGRAMA PRINCIPAL
# ========================
if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()
    
    s = Mensaje(rank)
    src = rank-1 if rank != 0 else size-1
    dst = rank+1 if rank != size-1 else 0
    
    # --------------------
    # Arreglo para enviar 
    # --------------------
    m = s.x
    
    #print(m)
    
    # -----------------------------------
    # Isend Irecv son para comuniacion
    # No bloqueante en arreglos de npmpy
    # -----------------------------------
    comm.Isend(m, dest = dst)
    
    # -----------------------------------
    # Arreglo vacío para recibir
    # con dimension 10 y tipo de datos
    # float64 (doble precisión)
    # ------------------------------------
    a = np.zeros(10, dtype = np.float64)
    req = comm.Irecv(a, source = src)
    req.Wait()
    
    print("Soy el proceso ", rank, ", el resultado es ", a)