import logging
import requests
from bs4 import BeautifulSoup


DOMAIN_URL = 'https://theminjoo.kr'
PEOPLE_TYPE = [
    # type_name, type_code, link_url
    ('중앙당', 1, '/connect/people/lists/1'),
    ('국회의원', 2, '/connect/people/lists/2'),
    ('시도당/지역구', 3, '/connect/people/lists/3'),
    ('지방자치단체', 4, '/connect/people/lists/4'),
]


def get_people(people_type: tuple) -> list:
    type_name, type_code, link_url = people_type
    r = requests.get(f"{DOMAIN_URL}{link_url}")
    # 정상 응답이 오지 않으면 AssertError 발생
    assert r.status_code == 200
    # logging.debug(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')
    # logging.debug(soup)
    for people in soup.find_all('a', 'clearfix'):
        # logging.debug(people)
        photo = f"{DOMAIN_URL}{people.find('span', 'lazy').get('data-bg')[4:-2]}"
        name = people.find('span', 'name').text.strip()
        area = people.find('span', 'area').text.strip()
        slogan = people.find('span', 'position').text.strip()

        logging.debug(f"{photo} / {name} / {area} / {slogan}")

        name = name.replace('>', '')
        logging.debug(' '.join(name.split()))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    try:
        for item in PEOPLE_TYPE:
            get_people(item)
    except AssertionError:
        logging.error(f"정치인 리스트 수집 실패: {item}")
