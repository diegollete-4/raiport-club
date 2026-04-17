import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common'; // Para usar *ngFor en el HTML
import { CatalogoService } from '../../services/catalogo'; 
import { Catalogo } from '../../models/catalogo.model';

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [CommonModule], // Importante para que funcione el bucle en el HTML
  templateUrl: './navbar.html',
  styleUrl: './navbar.scss',
})


export class Navbar implements OnInit {
  // Aquí guardaremos lo que venga del Backend
  categorias: Catalogo[] = [];

  constructor(private catalogoService: CatalogoService) {}

  ngOnInit(): void {
    // Cuando el componente carga, pedimos los datos
    this.catalogoService.getCatalogo().subscribe({
      next: (data) => {
        this.categorias = data;
        console.log('Catálogo recibido en el Navbar:', this.categorias);
      },
      error: (e) => {
        console.error('Error al obtener el catálogo:', e);
      }
    });
  }
}