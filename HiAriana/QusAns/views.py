from django.shortcuts import render, HttpResponse

from . import QusAnswer
import json

def index(request):
    file_path = './QusAns/Questions.json'
    if file_path != None:
        Qus_Ans = get_qusans(file_path)
        Statement = Qus_Ans.Statement

        return HttpResponse(Statement)
    else: return HttpResponse("File not loaded")

def get_qusans(file_path):
    with open(file_path) as f:
        Qus_data = json.load(f)
    Qus_Ans = QusAnswer.QusAns(Qus_data)
    return Qus_Ans

    
    
