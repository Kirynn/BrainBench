import pytest
import requests
from seleniumbase import BaseCase

from qa327_test.conftest import base_url

@pytest.mark.usefixtures('server')
class BadLoginTest(BaseCase):

    def test_bad_login(self):
        """ Checks if the login failed, if correct error message appears """
        self.open(base_url + '/login')
        self.type("#email", "badytest@test.com")
        self.type("#password", "FAILEDpassword!")
        self.click('input[type="submit"]')
        self.assert_element("#login_msg")
        self.assert_text("login failed", "#login_msg")