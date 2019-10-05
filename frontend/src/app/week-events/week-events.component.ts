import { Component, OnInit } from '@angular/core';

import { ApiService } from '../api.service';

@Component({
  selector: 'app-week-events',
  templateUrl: './week-events.component.html',
  styleUrls: ['./week-events.component.css']
})
export class WeekEventsComponent implements OnInit {

  constructor(private apiService: ApiService) { }
  thisweekEvents;
  ngOnInit() {
  	this.apiService.getThisWeekEvents().subscribe((data)=>{
      //console.log(data);
      this.thisweekEvents = data['thisweekEvents'];
      console.log(this.thisweekEvents);
    });
  }

}
