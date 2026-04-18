import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Catalogo } from '../models/catalogo.model';

@Injectable({
  providedIn: 'root'
})
export class CatalogoService {
  private apiUrl = 'http://localhost:5001/api';

  constructor(private http: HttpClient) { }

  // Obtiene el menú completo con categorías y subcategorías
  getCatalogo(): Observable<Catalogo[]> {
    return this.http.get<Catalogo[]>(`${this.apiUrl}/catalogo`);
  }

  // Nuevo método para traer productos de una sección
  getProductosBySub(id: number): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/subcategoria/${id}/productos`);
  }

  // Nuevo método para traer el detalle de un solo producto
  getProductoDetalle(id: number): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/producto/${id}`);
  }
}