from django.shortcuts import render, HttpResponse, redirect, reverse
from .forms import *
from django.conf import settings
from django.core.files.storage import default_storage
from urllib.parse import urlencode

from .models import FileUpload, QA_JFile, Statement, Answer

import os
from . import QusAnswer
from . import QusAnsDB as DB

from QusAns.serializers import FileUploadSerializer, QA_data, QA_input
from rest_framework import viewsets, views, status
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.response import Response


class FileUploadView(viewsets.ModelViewSet):
        '''
                View to upload questionnaire json file:
                Loads the file into the database
        '''
        
        queryset = FileUpload.objects.all()
        serializer_class = FileUploadSerializer
        parser_classes = (MultiPartParser, FormParser, JSONParser,)

class Get_QA(viewsets.ViewSet):
        '''
                Gets the Question and Answers for each step
                At the end of the Questionnaire, returns a dict of al the Questions and Answers
        '''
        
        def list(self, request):
                #       Initialisation process, loads the latest file from the #       database and extracts Question and Answers

                File = FileUpload.objects.latest('pub_datetime')
                path = File.Upload.path
                pk, Statement, Answers = DB.init_db(path)
                data_dict = {'pk':pk, 'Statement':Statement, 'Answers':Answers}
                serializer = QA_data(data_dict)

                return Response(serializer.data)
        
        def post(self, request):
                #       Updates latest question with answer, updates answer 
                #       Updates database and get new question and answer
                #       Generates a list off all Questions and Answers at end

                QA_input_data = QA_input(request.data)
                data = QA_input_data.data
                Statement, Answers, End_of_Qus = DB.process_answer(str(data             ['Answer']), data['pk'])
                if not End_of_Qus:
                        #       Generates next question 
                        data_dict = {'pk':data['pk'], 'Statement':Statement,
                                'Answers':Answers}
                        serializer = QA_data(data_dict)
                        return Response(serializer.data)
                else:
                        #       End of Questions
                        qa_list = DB.generate_list_of_qa(data['pk'])
                        return Response(qa_list)


def index(request):
    #   Main page, request file download


    if request.method == 'POST':
        
        #   Uploading file
        save_path = os.path.join(str(settings.MEDIA_ROOT), 'Qusfiles', 
                str(request.FILES['file']))
        path = default_storage.save(save_path, request.FILES['file'])
        
        #   Open question answer page
        base_url = reverse('QusAns:qus_ans', args=('0',))
        query_string = urlencode({'path':path})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)

    else: form = UploadFileForm()
    return render(request, 'QusAns/index.html', {'form':form})

def qus(request, pk):
    #   Page presenting Question and Answers

    form = QA_Form()
    
    if request.method == 'GET':
        path = request.GET.get('path')
        pk, Statement, Answers = DB.init_db(path)
    
    if request.method == 'POST':
        answer = request.POST['Choice']
        Statement, Answers, End_of_Qus = DB.process_answer(str(answer), pk)
    
        if End_of_Qus:
            #   Redirect to new page to display list of QA
        
            base_url = reverse('QusAns:qa_result', args=(pk,))
            return redirect(base_url)
    
    form.fields['Choice'].choices = [(ans,ans) for ans in Answers]
    form.label = 'NNN'
    return render(request, 'QusAns/Questionnaire.html', 
            {'statement':Statement, 'answers':Answers, 'form':form, 'pk':pk})

def end(request, pk):
    #   Page that displays final list of Question and Answers

    qa_list = DB.generate_list_of_qa(pk)
    qa_head = qa_list[:-1]
    qa_end = qa_list[-1]['Statement']
    return render(request, 'QusAns/Results.html', {'qa_head':qa_head, 'qa_end':qa_end})
        
