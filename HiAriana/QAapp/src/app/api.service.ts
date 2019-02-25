import { Injectable } from '@angular/core';
import { HttpClient} from  '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  API_URL = 'http://localhost:8000'; /* ULR for Django Rest Framework */
  
  
  constructor(private httpClient: HttpClient) { }

  public uploadfile(QA_file: File){
    const q_url = this.API_URL + '/upload/';
    const formData: FormData = new FormData();
    formData.append('Upload', QA_file, QA_file.name)
    return this.httpClient.post(q_url, formData, 
      { headers: 
        {'enctype':'mulitpart/form-data'}
      }
      )
  }

  public start_qa(){
    return this.httpClient.get(this.API_URL + '/Get_QA/')
  }
  public get_next_qa(answer){
    return this.httpClient.post(
      this.API_URL + '/Get_QA/', answer,
      { headers: 
        {'enctype':'mulitpart/form-data'}
      }
    )
  }
}