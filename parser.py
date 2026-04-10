import requests
from bs4 import BeautifulSoup


def parser():
    url = "https://www.chitai-gorod.ru/search?phrase=python"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Accept-Language': 'ru-RU,ru;q=0.9'
    }
    try:
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, "html.parser")
        cards = soup.find_all('article', class_='product-card')

        books_list = []
        for card in cards:
            title_tag = card.find('a', class_='product-card__title')
            author_tag = card.find('span', class_='product-card__subtitle')
            price_tag = card.find('span', class_='product-mini-card-price__price')

            title = title_tag.get_text(strip=True)
            author = author_tag.get_text(strip=True)
            price = price_tag.get_text(strip=True).replace('\xa0', ' ')

            books_list.append({
                'Название': title,
                'Автор': author,
                'Цена': price
            })

        return books_list

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None