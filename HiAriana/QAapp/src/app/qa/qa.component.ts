import { Component, OnInit } from '@angular/core';
import { ApiService } from  '../api.service';
import {  FileUploader, FileSelectDirective } from 'ng2-file-upload/ng2-file-upload';

const URL = 'http://localhost:8000/upload/';

@Component({
  selector: 'app-qa',
  templateUrl: './qa.component.html',
  styleUrls: ['./qa.component.css']
})
export class QAComponent implements OnInit {

  constructor(private  apiService:  ApiService) { }
  
  Start_QA = true;
  fileToUpload: File = null;

  ngOnInit() {}


  handleFileInput(files: FileList) {
    this.fileToUpload = files.item(0);
    return this.apiService.uploadfile(this.fileToUpload).subscribe((response) => {console.log(response);
      this.Start_QA = false;});
  };

}


