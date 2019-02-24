from . import QusAnswer
import json
from .models import FileUpload, QA_JFile, Statement, Answer

def init_db(path):
    #   Inserts json file into database
    #   Inserts first statement into database

    #QA_JFile.objects.all().delete()
    File = FileUpload.objects.latest('pub_datetime')
    path = File.Upload.path
    with open(path) as f:
        Qus_data = json.load(f)
    Qus_data_string = json.dumps(Qus_data)
    new_qus = File.qa_jfile_set.create(QA_File = Qus_data_string)
    QA_module = QusAnswer.QusAns(Qus_data)
    new_stment_pk = insert_statement(QA_module.Statement, new_qus.pk)
    return new_qus.pk, QA_module.Statement, QA_module.Answers

def insert_statement(Statement, qus_pk):
    #   Inserts given statement into database for given questionnaire pk

    qus = QA_JFile.objects.get(pk = qus_pk)
    new_Stment = qus.statement_set.create(Statement_text = Statement)
    return new_Stment.pk

def insert_answer(Answer, Statement_pk):
    #   Insert given answer into database for given statement pk

    stment = Statement.objects.get(pk = Statement_pk)
    new_ans = stment.answer_set.create(choice_text = Answer)
    return new_ans.pk

def process_answer(Answer, qus_pk):
    #   Update database with new answer for latest question
    
    #   Get question
    qus = QA_JFile.objects.get(pk = qus_pk)

    #   Get list of statement texts including answers
    sa_list = get_sa_list(qus)
       
    #   Update answer and get latest statement
    latest_stment = sa_list[-1]['Statement']
    stment = Statement.objects.latest('pub_datetime')
    insert_answer(Answer, stment.pk)

    qus_file = get_qus_entry(qus_pk)
    QA_module = QusAnswer.QusAns(qus_file)
    
    for sa in sa_list:
        if sa['Answer'] == None:
            QA_module.next_qus_ans(Answer)
        else:
            QA_module.next_qus_ans(sa['Answer'])

    #   Getting latest statement and answers
    new_stment = QA_module.Statement
    if QA_module.End_of_Qus:
        new_answers = None
    else: new_answers = QA_module.Answers

    #   Updating database with latest question
    stment_pk = insert_statement(new_stment, qus_pk)
    
    return new_stment, new_answers, QA_module.End_of_Qus

def generate_list_of_qa(qus_pk):
    #   Get a list of QA to present

    qus = QA_JFile.objects.get(pk = qus_pk)

    #   Get list of statement texts including answers
    sa_list = get_sa_list(qus)
    return sa_list

def get_qus_entry(qus_pk):
    #   Get json file questionnaire from database
    
    qus_entry = QA_JFile.objects.get(pk = qus_pk)
    return json.loads(qus_entry.QA_File)
        
def get_sa_list(qus):
    #   Extracts all statements and corresponding answers from database and 
    #   returns a ordered list

    stment_list = qus.statement_set.order_by('pub_datetime')
    sa_list = []
    for stment in stment_list:
        if stment.answer_set.exists():
            ans = stment.answer_set.get()
            answer = ans.choice_text
        else: answer = None
        statement = stment.Statement_text
        sa_list.append({'Statement':statement, 'Answer':answer})
    return sa_list

from collections import defaultdict

def test_db(qus_pk):
    qus = QA_JFile.objects.get(pk=qus_pk)
    stment_list = qus.statement_set.order_by('pub_datetime')
    output = []
    for stment in stment_list:
        tmp = defaultdict(list)
        tmp['Statement'].append(stment.Statement_text)
        if stment.answer_set.exists():
            for ans in stment.answer_set.all():
                    tmp['Answer'].append(ans.choice_text)
        output.append(tmp)
    return output
