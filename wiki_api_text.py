import requests
import mwparserfromhell

def get_article_text(page_title, lang = "en"):
    api_url = "https://%s.wikipedia.org/w/api.php"%lang
    headers = {"User-Agent": "MGerlach_(WMF) API tutorial"}
    params = {
        "action": "query",
        "prop": "revisions",
        "rvprop": "content",
#         "rvsection": "0", ## if you only want the first section
        "titles": page_title,
        "format": "json",
        "formatversion": "2",
}
    req = requests.get(api_url, headers=headers, params=params).json()
    req_query = req.get("query")
    req_pages = req_query.get("pages")
    page = req_pages[0]
    wikitext = page.get("revisions",[])[0].get("content","")
    return wikitext

page_title = "Muon"
wikitext = get_article_text(page_title)
print(wikitext)

text = mwparserfromhell.parse(wikitext).strip_code()
print(text[:100])