import { Component, OnInit } from '@angular/core';
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

  ngOnInit() {
    this.start_qa_page();
  }
  public start_qa_page(){
    this.apiService.start_qa().subscribe((data: Array<object>) => {
      
      this.pk = data['pk'];
      this.Statement = data['Statement'];
      this.Answers = data['Answers']
    })
  }
  public next_qa(Ans: string){
    var Answer_Reply = {'pk':this.pk, 'Answer':Ans}
    console.log(Answer_Reply)
    this.apiService.get_next_qa(Answer_Reply).subscribe((data: Array<object>) => {
      
      this.pk = data['pk'];
      this.Statement = data['Statement'];
      this.Answers = data['Answers']
    })
  }
  

}
