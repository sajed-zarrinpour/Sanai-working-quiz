import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { HttpClientModule } from '@angular/common/http';
import { MyEventsComponent } from './my-events/my-events.component';
import { WeekEventsComponent } from './week-events/week-events.component';
import { MonthEventsComponent } from './month-events/month-events.component';

@NgModule({
  declarations: [
    AppComponent,
    MyEventsComponent,
    WeekEventsComponent,
    MonthEventsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
