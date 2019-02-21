from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect, reverse
from .forms import UploadFileForm
from django.conf import settings
from django.core.files.storage import default_storage
from urllib.parse import urlencode

import os
from . import QusAnswer
import json


def get_qusans(file_path):
    with open(file_path) as f:
        Qus_data = json.load(f)
    Qus_Ans = QusAnswer.QusAns(Qus_data)
    return Qus_Ans


def index(request):
    if request.method == 'POST':

        #   Uploading file
        save_path = os.path.join(str(settings.MEDIA_ROOT), 'Qusfiles', 
                str(request.FILES['file']))
        path = default_storage.save(save_path, request.FILES['file'])
        
        #   Processing file
        Qus_Ans = get_qusans(path)
        Statement = Qus_Ans.Statement
        
        base_url = reverse('QusAns:qus_ans')
        print(base_url)
        query_string = urlencode({'path':path})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)

    else: form = UploadFileForm()
    return render(request, 'QusAns/index.html', {'form':form})

def qus(request):
    path = request.GET.get('path')
    Qus_Ans = get_qusans(path)
    Statement = Qus_Ans.Statement
    Answers = Qus_Ans.Answers
    return HttpResponse(Statement)
    
