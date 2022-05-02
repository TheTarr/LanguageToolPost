import os
path = './spanish_evaluation/3/essays/'
flag = 0

for root, dirs, files in os.walk(path):
    for file in files:
        f = open(path + str(file), 'r', encoding='utf-8')
        g = f.readlines()
        f.close()
        a = ''
        for line in g:
            a += line.strip()
        if len(a) <= 1500:
            print(a)
#             flag += 1
#
# print(flag)