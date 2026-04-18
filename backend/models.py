from flask_sqlalchemy import SQLAlchemy

# Creamos la instancia de la base de datos sin conectarla aún a la app
db = SQLAlchemy()

# 1. LA MÁS ALTA
class CategoriaPadre(db.Model):
    __tablename__ = 'categoria_padre' # Forzamos el nombre para que no haya dudas
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    subcategorias = db.relationship('Subcategoria', backref='padre', lazy=True)

# 2. LA QUE SIGUE
class Subcategoria(db.Model):
    __tablename__ = 'subcategoria'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    categoria_padre_id = db.Column(db.Integer, db.ForeignKey('categoria_padre.id'), nullable=False)
    productos = db.relationship('Producto', backref='subcategoria', lazy=True)

# 3. EL ÚLTIMO ESLABÓN
class Producto(db.Model):
    __tablename__ = 'producto'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    # FIJATE AQUÍ: 'subcategoria.id' en minúsculas
    subcategoria_id = db.Column(db.Integer, db.ForeignKey('subcategoria.id'), nullable=False)
