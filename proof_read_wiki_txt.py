# This file is designed to take wiki txt and do proof read
import requests
import os


# input: the file directory which contains all wiki txt
# output: a list of names of all txt, strings
def get_all_path(file_dir):
    files = os.listdir(file_dir)
    return files


# input: path to a txt file
# output: a string, what's in the txt file
def get_text(path):
    f = open(path, 'r', encoding='utf-8')
    g = f.readlines()
    f.close()
    gs = ''.join(g)
    return gs


# Post a request and get response
def requests_form(url, text):
    data = {'language': 'en-US', 'text': text}
    response = requests.post(url, data)
    return response


# Get the 'matches' field of the response
def process_response(response):
    raw_res = response.json()
    res = raw_res['matches']
    return res


# Get the refined text
# "matches": [
# {
#   "message": "This sentence does not start with an uppercase letter.",
#   "shortMessage": "",
#   "replacements": [
#     {
#       "value": "This"
#     }
#   ],
#   "offset": 0,
#   "length": 4,
#   "context": {
#     "text": "this is a test. this is another.",
#     "offset": 0,
#     "length": 4
#   },
#   "sentence": "this is a test.",
#   "type": {
#     "typeName": "Other"
#   },
#   "rule": {
#     "id": "UPPERCASE_SENTENCE_START",
#     "description": "Checks that a sentence starts with an uppercase letter",
#     "issueType": "typographical",
#     "category": {
#       "id": "CASING",
#       "name": "Capitalization"
#     },
#     "isPremium": false
#   },
#   "ignoreForIncompleteSentence": true,
#   "contextForSureMatch": -1
# },


# input: origin string, and res (what modified)
# output: a string, with each modification attached in []
def compare_text(text, res):
    compare = ''
    pre = 0
    after = 0
    for i in range(len(res)):
        after = res[i]['length'] + res[i]['offset']
        compare += text[pre:after]
        if res[i]['replacements']:
            temp = '[' + str(res[i]['replacements'][0]['value']) + ']'
            compare += temp
        else:
            compare += '[]'
        pre = after
    compare += text[after:]
    return compare


# if __name__ == "__main__":
#     # url = "http://localhost:8081/v2/check"
#     # text = get_text("C:/Users/x5/LanguageToolPost/test/Baenidae.txt")
#     # response1 = requests_form(url, text)
#     # res = process_response(response1)
#     # compared_text = compare_text(text, res)
#     # print(compared_text)
#     url = "http://localhost:8081/v2/check"
#     all_txt_name = get_all_path("C:/Users/x5/LanguageToolPost/wiki_text/")
#     for i in all_txt_name:
#         text = get_text("C:/Users/x5/LanguageToolPost/wiki_text/"+i)
#         response = requests_form(url, text)
#         res = process_response(response)
#         compared_text = compare_text(text, res)
#         print(compared_text)

# temp
if __name__ == "__main__":
    url = "https://api.languagetoolplus.com/v2/check"
    text = "It's difficult answer at the question \"what are you going to do in the future?\" if the only one who has to know it is in two minds. When I was younger I used to say that I wanted to be a teacher, a saleswoman and even a butcher.. I don't know why. I would like to study Psychology because one day I would open my own psychology office and help people. It's difficult because I'll have to study hard and a lot, but I think that if you like a subject, you'll study it easier. Maybe I'll change my mind, maybe not."
    response = requests_form(url, text)
    res = process_response(response)
    compared_text = compare_text(text, res)
    print(compared_text)