from flask import Flask, jsonify
from flask_cors import CORS
import os
import time
# Importamos la db y los modelos desde tu nuevo models.py
from models import db, CategoriaPadre, Subcategoria, Producto 

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

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
    padres = CategoriaPadre.query.all()
    resultado = []
    for p in padres:
        resultado.append({
            "id": p.id,
            "nombre": p.nombre,
            # Aquí está el truco: mandamos el ID y el nombre de cada hijo
            "subcategorias": [
                {"id": s.id, "nombre": s.nombre} for s in p.subcategorias
            ]
        })
    return jsonify(resultado)
    
# --- RUTAS PARA PRODUCTOS ---

# --- RUTA PARA TRAER PRODUCTOS DE UNA SECCIÓN ---
@app.route('/api/subcategoria/<int:id>/productos', methods=['GET'])
def get_productos_por_sub(id):
    """
    Busca en la bodega (DB) todos los productos que tengan el ID de la subcategoría que le pedimos.
    """
    # Buscamos los productos filtrando por el ID de la subcategoría
    productos = Producto.query.filter_by(subcategoria_id=id).all()
    
    # Armamos la lista para enviársela a Angular
    resultado = []
    for p in productos:
        resultado.append({
            "id": p.id,
            "nombre": p.nombre,
            "precio": float(p.precio), # Ponle float porque si no el JSON se apendeja
            "imagen": p.imagen,
            "condicion": p.condicion
        })
    
    return jsonify(resultado)

@app.route('/api/producto/<int:id>', methods=['GET'])
def get_detalle_producto(id):
    """
    Obtiene la información detallada de un solo producto usando su ID único.
    """
    # Buscamos el producto por su ID o mandamos un error 404 si no existe
    p = Producto.query.get_or_404(id)
    
    return jsonify({
        "id": p.id,
        "nombre": p.nombre,
        "descripcion": p.descripcion,
        "precio": float(p.precio),
        "imagen": p.imagen,
        "condicion": "Seminuevo", # Dato estático por ahora
        "stock": 1 # Cantidad disponible
    })

def seed_data():
    if CategoriaPadre.query.first() is None:
        print("Iniciando carga de datos maestros...")
        
        menu_raiport = {
            "HOMBRE": ["Camisetas", "Camisas", "Sacos", "Chalecos", "Chamarras Zip", 
                       "Hoodies", "Suéteres", "Pantalones", "Jeans", "Shorts", "Sombreros", "Accesorios"],
            "MUJER": ["Camisetas", "Camisas", "Sacos", "Chalecos", "Chamarras Zip", 
                      "Hoodies", "Suéteres", "Pantalones", "Jeans", "Shorts", "Sombreros", "Accesorios"],
            "BOLSAS": ["Gym", "Totes", "Cangureras", "Mochilas"],
            "JOYERIA": ["Anillos", "Cadenas", "Brazaletes", "Relojes", "Aretes"]
        }

        for nombre_padre, hijos in menu_raiport.items():
            padre = CategoriaPadre(nombre=nombre_padre)
            db.session.add(padre)
            db.session.flush() 

            for nombre_hijo in hijos:
                hijo = Subcategoria(nombre=nombre_hijo, categoria_padre_id=padre.id)
                db.session.add(hijo)
        
        # Guardamos todo lo anterior para que existan los IDs de las subcategorías
        db.session.commit()

        # --- AQUÍ EMPIEZA LA CARGA DE PRODUCTOS DE PRUEBA ---
        print("Metiendo mercancía a la bodega...")

        # Buscamos la subcategoría de "Camisetas" que acabamos de crear para HOMBRE
        # Usamos el nombre y el ID del padre HOMBRE (que suele ser el 1 si es DB nueva)
        sub_camisetas = Subcategoria.query.filter_by(nombre='Camisetas').first()

        if sub_camisetas:
            prod1 = Producto(
                nombre="Camiseta Raiport Vintage",
                descripcion="Una joya de algodón peinado, ideal para el diario. Corte slim fit.",
                precio=550.00,
                imagen="https://picsum.photos/400/500", # Imagen de relleno perrona
                condicion="Seminuevo",
                subcategoria_id=sub_camisetas.id
            )
            
            prod2 = Producto(
                nombre="Camiseta Oversize Negra",
                descripcion="Estilo urbano, usada un par de veces pero como nueva.",
                precio=420.00,
                imagen="https://picsum.photos/400/501",
                condicion="Usado",
                subcategoria_id=sub_camisetas.id
            )
            
            db.session.add_all([prod1, prod2])
            db.session.commit()
            print("¡Productos cargados exitosamente!")

        print("¡Todo listo en RAIPORT CLUB!")

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