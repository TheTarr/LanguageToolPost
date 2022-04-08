# This file is designed to take a string and get response from LanguageTool
import requests
import json
import time
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
            compare += '[NO SUGGEST VALUE]'
        pre = after
    compare += text[after:]
    return compare


def display_detail(text, res):
    compare = ''
    pre = 0
    after = 0
    for i in range(len(res)):
        after = res[i]['length'] + res[i]['offset']
        compare += text[pre:after]
        if res[i]['replacements'] and res[i]['rule']["id"] != "WRONG_APOSTROPHE":
            temp = '[' + str(res[i]['message']) + '[' + str(res[i]['replacements'][0]['value']) + ']]'
            compare += temp
        else:
            compare += '[NO SUGGEST VALUE]'
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
    # url = "http://localhost:8081/v2/check"
    origin_file = 'json/short.json'
    f = open(origin_file, encoding='utf-8')
    for i in range(5):
        line = f.readline()
        d = json.loads(line)
        text = d["text"]
        if text[0] == '\n':
            print()
            text = text[1:]
        response = requests_form(url, text)
        time.sleep(3)
        try:
            res = process_response(response)
            refined_text = refine(text, res)
            print(refined_text)
            # compared_text = compare_text(text, res)
            # print(compared_text)
            # display = display_detail(text, res)
            # print(display)
            print("+++++++++++++++++++++++++++++++")
            # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        except:
            print("=============================problem==========================")
            print(text)
        # compared_text = compare_text(text, res)
        # print(compared_text)
    f.close()
