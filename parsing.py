import requests
from bs4 import BeautifulSoup


def get_availability_of_goods(soup):
    check_availability = soup.find('span', class_='local')
    if check_availability is None:
        non_avail = soup.find('div', class_='product-item__status red')
        if non_avail is not None:
            return False
    else:
        return True


def check_price(soup):
    check_price = soup.find('span', class_="price_item", itemprop='price')
    if check_price is not None:
        price = int(check_price.text.strip())
    else:
        price = 0
    check_currency = soup.find('span', class_='currency')
    if check_currency is None:
        currency = None
    else:
        currency = check_currency.text
    return {
        'cost': price,
        'currency': currency
    }


def name_of_product(soup):
    check_name = soup.find('span', class_='product-item__name')
    name = check_name.text
    return name


def stars_rating(soup):
    stars_rating = soup.find('span', class_='star-list')
    stars = stars_rating.text
    return {
        'stars': stars.strip(),
        'count': len(stars.strip())
    }


def categories(soup):
    check_categories = soup.find('div', class_='bread-crumbs')
    categories = check_categories.text.strip().replace('\n\n\n\n\n\n', '>')
    return categories



def check_numbers_of_reviews(soup):
    check_numbers_of_reviews = soup.find('span', class_='rating', itemprop='aggregateRating')
    reviews = check_numbers_of_reviews.text.strip()
    return reviews


def check_description(soup):
    check_description = soup.find('div', itemprop="description")
    description = check_description.text.strip()
    return description


def check_country(soup):
    check_country = soup.find('div', class_='product-item__text')
    country = check_country.text.split('Сделано в:')[1].split('Объем:')[0].strip()
    return country


def check_first_5_reviews(soup):
    comments_list = []
    check_reviews = soup.find('ul', class_='comments-list')
    comments = check_reviews.find_all('li')[:5]
    for comment in comments:
        name = comment.find('span', class_='review-author-name', itemprop='author').text
        date = comment.find('time', class_='comment__time')['datetime']
        text_of_comment = comment.find('p', itemprop='reviewBody').text
        mark = comment.find('span', class_='star-list').text
        comments_dict = {
            'name': name,
            'date': date,
            'text': text_of_comment,
            'stars': {
                'stars': mark.strip(),
                'count': len(mark.strip())
            }
        }
        comments_list.append(comments_dict)
    return comments_list


def scrap_item_from_makeup(link: object) -> object:
    item_info = {}
    response = requests.get(link).text
    soup = BeautifulSoup(response, 'lxml')

    item_info['availability'] = get_availability_of_goods(soup=soup)
    item_info['name_of_product'] = name_of_product(soup=soup)
    item_info['stars_rating'] = stars_rating(soup=soup)
    item_info['categories'] = categories(soup=soup)
    item_info['price'] = check_price(soup=soup)
    item_info['check_numbers_of_reviews'] = check_numbers_of_reviews(soup=soup)
    item_info['description'] = check_description(soup=soup)
    item_info['country'] = check_country(soup=soup)
    item_info['check_first_5_reviews'] = check_numbers_of_reviews(soup=soup)
    return item_info


if __name__ == '__main__':
    print(scrap_item_from_makeup('https://makeup.com.ua/product/977131/'))