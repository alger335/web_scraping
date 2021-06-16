from homework6 import *

def main():
    KEYWORDS = {'3D', 'Intel', 'Kotlin', 'python', 'мониторинг', 'Microsoft', 'Linux'}
    rtext = web_request('https://habr.com/ru/all/')
    rsoup = soup_func(rtext)
    habr_scrap(rsoup, KEYWORDS)


if __name__ == '__main__':
    main()
