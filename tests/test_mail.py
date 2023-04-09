import logging
import unittest
from apps.mail.tasks import Mail

class TestMail(unittest.TestCase):
    def test_mail(self):
        m = Mail()
        m.send()


if __name__ == "__main__":
    unittest.main()

