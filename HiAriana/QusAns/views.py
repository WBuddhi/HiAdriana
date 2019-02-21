from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from .forms import DocumentForm

from . import QusAnswer
import json

def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # file_path = request.FILES['file']
            # #file_path = './QusAns/Questions.json'
            # if file_path != None:
            #     Qus_Ans = get_qusans(file_path)
            #     Statement = Qus_Ans.Statement

            return HttpResponse('Uploaded')
    else: form = DocumentForm()
    
    return render(request, 'QusAns/index.html', {'form':form})

def get_qusans(file_path):
    with open(file_path) as f:
        Qus_data = json.load(f)
    Qus_Ans = QusAnswer.QusAns(Qus_data)
    return Qus_Ans

    
    
