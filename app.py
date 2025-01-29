from flask import Flask, render_template

# Crear la aplicación Flask
app = Flask(__name__)

# Ruta principal que renderiza el template
@app.route("/")
def home():
    return render_template("index.html")

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True)