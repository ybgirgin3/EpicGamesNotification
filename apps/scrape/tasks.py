# import csv
import pandas as pd
from dateutil import parser

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
    "Referrer-Policy": "no-referrer-when-downgrade"}

  def scrape(self) -> str:
    resp = requests.get(self.url, headers=self.headers).json()
    return _extract_to_memory(resp.get('data').get(
      'Catalog').get('searchStore').get('elements'))


def _extract_to_memory(data: list[dict]):
  san = [_sanitize_data(i) for i in data if _sanitize_data(i) is not None]
  df = pd.DataFrame.from_dict(san)
  df.columns = [k for k, v in san[0].items()]

  # df = df.reset_index(drop=True)

  return df.sort_values(by='free?')


def iso_to_string(date: str):
  date = parser.parse(date)
  return date.strftime('%m/%d/%Y, %H:%M:%S')


def _sanitize_data(data: dict):
  original_price = data.get('price', '<unknown_price>')\
    .get('totalPrice', '<unknown_price>')\
    .get('originalPrice', '<unknown_price>')

  discount_price = data.get('price', '<unknown_price>')\
                       .get('totalPrice', '<unknown_price>')\
                       .get('discount', '<unknown_price>')

  product_domain = 'https://store.epicgames.com/en-US/p'

  prom: dict = data.get('promotions', None)
  if prom is not None:
    prom2: list = prom.get('promotionalOffers', [])
    if not len(prom2):
      prom2: list = prom.get('upcomingPromotionalOffers', [])
    prom3: list = prom2[0].get('promotionalOffers', [])

    if prom and prom2 and prom3:  # if len prom is not 0 and len prom2 is not 0
      start_date = prom3[0].get('startDate', '<unknown-date>')
      end_date = prom3[0].get('endDate', '<unknown-date>')

    is_free = 'True' if original_price == discount_price else 'False'

    return {
      # 'id': data.get('id', '<unknown_id>'),
      'name': data.get('title', '<unknown_title>'),
      # 'namespace': data.get('namespace', '<unknown_namespace>'),
      # 'description': data.get('description', '<unknown_description>').replace('\n', ' '),
      'game_release_date': iso_to_string(data.get('effectiveDate', '<unknown_game_release_date>')),
      'offer_type': data.get('offerType', '<unknown_offer_type>'),
      'start_date': iso_to_string(start_date),
      'end_date': iso_to_string(end_date),
      'product_link': f'{product_domain}/{data.get("productSlug")}',
      'price': f'₺ {original_price/100}',
      'free?': is_free
    }
