import requests
import re


# Функция для загрузки веб-страницы по указанному URL
def download_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при загрузке страницы: {e}")
        return None


# Функция для поиска номеров телефонов на веб-странице
def find_phone_numbers(webpage_text):
    phone_pattern = r"\s*8\s*\(?\d{3}\)?\s*\d{3}\s*\-?\d{2}\s*\-?\d{2}"
    phone_numbers = re.findall(phone_pattern, webpage_text)
    return phone_numbers

# Функция для поиска номеров на веб-странице
def search_phone_number(url):
    webpage_text = download_webpage(url)
    if webpage_text:
        phone_numbers = find_phone_numbers(webpage_text)
        if phone_numbers:
            print("Найденные номера телефонов на данной странице:")
            uniq_phone_number = set(phone_numbers)
            for phone_number in uniq_phone_number:
                print(phone_number)
        else:
            print("На данной странице нет номеров телефонов в указанном формате.")
    else:
        print(f"Не удалось загрузить страницу {url}. Проверьте URL или интернет-соединение.")

if __name__ == "__main__":
    url_list = ["https://hands.ru/company/about", "https://repetitors.info/"]
    for url in url_list:
        search_phone_number(url)


