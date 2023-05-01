import rumps
from apps.scrape.tasks import Scraper
from apps.mail.tasks import Mail


class EpicGamesReminder(rumps.App):
  scraper = Scraper()
  mail = Mail()

  # def __init__(self):
  #super(EpicGamesReminder, self).__init__('EGR')
  #self.menu = ['Get Free Games', 'Send Mail', 'Save Local']

  @rumps.clicked('Get Free Games')
  def get(self, sender):
    #ret = scraper.Scrape()
    # if self.send.sta
    # print(self.send(sender))
    if app.menu['Send Mail'].state:
      print('send mail yes')
    else:
      print('send mail no')

  @rumps.clicked('Send Mail')
  def send(self, sender):
    sender.state = not sender.state
    print('send clicked')

  @rumps.clicked('Save Local')
  def save(self, sender):
    sender.state = not sender.state
    print('save local clicked')


app = rumps.App('EGR', menu=['Get Free Games', 'Send Mail', 'Save Local'])
app.run()
