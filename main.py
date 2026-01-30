from dotenv import load_dotenv
import os
import csv
import mysql.connector
from pathlib import Path

load_dotenv()

host = os.getenv("DB_HOST")
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_DATABASE")

archivo = Path(__file__).parent.parent / "productos.csv"


def limpiezaDatos(archivo):
    lista_limpia = []

    try:
        with archivo.open("r", encoding="utf-8-sig") as file:
            contenido = csv.DictReader(file)

            for fila in contenido:
                try:
                    id_producto = fila["id_producto"]
                    nombre = fila["nombre"].title()
                    categoria = fila["categoria"].title()
                    precio_unitario = float(fila["precio_unitario"].replace("$", ""))
                    stock = int(fila["stock"])

                    lista_limpia.append({
                        "id_producto": id_producto,
                        "nombre": nombre,
                        "categoria": categoria,
                        "precio_unitario": precio_unitario,
                        "stock": stock
                    })

                except Exception as e:
                    print("Error procesando fila:", e)

        return lista_limpia

    except Exception as e:
        print("Error leyendo el archivo:", e)


def insercion(host, username, password, database, resultado):
    cnx = None
    sentencia_insert = "INSERT INTO productos (id_producto, nombre, categoria, precio_unitario, stock) VALUES (%s, %s, %s, %s, %s)"

    try:
        cnx = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )

        cursor = cnx.cursor()

        for fila in resultado:
            cursor.execute(
                sentencia_insert,
                (
                    fila["id_producto"],
                    fila["nombre"],
                    fila["categoria"],
                    fila["precio_unitario"],
                    fila["stock"]
                )
            )

        cnx.commit()
        cursor.close()

    except Exception as e:
        print("Error al insertar datos:", e)

    finally:
        if cnx and cnx.is_connected():
            cnx.close()


resultado = limpiezaDatos(archivo)
insercion(host, username, password, database, resultado)
