from . import QusAnswer
import json
from .models import QA_JFile, Statement, Answer

def insert_json(path):
    #   Inserts json file into database
    #   Inserts first statement into database

    QA_JFile.objects.all().delete()
    with open(path) as f:
        Qus_data = json.load(f)
    Qus_data_string = json.dumps(Qus_data)
    new_qus = QA_JFile()
    new_qus.QA_File = Qus_data_string
    new_qus.save()
    QA_module = QusAnswer.QusAns(Qus_data)
    new_stment_pk = insert_statement(QA_module.Statement, new_qus.pk)
    return new_qus.pk, new_stment_pk

def insert_statement(Statement, qus_pk):
    #   Inserts given statement into database for given questionnaire pk

    qus = QA_JFile.objects.get(pk = qus_pk)
    new_Stment = qus.statement_set.create(Statement_text = Statement)
    return new_Stment.pk

def insert_answer(Answre, Statement_pk):
    #   Insert given answer into database for given statement pk

    stment = Statement.objects.get(pk = Statement_pk)
    new_ans = stment.answer_set.create(choice_text = Answer)
    return new_ans.pk
