from flask import Flask, jsonify
from flask_cors import CORS
import os
import time
# Importamos la db y los modelos desde tu nuevo models.py
from models import db, CategoriaPadre, Subcategoria, Producto 

app = Flask(__name__)
CORS(app)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos con la app
db.init_app(app)

@app.route('/')
def health_check():
    return jsonify({"status": "RAIPORT API Online", "database": "Connected"})

@app.route('/api/catalogo', methods=['GET'])
def get_catalogo():
    try:
        categorias = CategoriaPadre.query.all()
        resultado = []
        for cat in categorias:
            resultado.append({
                "id": cat.id,
                "nombre": cat.nombre,
                "subcategorias": [sub.nombre for sub in cat.subcategorias]
            })
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def seed_data():
    # Solo insertamos si no hay categorías
    if CategoriaPadre.query.first() is None:
        print("Poblando base de datos inicial...")
        h = CategoriaPadre(nombre='HOMBRE')
        m = CategoriaPadre(nombre='MUJER')
        b = CategoriaPadre(nombre='BOLSAS')
        j = CategoriaPadre(nombre='JOYERIA')
        db.session.add_all([h, m, b, j])
        db.session.commit()
        print("¡Datos insertados!")

def setup_database():
    with app.app_context():
        for i in range(5):
            try:
                db.create_all()
                seed_data()
                print("¡Tablas creadas exitosamente!")
                break
            except Exception as e:
                print(f"Esperando DB... ({i+1}/5) Error: {e}")
                time.sleep(3)


if __name__ == '__main__':
    setup_database()
    app.run(host='0.0.0.0', port=5000, debug=True)