"""Sum email sending sorting by hour"""

hour_email = {}

try:
    handle = open(r'Hour_histogram_email\mbox-short.txt',
                  'r', encoding='UTF-8')
except Exception:
    print('Cannot reach it. The program will be terminated')
    exit()

for lines in handle:
    lines = lines.rstrip()
    words = lines.split()
    if len(words) == 0 or words[0] != 'From':
        continue
    hour = words[5]
    hour = hour[:2]
    hour_email[hour] = hour_email.get(hour, 0) + 1

lst_ht = []

for key, val in hour_email.items():
    lst_ht.append((key, val))
    # lst_ht.sort() ESTAVA TENTANDO EXIBIR DENTRO DO PROPRIO FOR QUE CRIOU
    # print(key, val) O SORT PRECISA ESTAR FORA PARA ALTERAR DEFINITIVAMENTE O LST

lst_ht.sort()

for key, val in lst_ht:
    print(key, val)
