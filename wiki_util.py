# This file is designed to get wiki text
# All text will be stored as a txt file in ./wiki_text/
import wikipedia
import random

data_path = "./wiki_text/"


def crawl_wiki(title):
    wiki = wikipedia.page(title)

    text = wiki.content
    name = data_path + title + '.txt'
    with open(name, 'w', encoding='utf-8') as f:
        f.write(text)
    f.close()

    links = wiki.links
    random.shuffle(links)
    print(links[0])
    try:
        crawl_wiki(links[0])
    except:
        crawl_wiki(links[1])


crawl_wiki("Neural networks")
