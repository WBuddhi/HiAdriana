from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from .forms import UploadFileForm
from django.conf import settings
from django.core.files.storage import default_storage

import os
from . import QusAnswer
import json

def index(request):
    if request.method == 'POST':
            # #file_path = './QusAns/Questions.json'
            # if file_path != None:
            #     Qus_Ans = get_qusans(file_path)
            #     Statement = Qus_Ans.Statement

        #   Uploading file
        save_path = os.path.join(str(settings.MEDIA_ROOT), 'Qusfiles', 
                str(request.FILES['file']))
        path = default_storage.save(save_path, request.FILES['file'])
        
        #   Processing file
        Qus_Ans = get_qusans(path)
        Statement = Qus_Ans.Statement
        
        return HttpResponse(Statement)

    else: form = UploadFileForm()
    return render(request, 'QusAns/index.html', {'form':form})

def get_qusans(file_path):
    with open(file_path) as f:
        Qus_data = json.load(f)
    Qus_Ans = QusAnswer.QusAns(Qus_data)
    return Qus_Ans

    
    
