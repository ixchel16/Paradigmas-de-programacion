{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "434749db-33aa-422b-8492-ae13544d3a57",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Yo soy el proceso 0\n",
      "Reportándome, soy el proceso  0 de  1\n"
     ]
    }
   ],
   "source": [
    "# ----------------------------------\n",
    "# mpirun -n 4 python3 tareas_mpi.py\n",
    "# ---------------------------------\n",
    "from mpi4py import MPI\n",
    "\n",
    "# ========================\n",
    "# Objeto de comunicadores\n",
    "# ========================\n",
    "comm = MPI.COMM_WORLD\n",
    "\n",
    "# -----------------------\n",
    "# Cuántos somos en total\n",
    "# -----------------------\n",
    "size = comm.Get_size()\n",
    "\n",
    "# -----------------------\n",
    "# Quien soy\n",
    "# -----------------------\n",
    "rank = comm.Get_rank()\n",
    "\n",
    "# -----------------------------\n",
    "# Si yo soy el cero hago esto\n",
    "# -----------------------------\n",
    "if rank == 0:\n",
    "    print(\"Yo soy el proceso 0\")\n",
    "    \n",
    "# --------------------------------\n",
    "# Si yo soy el uno hago esto otro\n",
    "# --------------------------------\n",
    "elif rank == 1:\n",
    "    print(\"Yo soy el proceso 1\")\n",
    "    \n",
    "# --------------------------------------------\n",
    "# Si yo no soy ni el uno ni el dos hago esto\n",
    "# --------------------------------------------\n",
    "else:\n",
    "    print(\"Yo no soy ninguno de los dos primeros procesos\")\n",
    "    \n",
    "print(\"Reportándome, soy el proceso \", str(rank), \"de \", str(size))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "21d4a953-f7c3-4305-b0e0-8a457d87d7e0",
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
