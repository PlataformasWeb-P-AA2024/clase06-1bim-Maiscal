from sqlalchemy.orm import sessionmaker

from crear_base import Saludo
from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()

# se crea un objeto de tipo
# Saludo

miSaludo = Saludo()
miSaludo.mensaje = "Hola que tal"
miSaludo.tipo = "informal"

#Utilizando El ORM de sqlAlchemy se puede ahorra el codigo de sql tradicional, utilizando el insert, gracias a SQLaLCHEMY
#se puede agilizar esto y tambien utilizando un csv tambien al igual que en otras este ORM ayuda un monton.

miSaludo2 = Saludo()
miSaludo2.mensaje = "Buenas tardes"
miSaludo2.tipo = "formal"


# se agrega el objeto miSaludo
# a la entidad Saludo a la sesión
# a la espera de un commit
# para agregar un registro a la base de
# datos demobase.db
session.add(miSaludo)
session.add(miSaludo2)

# se confirma las transacciones
session.commit()
