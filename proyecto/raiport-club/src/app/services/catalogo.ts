import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Catalogo } from '../models/catalogo.model';

@Injectable({
  providedIn: 'root'
})
export class CatalogoService {
  // La URL de API en Docker
  private apiUrl = 'http://localhost:5001/api/catalogo';

  constructor(private http: HttpClient) { }

  getCatalogo(): Observable<Catalogo[]> {
    return this.http.get<Catalogo[]>(this.apiUrl);
  }
}