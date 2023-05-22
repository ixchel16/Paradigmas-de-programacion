from aplicaciones.modelos.usuario import Usuario
from aplicaciones.repositorio.repositoriodeusuarios import RepositorioDeUsuarios

# =============================
# 	Clase storemanager
#     NO TIENE VARIABLES !!!
# ==============================
class ManejoDeInscripciones:
    # --------------------------------------------------------------
    # Decorador staticmethod
    # el objeto sólo tiene la dunion inscribirUsuario
    # ENVUELVE LA FUNCION SIN LLAMAR VARIABLES LOCALES
    # el objeto ManejoDeInscripciones es la interface intercambiable
    # --------------------------------------------------------------
    @staticmethod
    def inscribirUsuario(usuario: Usuario, repositorioDeUsuarios: RepositorioDeUsuarios) -> None:
        print("--------> Guardando usuario ... \n")
        repositorioDeUsuario.abrir()
        repositorioDeUsuario.guardar(usuario)
        repositorioDeUsuario.cerrar()

