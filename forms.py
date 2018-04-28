import csv

modulos = ['AST','BAN','CCT','CTE','CVI','CXA','EST',
           'IAG','IAP','ICC','ICP','ICT','IEF','IFP',
           'IGE','INS','IPA','IPT','IVI','PAG','PAR',
           'PTO','REC','VEN']

tipos = ['C', 'P', 'R', 'E', 'A']

with open('forms.csv', 'r', encoding='UTF-8') as csvfile_r:
    read = csv.reader(csvfile_r, delimiter=';', quotechar='"')
    with open('forms-insert.sql', 'w+', encoding='UTF-8') as csvfile_w:
        for row in read:
            if (row[0][1:4].upper() not in modulos) or (row[0][7:8].upper() not in tipos):
                continue

            instrucao = ("insert into tbgerprogramas on existing update " +\
                         "values ('{}', '{}', '{}', '{}');\n".format(
                             row[0][1:8], row[0][1:4], row[0][7:8], row[1]))

            csvfile_w.write(instrucao.upper())
