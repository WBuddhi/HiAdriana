import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { QAComponent } from './qa/qa.component';
import { QuestionnaireComponent } from './questionnaire/questionnaire.component';

const routes: Routes = [
  {path: '', redirectTo: 'qa', pathMatch: 'full'},
  {path: 'qa', component: QAComponent},
  {path: 'questionnaire', component: QuestionnaireComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
