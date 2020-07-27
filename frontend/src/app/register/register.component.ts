import { Component, Input, OnInit } from '@angular/core';
import { Register } from "./register.model";

@Component({
  selector: 'register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  @Input() name: string;
  @Input() register: Register;
  constructor() { }

  ngOnInit(): void {
  }

}
