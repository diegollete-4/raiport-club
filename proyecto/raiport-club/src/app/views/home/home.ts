import { Component } from '@angular/core';


import { BestSellers } from '../../components/best-sellers/best-sellers';
import { CategoryBanner } from '../../components/category-banner/category-banner';

@Component({
  selector: 'app-home',
  imports: [
    BestSellers,
    CategoryBanner
  ],
  templateUrl: './home.html',
  styleUrl: './home.scss',
})
export class HomeComponent {}
