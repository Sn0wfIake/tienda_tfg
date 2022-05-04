############################################CLASE USUARIOS###############################################
class Usuarios:

    id_usuario = ""
    nombre = ""
    apellidos = ""
    correo = ""
    passwd = ""
    preferencias = ""

    def __init__(self, id_usuario, nombre, apellidos, correo, passwd, preferencias):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo = correo
        self.passwd = passwd
        self.preferencias = preferencias

#getters y setters
def set_usuario(id_usuario):
    self.id_usuario = id_usuario


def getid_usuario (id_usuario):
    return Usuarios.id_usuario


def set_nombre(nombre):
    self.nombre = nombre


def get_nombre(nombre):
    return Usuarios.nombre


def set_apellidos(apellidos):
    self.apellidos = apellidos


def get_apellidos(apellidos):
    return Usuarios.apellidos


def set_correo(correo):
    self.correo = correo


def get_correo(correo):
    return Usuarios.correo


def set_passwd(passwd):
    self.passwd = passwd


def get_passwd(passwd):
    return Usuarios.passwd

def set_preferencias(preferencias):
    self.preferencias = preferencias


def get_preferencias(preferencias):
    return Usuarios.preferencias

def toString(self):
    return self.id_usuario +","+ self.nombre +","+ self.apellidos +","+ self.correo +","+ self.passwd +","+ self.preferencias
    print(self.id_usuario + self.nombre + self.apellidos+ self.correo+ self.passwd + self.preferencias)

############################################CLASE CATALOGO###############################################


class Catalogo:
    id_prenda = ""
    stock = ""
    tipo_prenda = ""
    estilo = ""
    color = ""
    precio = ""
    foto = ""
    def __init__(self, id_prenda, stock, tipo_prenda, estilo, color, precio, foto):
        self.id_prenda = id_prenda
        self.stock = stock
        self.tipo_prenda = tipo_prenda
        self.correo = correo
        self.estilo = estilo
        self.color = color
        self.precio = precio
        self.foto = foto
    # getters y setters


def set_prenda(id_prenda):
    self.id_prenda = id_prenda


def getid_prenda(id_prenda):
    return Catalogo.id_prenda


def set_stock(stock):
    self.stock = stock


def get_stock(stock):
    return Catalogo.stock


def set_tipo_prenda(tipo_prenda):
    self.tipo_prenda = tipo_prenda


def get_tipo_prenda(tipo_prenda):
    return Catalogo.tipo_prenda


def set_correo(estilo):
    self.estilo = estilo


def get_estilo(estilo):
    return Catalogo.estilo


def set_passwd(color):
    self.color = color


def get_color(color):
    return Catalogo.color


def set_precio(precio):
    self.precio = precio


def get_precio(precio):
    return Catalogo.precio

def set_precio(precio):
    self.precio = precio


def get_foto(foto):
    return Catalogo.foto

############################################CLASE TRANSACCIONES###############################################


class Transacciones:
    id_transaccion = ""
    id_usuario = ""
    id_prenda = ""
    precio = ""
    pago = ""
    estado = ""

    def __init__(self, id_transaccion, id_usuario, id_prenda, precio, pago, estado):
        self.id_transaccion = id_transaccion
        self.id_usuario = id_usuario
        self.id_prenda = id_prenda
        self.precio = precio
        self.pago = pago
        self.estado = estado

    # getters y setters


def set_id_transaccion(id_transaccion):
    self.id_transaccion = id_transaccion


def getid_transaccion(id_transaccion):
    return Transacciones.id_transaccion


def set_id_usuario(id_usuario):
    self.id_usuario = id_usuario


def get_id_usuario(id_usuario):
    return Transacciones.id_usuario


def set_id_prenda(id_prenda):
    self.id_prenda = id_prenda


def get_id_prenda(id_prenda):
    return Transacciones.id_prenda

def set_precio(precio):
    self.precio = precio


def get_precio(precio):
    return Transacciones.precio


def set_pago(pago):
    self.pago = pago


def get_pago(pago):
    return Transacciones.pago
#########ESTADO##########
def set_estado(estado):
    self.estado = estado


def get_estado(estado):
    return Transacciones.estado