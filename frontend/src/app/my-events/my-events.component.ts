import { Component, OnInit } from '@angular/core';

import { ApiService } from '../api.service';

@Component({
  selector: 'app-my-events',
  templateUrl: './my-events.component.html',
  styleUrls: ['./my-events.component.css']
})
export class MyEventsComponent implements OnInit {
   
  todayEvnents;
  constructor(private apiService: ApiService) { }

  ngOnInit() {
  	this.apiService.getTodayEvents().subscribe((data)=>{
      //console.log(data);
      this.todayEvnents = data['todayEvnents'];
      console.log(this.todayEvnents);
    });
  }

}
