import { Injectable } from '@angular/core';

import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  BASE_URL = 'http://localhost:5000';
  constructor(private httpClient: HttpClient) { }
  public getTodayEvents(){
    return this.httpClient.get(`${this.BASE_URL}/`);
  }
  public getThisWeekEvents(){
    return this.httpClient.get(`${this.BASE_URL}/this_week`);
  }
  public getThisMonthEvents(){
    return this.httpClient.get(`${this.BASE_URL}/this_month`);
  }
}
