import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from "@angular/common/http";

import { AppComponent } from './app.component';

import { BlockService } from "./block.service";
import { RegisterComponent } from './register/register.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

@NgModule({
  declarations: [
    AppComponent,
    RegisterComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    NgbModule
  ],
  providers: [ BlockService ],
  bootstrap: [ AppComponent ]
})
export class AppModule { }
