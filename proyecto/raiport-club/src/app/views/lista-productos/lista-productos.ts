// views/lista-productos/lista-productos.component.ts
import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, RouterModule } from '@angular/router'; // Para leer el ID de la URL
import { CatalogoService } from '../../services/catalogo';

@Component({
  selector: 'app-lista-productos',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './lista-productos.html',
  styleUrl: './lista-productos.scss'
})
export class ListaProductosComponent implements OnInit {
  productos: any[] = [];
  subcategoriaId: number = 0;

  constructor(
    private route: ActivatedRoute, // El que sabe qué dice la URL
    private catalogoService: CatalogoService
  ) {}

  ngOnInit(): void {
    // Nos "suscribimos" a los cambios de la URL
    // Esto sirve para que si pasas de 'Camisetas' a 'Pantalones', la página se actualice sola
    this.route.params.subscribe(params => {
      this.subcategoriaId = +params['id']; // El '+' convierte el texto en número
      this.cargarProductos();
    });
  }

  cargarProductos(): void {
    this.catalogoService.getProductosBySub(this.subcategoriaId).subscribe({
      next: (data) => {
        this.productos = data;
        console.log('Productos cargados:', this.productos);
      },
      error: (e) => console.error('Error al cargar productos', e)
    });
  }
}