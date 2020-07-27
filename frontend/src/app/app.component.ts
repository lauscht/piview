import { Component, OnInit, OnDestroy } from '@angular/core';
import { BlockService } from "./block.service";
import { Subscription } from "rxjs";
import { Block } from "./block.model";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements  OnInit, OnDestroy {
  title = 'piView';
  blockSubscription: Subscription;
  blocks: Block[];

  constructor(private blockService: BlockService) {
  }

  ngOnInit() {
    this.blockSubscription = this.blockService
      .get()
      .subscribe(res => {
          this.blocks = res;
        },
        console.error
      );
  }

  ngOnDestroy() {
    this.blockSubscription.unsubscribe();
  }
}
