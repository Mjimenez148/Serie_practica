import mysql.connector

mydb = mysql.connector.connect(
    
    host="localhost",
    user="root",
    password="Monicale200478@",
    database="practico",
    port="3306"
)

cursor = mydb.cursor()
ide =input("ingrese un numero")
descripcion = input("ingrese descripcion de la tarea")
fecha = input("ingrese fecha actual: Año, Mes, Dia")
completar = int(input("indique si ya esta completa,  Si = 1, No = 2"))

datos = []
datos.insert(0,ide)
datos.insert(1,descripcion)
datos.insert(2,fecha)
datos.insert(3,completar)
consulta = "insert into tareas(ID, Descripcion, `Fecha de creacion`, completada) VALUES(%s,%s,%s,%s)"
cursor.execute(consulta,datos)
mydb.commit()
cursor.close()
mydb.close
