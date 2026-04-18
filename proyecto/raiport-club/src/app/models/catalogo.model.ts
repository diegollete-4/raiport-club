export interface Subcategoria {
  id: number;
  nombre: string;
}

export interface Catalogo {
  id: number;
  nombre: string;
  subcategorias: Subcategoria[]; // <-- Ahora es una lista de objetos, no solo texto
}