{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b076c698-7e70-42ac-95e8-8d8b7d2ec1f8",
   "metadata": {},
   "outputs": [],
   "source": [
    "from mpi4py import MPI\n",
    "\n",
    "# ==============\n",
    "# Objeto mensaje\n",
    "# ==============\n",
    "class Mensaje:\n",
    "    def __init__(self, rank):\n",
    "        # iterador\n",
    "        self.x = range(rank*10)\n",
    "        # stting\n",
    "        self.p = \"Vengo del proceso \" + str(rank)\n",
    "        \n",
    "# ===================\n",
    "# Programa principal\n",
    "# ===================\n",
    "if __name__ == \"__main__\":\n",
    "    comm = MPI.COMM_WORLD\n",
    "    size = comm.Get_size()\n",
    "    rank = comm.Get_rank()\n",
    "    \n",
    "    s = Mensaje(rank)\n",
    "    #print(s.x)\n",
    "    \n",
    "    # --------------------------------------------------------\n",
    "    # Que te mande el anterior y si es cero que sea el último\n",
    "    # ---------------------------------------------------------\n",
    "    fuente = rank-1 if rank != 0 else size-1\n",
    "    \n",
    "    # ------------------------------------------------------------\n",
    "    # Mándalo al siguiente y si eres el ultimo mandalo al primero\n",
    "    # ------------------------------------------------------------\n",
    "    destino = rank + 1 if rank != size - 1 else 0\n",
    "    \n",
    "    # ---------------------------------------------------------\n",
    "    # send y recv son operaciones bloqueadas y generan que el \n",
    "    # código se atore esperando que alguien reciba un mensaje\n",
    "    # esto se resuelve enviando con los pares y recibiendo con\n",
    "    # los impares\n",
    "    # ---------------------------------------------------------\n",
    "    \n",
    "    \n",
    "    # Si soy par\n",
    "    if rank%2 == 0:\n",
    "        # --------------------------\n",
    "        #  Enviar mensajes al dest\n",
    "        # --------------------------\n",
    "        comm.send(s, dest=destino)\n",
    "        \n",
    "        # =================================\n",
    "        # Recibir de source y lo pone en m\n",
    "        # =================================\n",
    "        m = comm.recv(source = fuente)\n",
    "        \n",
    "    \n",
    "    # Si no soy par\n",
    "    else:\n",
    "        # -----------------------------------------\n",
    "        # Recibir primero y mandar mensaje después\n",
    "        # -----------------------------------------\n",
    "        m = comm.recv(source = fuente)\n",
    "        comm.send(s, dest = destino)\n",
    "        \n",
    "    print(\"Soy el proceso \", rank, \"El resultado es: \", len(m,x), \",\", m.p)\n",
    "        \n",
    "    \n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "769e8671-2bc9-43fa-83dc-e0dbd50629ba",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9729e894-e2b6-467c-9c22-0589e48eae97",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}