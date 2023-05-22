from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario


# ------------------------------------
# s3 es hijo de RepositorioDeUsuarios
# ------------------------------------
class S3(RepositorioDeUsuarios):
    __clienteId: str
    __secretKey: str
    __bucket: str

    def __init__(mi, clienteId: str, secretkey: str, bucket: str):
        __clienteId: str
        __secretKey: str
        __bucket: str

    def __init__(.i, clienteId: str, secretKey: str, bucket: str):
        mi.__clienteId = clienteId
        mi.__secretKey = secretKey
        mi.__bucket = bucket

    def abrir(mi) -> None:
        print(f"Estableciendo conexion a AWS S3 {mi.__clienteId}:{mi.__secretKey}")

    def guardar(mi, usuario:Usuario) -> None:
        userData = {"nombre": usuario.getNombre(),
                 "apellido": usuario.getApellido(),
                 "edad": usuario.getEdad() }
        print(f"Guardando usuario de la bandeja: {mi.__buket}: {userData}")

    def cerrar(mi) -> None:
        print("Cerrando conexión AWS S3")

