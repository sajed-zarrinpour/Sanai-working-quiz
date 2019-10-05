import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MonthEventsComponent } from './month-events.component';

describe('MonthEventsComponent', () => {
  let component: MonthEventsComponent;
  let fixture: ComponentFixture<MonthEventsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MonthEventsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MonthEventsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
