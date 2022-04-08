# This file is designed to pre-process wiki txt
# unfinish!
import os

path = './test/'


def filter_files(text_path):
    files = os.listdir(text_path)
    f = open(path+files[1], 'r', encoding='utf-8')
    g = f.readlines()
    f.close()
    gs = ''.join(g)
    print(gs)
    # for i in files:
    #     print(i)
    #     f = open(path+i)

filter_files(path)

