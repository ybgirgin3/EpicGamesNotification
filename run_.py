from epicgamesnotification.apps.scrape.steampowered import SteamPowered


s = SteamPowered()
ret = s.scrape()
ret = ret.content.decode('utf-8')
print('steam ret:', ret, type(ret))
with open('steam.offers.html', 'w') as f:
    f.write(ret)
