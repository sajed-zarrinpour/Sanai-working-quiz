import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WeekEventsComponent } from './week-events.component';

describe('WeekEventsComponent', () => {
  let component: WeekEventsComponent;
  let fixture: ComponentFixture<WeekEventsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WeekEventsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WeekEventsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
