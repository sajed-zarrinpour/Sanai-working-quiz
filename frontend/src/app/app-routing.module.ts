import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { MyEventsComponent } from './my-events/my-events.component';
import { WeekEventsComponent } from './week-events/week-events.component';
import { MonthEventsComponent } from './month-events/month-events.component';

const routes: Routes = [
	{path:'today', component: MyEventsComponent},
	{path:'this-week', component: WeekEventsComponent},
	{path:'this-month', component: MonthEventsComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
