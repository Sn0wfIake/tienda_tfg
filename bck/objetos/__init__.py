from Objetos import *
from conector import *

db = database()
st = crudusuarios()
sta = crudcatalogo()
y = True
usuario1 = Usuarios(1, "copi", "mateo","alexmatemese", "1234", "no")
#usuario1.__init__("1", "alex", "mateo","alexmatemese", "1234", "no")
prenda1 = Catalogo("1","20","pantalon","techwear","verde","5","foto")
pago1 = Transacciones("1","1","2","5",y,"enviado")
print(sta.listarcatalogo())
print(usuario1)
print(prenda1)
print(pago1)
#Insercion
#st.insertausu((usuario1.nombre, usuario1.apellidos, usuario1.correo, usuario1.passwd, usuario1.preferencias))

#listado de todos
print(st.listausuarios())

#lista por id
print(st.buscaid(1))
#borrado
#st.delete(4)
print("meto los usuarios")
usurecoge = st.listausuarios()
#actualizar
#st.update(6, (usuario1.nombre, usuario1.apellidos, usuario1.correo, usuario1.passwd, usuario1.preferencias))
print(usurecoge)
