// app.routes.ts
import { Routes } from '@angular/router';

import { HomeComponent } from './views/home/home';
import { ListaProductos } from './views/lista-productos/lista-productos';
import { DetalleProducto } from './views/detalle-producto/detalle-producto';

export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'subcategoria/:id', component: ListaProductos },
  { path: 'producto/:id', component: DetalleProducto },
  { path: '**', redirectTo: '' }
];