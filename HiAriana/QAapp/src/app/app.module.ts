import { HttpClientModule } from  '@angular/common/http';

import { BrowserModule } from '@angular/platform-browser';
import {CommonModule} from '@angular/common'
import { NgModule } from '@angular/core';
import { FormsModule }   from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { QAComponent } from './qa/qa.component';
import { QuestionnaireComponent } from './questionnaire/questionnaire.component';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { THNavbarComponent } from './thnavbar/thnavbar.component';
import { LayoutModule } from '@angular/cdk/layout';
import { MatToolbarModule, MatButtonModule, MatSidenavModule, MatIconModule, MatListModule, MatGridListModule, MatCardModule, MatMenuModule, MatTableModule, MatPaginatorModule, MatSortModule, MatDialogModule, MatFormFieldModule, MatInputModule,MatSelectModule} from '@angular/material';
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
    CommonModule,
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
    MatInputModule,
    MatSelectModule,
    ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
