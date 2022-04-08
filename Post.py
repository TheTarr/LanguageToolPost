import requests
import json

url = "http://localhost:8081/v2/check"
text = 'i and he are good firends.'
# text = 'he and i are best firends. I go to his house yesterday.'


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


# Modify the original test, each with first value in the value field
def refine_text(text, res):
    none_replacement = 0  # Some suggestions don't have a replacement, that is not determined?s
    refined = ''
    pre = 0
    for i in range(len(res)):
        if res[i]['replacements'] != []:
            after = res[i]['offset']
            refined += text[pre:after]
            temp = str(res[i]['replacements'][0]['value'])
            refined += temp
            pre = after + res[i]['length']
        else:
            none_replacement += 1
    refined += text[pre:]
    print(none_replacement)
    return refined


if __name__ == "__main__":
    response1 = requests_form(url, text)

    print("Original text:")
    print(text)
    print("Refined text:")
    res = process_response(response1)
    refined_text = refine_text(text, res)
    print(refined_text)