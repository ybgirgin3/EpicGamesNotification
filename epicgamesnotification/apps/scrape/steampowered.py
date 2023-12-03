import requests


class SteamPowered:
    base_url = 'https://store.steampowered.com/'
    # special_offer_url = 'https://store.steampowered.com/specials?snr=1_4_4_#tab=TopSellers'
    special_offers = 'facetedbrowse_FacetedBrowseItems_NO-IP'
    special_offer_url = 'https://store.steampowered.com/specials?flavor=contenthub_all&offset=62'

    # def __init__(self) -> None:
    #     pass
    def scrape(self):
        return requests.get(self.special_offer_url)



