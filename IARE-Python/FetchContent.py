import requests

def fetch_content_from_wiki(url):
    page = requests.get(url)
    content = page.content
    return content

wiki_url = "https://www.youtube.com"
content = fetch_content_from_wiki(wiki_url)
print(content)
