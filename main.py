import requests
from bs4 import BeautifulSoup

words = '''
1. estrangement
2. predispose
3. premeditate
...
'''.strip().splitlines()

def get_word_root(word):
    response = requests.get(f"https://www.etymonline.com/word/{word}")
    try:
        if response.ok:
            response = response.text
            response = response[response.index(word):]
            response = response[response.index('<section class="word__defination--'):]
            response = response[response.index('<p>'):]
            response = response[:response.index('</section>')]
            response = BeautifulSoup(response, "html.parser").get_text().replace('\n', ' ')
            return response + '\n'
    except: pass
    return None

for line in words:
    request = get_word_root(line.split()[1])
    if request:
        print(line.upper())
        print(request)
