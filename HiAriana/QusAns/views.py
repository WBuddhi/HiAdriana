from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .forms import UploadFileForm
from .forms import QA_Form 
from django.conf import settings
from django.core.files.storage import default_storage
from urllib.parse import urlencode
from .models import Statement,Answer

import os
from . import QusAnswer
from . import QusAnsDB as DB
import json


def get_qusans(file_path=None,data=None):
    if data == None:
        with open(file_path) as f:
            Qus_data = json.load(f)
    else: Qus_data = data
    Qus_Ans = QusAnswer.QusAns(Qus_data)
    return Qus_Ans

def index(request):
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
    form = QA_Form()
    
    if request.method == 'GET':
        path = request.GET.get('path')
        pk, Statement, Answers = DB.init_db(path)
    
    if request.method == 'POST':
        answer = request.POST['Choice']
        Statement, Answers, End_of_Qus = DB.process_answer(str(answer), pk)
    
    form.fields['Choice'].choices = [(ans,ans) for ans in Answers]
    form.label = 'NNN'
    return render(request, 'QusAns/Questionnaire.html', 
            {'statement':Statement, 'answers':Answers, 'form':form, 'pk':pk})

