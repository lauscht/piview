import { Register } from "./register/register.model";


export class Block{
  constructor(
    public name: string,
    public version: string,
    public info: string,
    public registers: { [name:string]:Register}
  ){}
}
