'''

Extract questionnear from JSON file and present questions

'''

import json
from pathlib import Path

class QusAns:
    def __init__(self, data):
        self.data = data
        self.Statement = None
        self.Answers = None
        self.End_of_Qus = False
        self.log = {}
        self.data_hist = []

        self.get_qus_ans()
        
    def get_qus_ans(self, update_hist = True):
        #   Extract Initial Question and Answers

        if type(self.data) == dict:
            try:
                for keys, values in self.data.items():
                    self.Statement = str(keys)
                    self.Answers = list(values.keys())[:5]
                    self.data = self.data[self.Statement]
                    if update_hist:
                        self.data_hist.append({self.Statement: self.data})
            except:
                self.End_of_Qus = True
                self.Statement = "File Error"
        else: 
            self.Statement = self.data
            self.Answers = None
            self.update_log(None)
            self.End_of_Qus = True

    def next_qus_ans(self, Answer):
        #   Get next Question and Answers

        if not self.End_of_Qus:
            if Answer in self.Answers:
                self.update_log(Answer) 
                self.data = self.data[Answer]
                self.get_qus_ans()
        else: print('End of Questions')

    def prev_qus_ans(self):
        #   Get previous qustion and answer
        if len(self.data_hist) > 1:
            self.data_hist.pop()
            self.data = self.data_hist[-1]
            self.get_qus_ans(update_hist = False)
        else:
            print('Back to inital Question')

    def update_log(self, Answer):
        self.log[self.Statement] = Answer

    def validate_data(self):
        #   To be implemented: Check if questions have more than 5 answers
        pass

