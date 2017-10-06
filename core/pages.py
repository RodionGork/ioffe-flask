import re
import os
import markdown2

def get_folder_path():
    path = os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(path + '/../pages')

def parse(text):
    result = {}
    key = ''
    while True:
        m = re.search(r'^\?(\S+).*[\r\n]+', text, re.MULTILINE)
        if m is None:
            result[key] = text
            break
        else:
            result[key] = text[0 : m.start()]
        key = m.group(1)
        text = text[m.end() :]
    return result

def load(page):
    page = re.sub(r'\/+$', '', page)
    page = get_folder_path() + '/' + page
    if os.path.isdir(page):
        page += '/_idx'
    page += '.txt'
    if not os.path.isfile(page):
        return None
    else:
        with open(page) as f:
            content = parse(f.read())
    if 'text' in content:
        content['text-orig'] = content['text']
        content['text'] = markdown2.markdown(content['text-orig'])
    return content

