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
    def test_a1_login(self):

        """ This test checks standard login for the Swag Labs store. """        
        self.open(base_url + '/logout')
        self.register()
        self.login()
        self.open(base_url)

        self.assert_element("#welcome-header")
        self.assert_text("Welcome pytest", "#welcome-header")

    # All fields of ticket are valid
    def test_all_pos(self):

        self.open(base_url + '/logout')
        self.register()
        self.login()
        self.open(base_url)

        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "testingName")
        self.type("#sell-ticket-quantity", "10")
        self.type("#sell-ticket-price", "20")
        self.type("#sell-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#sell-ticket-button')
        
        self.assert_element("#testingName")

    # Field for name of ticket isn't alphanumeric
    def test_name_alpha_neg(self):

        self.open(base_url + '/logout')
        self.register()
        self.login()
        self.open(base_url)

        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "b@d!_nam3")
        self.type("#sell-ticket-quantity", "10")
        self.type("#sell-ticket-price", "20")
        self.type("#sell-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#sell-ticket-button')

        self.assert_element("#error_msg")
        self.assert_text("Name must be alphanumeric", "#error_msg")

    # Field for name of ticket is less than 6 characters
    def test_name_short(self):

        self.open(base_url + '/logout')
        self.register()
        self.login()
        self.open(base_url)

        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "small")
        self.type("#sell-ticket-quantity", "10")
        self.type("#sell-ticket-price", "20")
        self.type("#sell-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#sell-ticket-button')

        self.assert_element("#error_msg")
        self.assert_text("Name length must be between 6 and 60 characters", "#error_msg")

    # Field for name of ticket is more than 60 characters
    def test_name_long(self):

        self.open(base_url + '/logout')
        self.register()
        self.login()
        self.open(base_url)

        self.click("#btn-add-ticket")
        time.sleep(1)
        self.type("#sell-ticket-name", "verylongstringohmythisisanextemelywrongnameIwonderifievenspeltextremelycorrectly")
        self.type("#sell-ticket-quantity", "10")
        self.type("#sell-ticket-price", "20")
        self.type("#sell-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#sell-ticket-button')

        self.assert_element("#error_msg")
        self.assert_text("Name length must be between 6 and 60 characters", "#error_msg")

    # Field for quanity of ticket is less than 1
    def test_quantity_small(self):

        self.open(base_url + '/logout')
        self.register()
        self.login()
        self.open(base_url)

        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "testingName")
        self.type("#sell-ticket-quantity", "0")
        self.type("#sell-ticket-price", "20")
        self.type("#sell-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#sell-ticket-button')
        
        self.assert_element("#error_msg")
        self.assert_text("Please select 1 to 100 tickets", "#error_msg")
        
    # Field for quantity of ticket is more than 100
    def test_quantity_large(self):

        self.open(base_url + '/logout')
        self.register()
        self.login()
        self.open(base_url)

        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "testingName")
        self.type("#sell-ticket-quantity", "1000")
        self.type("#sell-ticket-price", "20")
        self.type("#sell-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#sell-ticket-button')
        
        self.assert_element("#error_msg")
        self.assert_text("Please select 1 to 100 tickets", "#error_msg")

    # Field for price of each ticket is less than 10
    def test_price_small(self):
        
        self.open(base_url + '/logout')
        self.register()
        self.login()
        self.open(base_url)

        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "testingName")
        self.type("#sell-ticket-quantity", "10")
        self.type("#sell-ticket-price", "5")
        self.type("#sell-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#sell-ticket-button')
        
        self.assert_element("#error_msg")
        self.assert_text("Please enter an amount between 10 and 100", "#error_msg")

    # Field for price of each ticket is more than 100
    def test_price_large(self):

        self.open(base_url + '/logout')
        self.register()
        self.login()
        self.open(base_url)

        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "testingName")
        self.type("#sell-ticket-quantity", "10")
        self.type("#sell-ticket-price", "9000")
        self.type("#sell-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#sell-ticket-button')
        
        self.assert_element("#error_msg")
        self.assert_text("Please enter an amount between 10 and 100", "#error_msg")

    # Field for date of ticket expiry is earlier than the current date
    def test_bad_date(self):

        self.open(base_url + '/logout')
        self.register()
        self.login()
        self.open(base_url)

        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "testingName")
        self.type("#sell-ticket-quantity", "10")
        self.type("#sell-ticket-price", "20")
        self.type("#sell-datetime", "1977/12/10")
        self.click('#sell-ticket-button')
        
        self.assert_element("#error_msg")
        self.assert_text("This ticket has expired", "#error_msg")

    # Makes two of the exact same tickets to see how duplicates are handled by the app
    def test_handles_duplicates(self):

        self.open(base_url + '/logout')
        self.register()
        self.login()
        self.open(base_url)

        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "testingName")
        self.type("#sell-ticket-quantity", "10")
        self.type("#sell-ticket-price", "20")
        self.type("#sell-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#sell-ticket-button')

        # Do it again for a duplicate ticket
        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "testingName")
        self.type("#sell-ticket-quantity", "10")
        self.type("#sell-ticket-price", "20")
        self.type("#sell-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#sell-ticket-button')

        self.assert_element("#error_msg")
        self.assert_text("There is a ticket already specified", "#error_msg")
