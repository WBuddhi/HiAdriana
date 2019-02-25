import { Component, OnInit } from '@angular/core';
import {CommonModule} from '@angular/common'
import { ApiService } from  '../api.service';

@Component({
  selector: 'app-questionnaire',
  templateUrl: './questionnaire.component.html',
  styleUrls: ['./questionnaire.component.css']
})

export class QuestionnaireComponent implements OnInit {

  constructor(private  apiService:  ApiService) { }

  Statement: string;
  Answers = [];
  pk: number;
  QA_Form: boolean;
  Entries = [];
  Last_Entry;

  ngOnInit() {
    this.QA_Form = true;
    this.start_qa_page();
  }
  public start_qa_page(){
    this.apiService.start_qa().subscribe((data: Array<object>) => {
      if (data.hasOwnProperty('Statement')==true){
        this.QA_Form = true;
        this.pk = data['pk'];
        this.Statement = data['Statement'];
        this.Answers = data['Answers']
      } else {
        this.QA_Form = false;
        this.Last_Entry = {'Statement':'Invalid File'};
      }
      
    },Error =>{
      if(Error != ''){
        this.QA_Form = false;
        this.Last_Entry = {'Statement':'Invalid File'};
      }
    })
  }
  public next_qa(Ans: string){
    var Answer_Reply = {'pk':this.pk, 'Answer':Ans}
    this.apiService.get_next_qa(Answer_Reply).subscribe((data: Array<object>) => {
      this.QA_Form = true;
      var test = {'pk':1, 'Ans':"asdfa"}
      if ('pk' in data){
        this.pk = data['pk'];
        this.Statement = data['Statement'];
        this.Answers = data['Answers']

      }else{
        this.QA_Form = false;
        this.Statement = 'End of Questions';
        this.pk = 0;
        this.Answers = [];
        this.Entries = data;
        this.Last_Entry = this.Entries.pop();
      };
    })
  }
}
