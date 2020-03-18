import requests
from bs4 import BeautifulSoup as bs


def main():
    a = requests.get("https://google.com.tw")
    print("a:", a)
    print(type(a))
    b = bs(a.text, 'html.parser')
    print("b:", b.div.contents)


if __name__ == '__main__':
    main()
