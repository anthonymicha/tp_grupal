from flask import Flask
from flask import jsonify
import sqlite3

conexion = sqlite3.connect('/Users/anthonymicha/Desktop/tp_grupal/kissaten.db')
cursor = conexion.cursor()
sentencia = "SELECT * FROM pedidos"
cursor.execute(sentencia)
datos = cursor.fetchall()
conexion.close()


app = Flask(__name__)

@app.route("/ventas", methods=["GET"])

def kissaten():
   return jsonify({"ventas_kissaten": datos})

if __name__ == '__main__':
   app.run(debug=True,port=5000)