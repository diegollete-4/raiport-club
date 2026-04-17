from flask_sqlalchemy import SQLAlchemy

# Creamos la instancia de la base de datos sin conectarla aún a la app
db = SQLAlchemy()

class CategoriaPadre(db.Model):
    __tablename__ = 'categorias_padre'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    # Relación: permite acceder a las subcategorías desde el padre
    subcategorias = db.relationship('Subcategoria', backref='padre', lazy=True)

class Subcategoria(db.Model):
    __tablename__ = 'subcategorias'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    categoria_padre_id = db.Column(db.Integer, db.ForeignKey('categorias_padre.id'), nullable=False)
    # Relación: permite acceder a los productos desde la subcategoría
    productos = db.relationship('Producto', backref='subcategoria', lazy=True)

class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    imagen = db.Column(db.String(255))
    subcategoria_id = db.Column(db.Integer, db.ForeignKey('subcategorias.id'), nullable=False)