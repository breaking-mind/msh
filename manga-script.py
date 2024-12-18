from requests import get
from bs4 import BeautifulSoup

def __to_bs4(url:str):
    """
    convert html string to BeautifulSoup object
    """
    return BeautifulSoup(get(url).content, 'html.parser')

def list_mangas_to_translate(url:str):
    """
    get list of mangá chapters to translate from mangadex
    """
    num_chapters_to_translate = []
    page = __to_bs4(url)
    divs_manga_list = page.find_all('div', class_='bg-accent')
    print(divs_manga_list)
    for div in divs_manga_list:
        has_br = div.find('img', attrs={'title':'Portuguese (Br)'})
        if has_br:
            num_chapters_to_translate.append(has_br)
    return len(num_chapters_to_translate)

if __name__ == "__main__":
    url = 'https://mangadex.org/title/50cb0480-1baf-4c63-b8c4-0145d1f1cd5e/we-shall-now-begin-ethics'
    print(f'Number of chapters to translate: {list_mangas_to_translate(url)}')