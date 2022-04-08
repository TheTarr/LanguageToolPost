import json


# 把原数据集变成对比/经过修改格式
def compare_text(json):
    text = json["text"]
    res = json["edits"]
    compare = ''
    pre = 0
    after = 0
    for i in range(len(res[0][1])):
        after = res[0][1][i][1]
        compare += text[pre:after]
        temp = '[' + str(res[0][1][i][2]) + ']'
        compare += temp
        pre = after
    compare += text[after:]
    return compare


def refine(json):
    text = json["text"]
    edits = json["edits"]
    refined = ''
    pre = 0
    for i in range(len(edits[0][1])):
        after = edits[0][1][i][0]  # start of edition
        refined += text[pre:after]
        if "\n" in text[edits[0][1][i][0]:edits[0][1][i][1]]:  # to make sure the total line of text do not change, in order to evaluation
            refined += text[edits[0][1][i][0]:edits[0][1][i][1]]
        else:
            if edits[0][1][i][2] is None:
                temp = ''
            else:
                temp = str(edits[0][1][i][2])
            refined += temp
        pre = edits[0][1][i][1]
    refined += text[pre:]
    return refined


path = 'json/short.json'
n = 10

f = open(path, encoding='utf-8')
for i in range(n):
    line = f.readline()
    d = json.loads(line)
    # refined = refine(d)
    # print(refined)
    compare = compare_text(d)
    print(compare)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")