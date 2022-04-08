import time
from groud_truth_check import *

url = "https://api.languagetoolplus.com/v2/check"
file_path = "D:/lang-8/lang-8-en-1.0/entries.train"
number_of_lines = 5000
pre_punctuation = [',', '.', '!', '?', "'", ')', ':', '~']
both_punctuation = ['-']
after_punctuation = ['(']

def format(str):
    j = 1
    i = 2
    temp = ''
    temp += str[0]
    while i < len(str):
        if str[i] in pre_punctuation:
            temp += str[i]
            i += 2
            j += 2
        elif str[i] in both_punctuation:
            temp += str[i]
            i += 3
            j += 3
        elif str[i] in after_punctuation:
            temp += str[j]
            temp += str[i]
            i += 3
            j += 3
        else:
            temp += str[j]
            i += 1
            j += 1
    temp2=''
    pre = 0
    for x in range(len(temp)-2):
        if temp[x:(x+2)] == "'t":
            temp2 += temp[pre:x-1]
            temp2 += 'n'
            pre = x
    temp2+= temp[pre:]
    return temp2

def print_original(temp):
    if len(temp) == 5 or len(temp) == 6:
        original = format(temp[4])
        print(original.strip('\n'))

def print_target(temp):
    if len(temp) == 5:
        target = format(temp[4])
        print(target.strip('\n'))
    if len(temp) == 6:
        target = format(temp[5])
        print(target.strip('\n'))



f = open(file_path, encoding='utf-8')
for i in range(number_of_lines):
    line = f.readline()
    # temp[0] is how many changes, temp[4] is the original sentence, temp[5] is the corrected sentence.
    temp = line.split("	")
    # print_original(temp)
    # print_target(temp)
    if len(temp) == 5 or len(temp) == 6:
        text = format(temp[4])
        response = requests_form(url, text)
        time.sleep(3)
        res = process_response(response)
        refined_text = refine(text, res)
        print(refined_text.strip('\n'))