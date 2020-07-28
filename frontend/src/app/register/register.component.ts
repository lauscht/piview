import { Component, Input, OnInit } from '@angular/core';
import { Register } from "./register.model";
import { Mask } from "./mask.model";

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

  reset(){
    this.register.value = this.register.default_value;
  }

  isAuto(mask:Mask):boolean {
    let is_auto: boolean = mask.reset == 'auto';
    console.log(mask, is_auto);
    return is_auto;
  }
}
