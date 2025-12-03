from flask import Flask

app = Flask(__name__)

@app.route("/principio")
def home():
    return "¡Hola desde Flask desplegado en Render!"

if __name__ == "__main__":
    # Render usa el puerto que define en la variable PORT
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)