from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(
        host=os.environ["DB_HOST"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASS"],
        database=os.environ["DB_NAME"],
        port=int(os.environ["DB_PORT"]),
        ssl_disabled=False
    )

@app.route("/formulario", methods=["POST"])
def formulario():
    try:
        data = request.get_json()
        nombre = data.get("nombre")
        apellido = data.get("apellido")

        conn = get_connection()
        cursor = conn.cursor()

        query = "INSERT INTO Usuarios (nombre, apellido) VALUES (%s, %s)"
        cursor.execute(query, (nombre, apellido))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({"status": "OK"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
