import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Header } from './components/header/header';
import { Navbar } from './components/navbar/navbar';
import { Carousel } from './components/carousel/carousel';
import { Footer } from './components/footer/footer';

@Component({
  selector: 'app-root',
  imports: [   
    RouterOutlet,
    Header,
    Navbar,
    Carousel,
    Footer],

  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App {
  protected readonly title = signal('raiport-club');
}
