import pytest
import requests
from seleniumbase import BaseCase

from qa327_test.conftest import base_url

@pytest.mark.usefixtures('server')
class BadRegisterTests(BaseCase):
    def test_bad_password1(self):
        self.open(base_url + '/register')
        self.type("#email", "bad@test.com")
        self.type("#name", "bad")
        self.type("#password", "xd")
        self.type("#password2", "xd")
        self.click('input[type="submit"]')
        self.assert_element("#login_msg")
        self.assert_text("Password length must be greator then 6.", "#login_msg")

    def test_bad_password2(self):
        self.open(base_url + '/register')
        self.type("#email", "bad@test.com")
        self.type("#name", "bad")
        self.type("#password", "1234567")
        self.type("#password2", "1234567")
        self.click('input[type="submit"]')
        self.assert_element("#login_msg")
        self.assert_text(
            "You password must meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character (@$!%*?&)",
            "#login_msg")

    def test_bad_email(self):
        self.open(base_url + '/register')
        self.type("#email", "bademail")
        self.type("#name", "pytest")
        self.type("#password", "PYTESTpassword!")
        self.type("#password2", "PYTESTpassword!")
        self.click('input[type="submit"]')
        self.assert_element("#login_msg")
        self.assert_text("Invalid Email.", "#login_msg")

    def test_duplicate_email(self):
        self.open(base_url + '/register')
        self.type("#email", "pytest@test.com")
        self.type("#name", "pybad")
        self.type("#password", "NEWpassword@")
        self.type("#password2", "NEWpassword@")
        self.click('input[type="submit"]')
        self.assert_element("#login_msg")
        self.assert_text("This email is already in use.", "#login_msg")
        