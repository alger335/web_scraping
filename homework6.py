import requests
from bs4 import BeautifulSoup


def web_request(habr_url):
    response = requests.get(habr_url)
    if not response.ok:
        raise RuntimeError('Сайт недоступен!')
    text = response.text
    return text


def soup_func(text):
    soup = BeautifulSoup(text, features='html.parser')
    articles = soup.find_all('article')
    return articles


#Вывести в консоль список подходящих статей в формате: <дата> - <заголовок> - <ссылка>.
def habr_scrap(articles, KEYWORDS):
    for article in articles:
        for h in article.find_all('div', class_='post__text'):
            hubs = set(h.text.strip().split())
            if hubs & KEYWORDS:
                a = article.find('a', class_='post__title_link')
                t = article.find('a', class_='post__title_link').text
                d = article.find('span', class_='post__time').text
                h_link = a.attrs.get('href')
                print(f'{d} - {t}. Ссылка: {h_link}')
