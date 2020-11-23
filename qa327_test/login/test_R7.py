import pytest
import requests

from qa327 import backend
from qa327.models import User
from werkzeug.security import generate_password_hash
from seleniumbase import BaseCase

from qa327_test.conftest import base_url


@pytest.mark.usefixtures('server')
def test_server_is_live():
    r = requests.get(base_url)
    assert r.status_code == 200


@pytest.mark.usefixtures('server')
class redirectLoginTests(BaseCase):

    def test_loginredirect(self): #R7.1
        """  Test logged out redirect on / """
        self.open(base_url + '/logout')
        self.open(base_url + '/')
        self.open(base_url)
        self.assert_element("#login-prompt")

    def test_selllogin(self): #R7.2
        """ Test logged out redirect on /sell """
        self.open(base_url + '/logout')
        self.open(base_url + '/sell')
        self.open(base_url)
        self.assert_element("#login-prompt")

    def test_updatelogin(self): #R7.3
        """ Test logged out redirect on /update """
        self.open(base_url + '/logout')
        self.open(base_url + '/update')
        self.open(base_url)
        self.assert_element("#login-prompt")

    def test_buylogin(self): #R7.4
        """ Test logged out redirect on /buy """
        self.open(base_url + '/logout')
        self.open(base_url + '/buy')
        self.open(base_url)
        self.assert_element("#login-prompt")