import mysql.connector
from mysql.connector import Error

def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="parcial-tendencias"
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
        return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

class Cliente:
    def __init__(self, id, nombre, apellido, email, telefono, direccion):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.direccion = direccion

class Factura:
    def __init__(self, factura_id, pedido_id, fecha_factura, total):
        self.factura_id = factura_id
        self.pedido_id = pedido_id
        self.fecha_factura = fecha_factura
        self.total = total

def insertar_cliente():
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        try:
            nombre = input("Ingrese el nombre del cliente: ")
            apellido = input("Ingrese el apellido del cliente: ")
            email = input("Ingrese el email del cliente: ")
            telefono = input("Ingrese el teléfono del cliente: ")
            direccion = input("Ingrese la dirección del cliente: ")
            
            cursor.execute("""
                INSERT INTO clientes (nombre, apellido, email, telefono, direccion) 
                VALUES (%s, %s, %s, %s, %s)
            """, (nombre, apellido, email, telefono, direccion))
            
            connection.commit()
            print("Cliente insertado correctamente")
        except Error as e:
            print(f"Error al insertar cliente: {e}")
        finally:
            cursor.close()
            connection.close()

def insertar_factura():
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        try:
            pedido_id = input("Ingrese el ID del pedido: ")
            fecha_factura = input("Ingrese la fecha de la factura (YYYY-MM-DD): ")
            total = input("Ingrese el total de la factura: ")
            
            cursor.execute("""
                INSERT INTO facturas (pedido_id, fecha_factura, total) 
                VALUES (%s, %s, %s)
            """, (pedido_id, fecha_factura, total))
            
            connection.commit()
            print("Factura insertada correctamente")
        except Error as e:
            print(f"Error al insertar factura: {e}")
        finally:
            cursor.close()
            connection.close()

def leer_datos(tabla):
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute(f"SELECT * FROM {tabla}")
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
        except Error as e:
            print(f"Error al leer datos de {tabla}: {e}")
        finally:
            cursor.close()
            connection.close()

def leer_todos_los_datos():
    print("Clientes:")
    leer_datos("clientes")
    print("\nFacturas:")
    leer_datos("facturas")

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Insertar Cliente")
        print("2. Insertar Factura")
        print("3. Ver Clientes")
        print("4. Ver Facturas")
        print("5. Ver Todos los Datos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            insertar_cliente()
        elif opcion == "2":
            insertar_factura()
        elif opcion == "3":
            leer_datos("clientes")
        elif opcion == "4":
            leer_datos("facturas")
        elif opcion == "5":
            leer_todos_los_datos()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
