import pytest
import requests
from seleniumbase import BaseCase

from datetime import date
import time

from qa327_test.conftest import base_url

@pytest.mark.usefixtures('server')
class CreatingTickets(BaseCase):
    
    # General functions
    def login(self):
        """ Login to Swag Labs and verify that login was successful. """
        self.open(base_url + '/login')
        self.type("#email", "pytest@test.com")
        self.type("#password", "PYTESTpassword!")
        self.click('input[type="submit"]')

    def register(self):
        """register new user"""
        self.open(base_url + '/register')
        self.type("#email", "pytest@test.com")
        self.type("#name", "pytest")
        self.type("#password", "PYTESTpassword!")
        self.type("#password2", "PYTESTpassword!")
        self.click('input[type="submit"]')

    # Actual testing begins
    def test_login(self):
        """ This test checks standard login for the Swag Labs store. """
        
        self.open(base_url + '/logout')
        self.register()
        self.login()
        self.open(base_url)
        self.assert_element("#welcome-header")
        self.assert_text("Welcome pytest", "#welcome-header")

    def test_name_pos(self):

        self.open(base_url + '/logout')
        self.register()
        self.login()
        self.open(base_url)
        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "testing name")
        self.type("#sell-ticket-quantity", 10)
        self.type("#sell-ticket-price", 20)
        self.type("#sell-datetime", date.today().strftime("%Y%m%d"))
        self.click('#sell-ticket-button')
        self.assert_element("#testing-name")

    def test_name_alpha_neg(self):

        self.open(base_url + '/logout')
        self.register()
        self.login()
        self.open(base_url)
        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "b@d!_nam3")
        self.type("#sell-ticket-quantity", 10)
        self.type("#sell-ticket-price", 20)
        self.type("#sell-datetime", date.today().strftime("%Y%m%d"))
        self.click('#sell-ticket-button')

        self.assert_text("Name must be alphanumeric", "#error_msg")


        



