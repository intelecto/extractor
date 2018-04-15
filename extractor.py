"""
Extract the file name and form name of all forms from all directories 
and subdirectories of the Delphi projects and write to the CSV file.

"""

import os
import csv

class Extractor:

    def __init__(self):
        self.ROOT_DIR = ''
        self.EXCLUDE_DIRS = [] 
        self.EXCLUDE_FILES_WITH = []
        self.VALID_EXTENSION = ''
        self.CSV_FILE = ''
        self.formList = {}

    def fixFormCaption(self, line):
        """
        Fix ASCII code
        """
        fix = {'#39' : '',  '#186': 'º', '#195': 'Ç', '#231': 'ç',
               '#192': 'A', '#193': 'Á', '#199': 'Ã', '#174': 'C',
               '#194': 'Â', '#226': 'â', '#227': 'ã', '#225': 'á',
               '#224': 'à', '#201': 'É', '#202': 'Ê', '#233': 'é',
               '#234': 'ê', '#205': 'Í', '#237': 'í', '#211': 'Ó',
               '#212': 'Ô', '#243': 'ó', '#244': 'ô', '#245': 'õ',
               '#218': 'Ú', '#220': 'Ü', '#250': 'ú', '#252': 'ü'}

        for key, value in fix.items():
            line = line.replace(key, value)
        return line

    def lineBreak(self, line):
        """
        Remove line break
        """
        return line.replace('\n', '') 

    def lineCaption(self, line):
        """
        Clean Form name
        """
        line = line.replace('Caption = ', '')
        line = line.replace("'", '')
        line = line.replace("~", '')
        line = line.replace("+", '')
        return line.strip()

    def onlyFormname(self, form):
        """
        NAME1.dfm -> FNAME1
        """
        return 'F'+form.replace('.dfm', '')

    def saveCSV(self):
        """
        Save dictionary to CSV file
        """
        with open(self.CSV_FILE, 'w', newline='') as csvfile:
            filename = csv.writer(csvfile, delimiter=';')
            filename.writerow(['Form','Name'])
            for key, value in self.formList.items():
                filename.writerow([key, value])

    def findFiles(self):
        """
        Find files in directory e subdirectories
        """
        for root, dirs, files in os.walk(self.ROOT_DIR):
            if any(root.startswith(path) for path in self.EXCLUDE_DIRS):
                continue
            for file in files:
                if file.endswith(self.VALID_EXTENSION) and \
                not any([file.startswith(s) for s in self.EXCLUDE_FILES_WITH]) and \
                not any([file.endswith(s) for s in self.EXCLUDE_FILES_WITH]):
                    with open(os.path.join(root, file), 'r', encoding='latin-1') as filename:
                        line_index = 0
                        for line in filename:
                            s_line = line.lstrip()
                            line_index += 1
                            if any([s_line.startswith(s) for s in ['Caption = ']]):

                                # remove linebreak
                                s_line = self.lineBreak(s_line)

                                # clean form name
                                s_line = self.lineCaption(s_line)
                                if s_line == '':
                                    s_line_aux = filename.readlines()[0]
                                    s_line = s_line + s_line_aux
                                s_line = self.lineCaption(s_line)

                                # fix caracters code
                                s_line = self.fixFormCaption(s_line)

                                # extract form names
                                form_code = self.onlyFormname(file)

                                # list iter
                                self.formList[form_code] = s_line
                                
                                # break loop 
                                break

if __name__ == "__main__":
    
    extract = Extractor()
    extract.ROOT_DIR = '.\\SIS'
    extract.EXCLUDE_DIRS = [r'.\SIS\ACBr', 
                            r'.\SIS\SISMobile', 
                            r'.\SIS\SISDLL'] 

    extract.EXCLUDE_FILES_WITH = ['900A.dfm',
                                  'BARVERTICAL',
                                  'Frame',
                                  'PAI']

    extract.VALID_EXTENSION = '.dfm'
    extract.CSV_FILE = 'result.csv'
    extract.formList = {}

    extract.findFiles()

    extract.saveCSV()
