import { HttpClientModule } from  '@angular/common/http';

import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule }   from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { QAComponent } from './qa/qa.component';
import { QuestionnaireComponent } from './questionnaire/questionnaire.component';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { THNavbarComponent } from './thnavbar/thnavbar.component';
import { LayoutModule } from '@angular/cdk/layout';
import { MatToolbarModule, MatButtonModule, MatSidenavModule, MatIconModule, MatListModule, MatGridListModule, MatCardModule, MatMenuModule, MatTableModule, MatPaginatorModule, MatSortModule, MatDialogModule, MatFormFieldModule, MatInputModule } from '@angular/material';
import { THDashboardComponent } from './thdashboard/thdashboard.component';
import { NameComponent } from './name/name.component';

@NgModule({
  declarations: [
    AppComponent,
    QAComponent,
    QuestionnaireComponent,
    THNavbarComponent,
    THDashboardComponent,
    NameComponent,
    
  ],

  imports: [
    BrowserModule,BrowserAnimationsModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    LayoutModule,
    MatFormFieldModule,
    MatDialogModule,
    MatToolbarModule,
    MatButtonModule,
    MatSidenavModule,
    MatIconModule,
    MatListModule,
    MatGridListModule,
    MatCardModule,
    MatMenuModule,
    MatTableModule,
    MatPaginatorModule,
    MatSortModule,
    MatInputModule
    ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
