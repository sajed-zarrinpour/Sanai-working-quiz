import { Component, OnInit } from '@angular/core';

import { ApiService } from '../api.service';

@Component({
  selector: 'app-month-events',
  templateUrl: './month-events.component.html',
  styleUrls: ['./month-events.component.css']
})
export class MonthEventsComponent implements OnInit {

  constructor(private apiService: ApiService) { }
  thismonthEvents;
  ngOnInit() {
  	this.apiService.getThisMonthEvents().subscribe((data)=>{
      //console.log(data);
      this.thismonthEvents = data['thismonthEvents'];
      console.log(this.thismonthEvents);
    });
  }

}
