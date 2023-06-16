{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9c5fa9bd-570c-40bb-8b63-d09987479690",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Saludos desde el proceso 0 de  1\n"
     ]
    }
   ],
   "source": [
    "# ==================================\n",
    "# mpiexec -n 4 python3 hola_mpi.py\n",
    "# mpirun  -n 4 python3 hola_mpi.py\n",
    "# ==================================\n",
    "# Para correr en 4 procesos\n",
    "# ==================================\n",
    "from mpi4py import MPI\n",
    "\n",
    "# =============================\n",
    "# Crear un objeto comunicador\n",
    "# =============================\n",
    "comunicadores = MPI.COMM_WORLD\n",
    "\n",
    "# -------------------------\n",
    "# Numero total de procesos\n",
    "# -------------------------\n",
    "n_procesos = comunicadores.Get_size()\n",
    "\n",
    "# -------------------------------------\n",
    "# Numero identificador de este proceso\n",
    "# -------------------------------------\n",
    "quien_soy = comunicadores.Get_rank()\n",
    "\n",
    "print(\"Saludos desde el proceso\", str(quien_soy), \"de \", str(n_procesos))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "48f86085-7c52-489c-a6aa-657c858f56e4",
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
