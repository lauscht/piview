import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import {API_URL} from '../environments/environment';
import {Block} from './block.model';


@Injectable()
export class BlockService {

  constructor(private http: HttpClient) {
  }

  private static _handleError(err: HttpErrorResponse | any) {
    return Observable.throw(err.message || 'Error: Unable to complete request.');
  }

  get(): Observable<Block[]> {
    return this.http
      .get<Block[]>(`${API_URL}/block`)
      .catch(BlockService._handleError);
  }
}
