# url = "http://localhost:8081/v2/check"
# text = "Don’t forget to put on the breaks."
#
# import requests
#
#
# # Post a request and get response
# def requests_form(url, text):
#     data = {'language': 'en-US', 'text': text}
#     response = requests.post(url, data)
#     return response
# # Get the 'matches' field of the response
# def process_response(response):
#     raw_res = response.json()
#     res = raw_res['matches']
#     return res
# def compare_text(text, res):
#     compare = ''
#     pre = 0
#     after = 0
#     for i in range(len(res)):
#         after = res[i]['length'] + res[i]['offset']
#         compare += text[pre:after]
#         if res[i]['replacements'] and res[i]['rule']["id"] != "WRONG_APOSTROPHE":
#             temp = '[' + str(res[i]['replacements'][0]['value']) + ']'
#             compare += temp
#         else:
#             compare += '[]'
#         pre = after
#     compare += text[after:]
#     return compare
#
# response = requests_form(url, text)
# res = process_response(response)
# compared_text = compare_text(text, res)
# print(compared_text)

# import json
#
# path = 'json/A.train.json'
# new = 'json/short.json'
# n = 1200
#
# f = open(path, encoding='utf-8')
# for i in range(n):
#     line = f.readline()
#     d = json.loads(line)
#     if len(d["text"]) < 1300:
#         print(i)
#         with open(new, 'a') as wf:
#             json.dump(d, wf)
#             wf.write('\n')



# This file is designed to take a string and get response from LanguageTool
import requests
import json
null = None

# Post a request and get response
def requests_form(url, text):
    data = {'language': 'en-US', 'text': text}
    response = requests.post(url, data)
    return response


# Get the 'matches' field of the response
def process_response(response):
    raw_res = response.json()
    res = raw_res['matches']
    print(str(res))
    return res


def compare_text(text, res):
    compare = ''
    pre = 0
    after = 0
    for i in range(len(res)):
        after = res[i]['length'] + res[i]['offset']
        compare += text[pre:after]
        if res[i]['replacements'] and res[i]['rule']["id"] != "WRONG_APOSTROPHE":
            temp = '[' + str(res[i]['replacements'][0]['value']) + ']'
            compare += temp
        else:
            compare += '[]'
        pre = after
    compare += text[after:]
    return compare


def refine(text, res):
    refined = ''
    pre = 0
    for i in range(len(res)):
        after = res[i]['offset']
        refined += text[pre:after]
        if res[i]['replacements']:
            if res[i]['rule']["id"] != "WRONG_APOSTROPHE" and '\n' not in text[res[i]['offset']:res[i]['offset']+res[i]['length']] and '\n' not in str(res[i]['replacements'][0]['value']):
                temp = str(res[i]['replacements'][0]['value'])
            else:
                temp = text[after:(after + res[i]['length'])]

            refined += temp
        else:
            temp = text[after:(after + res[i]['length'])]
            refined += temp
        pre = after + res[i]['length']
    refined += text[pre:]
    return refined


if __name__ == "__main__":
    url = "https://api.languagetoolplus.com/v2/check"
    d = {"text": "Motorola It was the first doing something to a mobile phone  was on 3 April 1973 the first to do so was an employee of Martin Cooper\nCooper made mobile phone history in April 1973 when he made the first ever call on a handheld mobile phone", "id": "1-61974", "cefr": "A2.i", "edits": [[0, [[50, 60, ""], [61, 65, ""], [115, 122, "not now"], [154, 158, None], [242, 246, "run"], [247, 249, "around"], [276, 278, "them"], [305, 311, ""], [350, 353, "their"], [382, 382, "to "]]]], "userid": "11116"}
    # d = {"text": "In the following decades revolution and civil smote many of the Powers of Europe, and new nations were born. Britain alone escaped almost unscathed from these years of unrest. There was an unparalleled expansion of the English-Speaking Peoples both by birth and emigration.", "id": "1-221491", "cefr": "A1.i", "edits": [[0, [[24, 24, ","], [45, 45, " wars"], [46, 51, null]]]], "userid": "31574"}

    text = d["text"]
    if text[0] == '\n':
        print()
        text = text[1:]
    response = requests_form(url, text)
    try:
        res = process_response(response)
        refined_text = refine(text, res)
        print(refined_text)
        refined_text = compare_text(text, res)
        print(refined_text)
    except:
        print("=============================problem==========================")
        print(text)
        # compared_text = compare_text(text, res)
        # print(compared_text)