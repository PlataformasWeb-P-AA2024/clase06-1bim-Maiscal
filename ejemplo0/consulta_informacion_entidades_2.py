"""
    Consulta de información en las entidades en la base de datos
"""

from base_datos import conn

# se usa el objeto Connection y se accede al método cursor
# para poder realizar las acciones en la base de datos.

cursor = conn.cursor()

# a través de cursor su puede ejecutar comandos SQL mediante el método
# execute



# hace consultas a la base de datos
cadena_consulta_sql = "SELECT * from Autor"
cursor.execute(cadena_consulta_sql)
# la información resultante se la obtiene del método fetchall de cursor.
informacion = cursor.fetchall()
#print(informacion)
# se realiza un ciclo repetitivo para recorrer la secuencia de información
# resultante
for d in informacion:
    #Bueno al ingresar el print estamos cogiendo la posicion, consultando desde la base de datos, es decir tomar la posicion 0 y
    #la posicion 3 que en este caso es Nombre y edad, para luego darle formateo al print  al utilizar d[0] estamos llamando al listado de la informacion en esa posicion.
    print("El nombre es: %s y la edad: es %d" %(d[0], d[3]))
#    print("%s - %s - %s - %d" % (d[0], d[1], d[2], d[3]))


# cerrar el enlace a la base de datos (recomendado)
cursor.close()
