from src.apps.mail.tasks import Mail


class _mail():
  def _mail(data):
    try:
      m = Mail()  # define mail
      m.send(data=data)  # send mail
      return True, 1
    except Exception as e:
      return False, e
