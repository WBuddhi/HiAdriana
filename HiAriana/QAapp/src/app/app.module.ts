import { HttpClientModule } from  '@angular/common/http';

import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FileSelectDirective } from 'ng2-file-upload';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { QAComponent } from './qa/qa.component';
import { QuestionnaireComponent } from './questionnaire/questionnaire.component';
import { ResultsComponent } from './results/results.component';



@NgModule({
  declarations: [
    AppComponent,
    QAComponent,
    QuestionnaireComponent,
    ResultsComponent,
    FileSelectDirective,
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
