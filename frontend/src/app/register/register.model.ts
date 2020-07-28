import { Address } from "../address.model";
import { Mask } from "./mask.model";

export class Register{
  constructor(public info: string,
              public address: Address,
              public masks: Mask[],
              public value: string,
              public default_value: string
  ){

  }

}
