import re
import os

def get_folder_path():
    path = os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(path + '/../pages')

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
            content = f.read()
    return content
