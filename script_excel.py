'''
#Corra el codigo y c
#Conecte con el sql
#Lo transforme en un excel
'''
import sqlite3
from io import open
import csv

conn = sqlite3.connect('/Users/anthonymicha/Desktop/tp_grupal/kissaten.db')
c = conn.cursor()
#cargar_pedido()
c.execute(f"SELECT * FROM pedidos ")
pedidos = c.fetchall()
#print(pedidos)


while True:
    try:
        archivo_name = input('\nInserte nombre del archivo: ').strip()
        if archivo_name.isalnum() == True:
            with open(f'/Users/anthonymicha/Desktop/tp_grupal/{archivo_name}.csv', 'w', newline='') as archivo_pedidos:
                writer = csv.writer(archivo_pedidos)
                writer.writerows(pedidos)
                break
        else:
            raise Exception
    except:
        print(f'{archivo_name}: Nombre invalido')
        print('Procure ingresar valores alfanumericos unicamente')


