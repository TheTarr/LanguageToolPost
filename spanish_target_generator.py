import os
path1 = './spanish_evaluation/3/essays/'
path = './spanish_evaluation/3/corrected/'
ml = []
for root, dirs, files in os.walk(path1):
    for file in files:
        ml.append(file.replace('.txt', '.corrected.txt'))

def match_origin(ml):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file in ml:
                ml.remove(file)
    print(ml)

def get_target():
    for root, dirs, files in os.walk(path):
        for file in files:
            if file in ml:
                f = open(path + str(file), 'r', encoding='utf-8')
                g = f.readlines()
                f.close()
                a = ''
                for line in g:
                    a += line.strip()
                print(a)

# match_origin(ml)
get_target()