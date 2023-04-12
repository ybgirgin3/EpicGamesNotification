import csv
import logging

import requests


class Scraper:
    url = 'https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=TR&allowCountries=TR'
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "x-requested-with": "XMLHttpRequest",
        "Referer": "https://store.epicgames.com/en-US/free-games",
        "Referrer-Policy": "no-referrer-when-downgrade"
    }
    logging.debug(f'url: {url}, headers: {headers}')

    def scrape(self) -> dict:
        resp = requests.get(self.url, headers=self.headers).json()
        self.extract(resp.get('data').get('Catalog').get('searchStore').get('elements'))
        return resp

    def extract(self, data: list[dict]):
        _extract(data)


def _sanitize_data(data: dict):
    original_price = data.get('price', '<unknown_price>').get('totalPrice', '<unknown_price>').get('originalPrice',
                                                                                                   '<unknown_price>')
    discount_price = data.get('price', '<unknown_price>').get('totalPrice', '<unknown_price>').get('discount',
                                                                                                   '<unknown_price>')

    is_free = False
    prom: dict = data.get('promotions', None)
    if prom is not None:
        prom2: list = prom.get('promotionalOffers', [])
        if not len(prom2):
            prom2: list = prom.get('upcomingPromotionalOffers', [])
        prom3: list = prom2[0].get('promotionalOffers', [])

        if prom and prom2 and prom3:  # if len prom is not 0 and len prom2 is not 0
            start_date = prom3[0].get('startDate', '<unknown-date>')
            end_date = prom3[0].get('endDate', '<unknown-date>')

        return {
            'free?': 'True' if original_price == discount_price else 'False',
            'id': data.get('id', '<unknown_id>'),
            'name': data.get('title', '<unknown_title>'),
            'namespace': data.get('namespace', '<unknown_namespace>'),
            'description': data.get('description', '<unknown_description>').replace('\n', ' '),
            'game_release_date': data.get('effectiveDate', '<unknown_game_release_date>'),
            'offer_type': data.get('offerType', '<unknown_offer_type>'),
            'start_date': start_date,
            'end_date': end_date
        }


def _extract(data: list[dict]):
    """
    :param data:
    :return:
    """
    # ciktigi tarih: viewable data
    # promotionalOffers:
    csv_file = open('freegames.csv', 'w', newline='')
    csv_writer = csv.writer(csv_file)
    count = 0

    for each in data:
        if count == 0:
            _each = _sanitize_data(each)
            header = _each.keys()
            csv_writer.writerow(header)
            count += 1

        _each = _sanitize_data(each)
        if _each is not None:
            csv_writer.writerow(_each.values())

    csv_file.close()
