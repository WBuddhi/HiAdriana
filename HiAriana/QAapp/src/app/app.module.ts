import { HttpClientModule } from  '@angular/common/http';

import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule }   from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { QAComponent } from './qa/qa.component';
import { QuestionnaireComponent } from './questionnaire/questionnaire.component';
import { ResultsComponent } from './results/results.component';
import { QAFormComponent } from './qa-form/qa-form.component';



@NgModule({
  declarations: [
    AppComponent,
    QAComponent,
    QuestionnaireComponent,
    ResultsComponent,
    QAFormComponent,
    
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
