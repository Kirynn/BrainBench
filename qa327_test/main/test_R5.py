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

    def create_ticket(self):
        """ All fields of ticket are valid. Creates a ticket """
        self.click("#btn-add-ticket")
        time.sleep(1)
        self.type("#sell-ticket-name", "testingName")
        self.type("#sell-ticket-quantity", "10")
        self.type("#sell-ticket-price", "20")
        self.type("#sell-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#sell-ticket-button')

    # Actual testing begins
    def test_check_login(self):
        """ This test checks standard login for the Swag Labs store. """        
        self.open(base_url + '/logout')
        self.register()
        self.login()
        self.open(base_url)

        self.assert_element("#welcome-header")
        self.assert_text("Welcome pytest", "#welcome-header")

    def test_name_alpha_neg(self): # Test case R5.1
        """ /update[POST] The name of the ticket is alphanumeric """
        self.open(base_url + '/logout')
        self.register()
        self.login()
        self.open(base_url)

        self.create_ticket()

        self.click("#btn-update-testingName")
        self.type("#update-ticket-name", "b@d!_nam3")
        self.type("#update-ticket-quantity", "10")
        self.type("#update-ticket-price", "20")
        self.type("#update-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#update-ticket-button')

        self.assert_element("#error_msg")
        self.assert_text("Name must be alphanumeric", "#error_msg")

    def test_name_short(self): # Test case R5.2.0
        """ /update[POST] The name of the ticket is no longer than 60 characters (more than 0) """
        self.open(base_url + '/logout')
        self.register()
        self.login()
        self.open(base_url)

        self.create_ticket()

        self.click("#btn-update-testingName")
        self.type("#update-ticket-name", "small")
        self.type("#update-ticket-quantity", "10")
        self.type("#update-ticket-price", "20")
        self.type("#update-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#update-ticket-button')

        self.assert_element("#error_msg")
        self.assert_text("Name length must be between 6 and 60 characters", "#error_msg")

    def test_name_long(self): # Test case R5.2.1
        """ /update[POST] The name of the ticket is no longer than 60 characters (less than 61) """
        self.open(base_url + '/logout')
        self.register()
        self.login()
        self.open(base_url)

        self.create_ticket()

        self.click("#btn-update-testingName")
        self.type("#update-ticket-name", "verylongstringohmythisisanextemelywrongnameIwonderifievenspeltextremelycorrectly")
        self.type("#update-ticket-quantity", "10")
        self.type("#update-ticket-price", "20")
        self.type("#update-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#update-ticket-button')

        self.assert_element("#error_msg")
        self.assert_text("Name length must be between 6 and 60 characters", "#error_msg")

    def test_quantity_small(self): # Test case R5.3.1
        """ /update[POST] The quantity of the tickets has to be more than 0 """
        self.open(base_url + '/logout')
        self.register()
        self.login()
        self.open(base_url)

        self.create_ticket()

        self.click("#btn-update-testingName")
        self.type("#update-ticket-name", "testingName")
        self.type("#update-ticket-quantity", "0")
        self.type("#update-ticket-price", "20")
        self.type("#update-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#update-ticket-button')
        
        self.assert_element("#error_msg")
        self.assert_text("Please select 1 to 100 tickets", "#error_msg")
        
    def test_quantity_large(self): # Test case R5.3.2
        """  /update[POST] The quantity of the tickets has to be less than or equal to 100 """
        self.open(base_url + '/logout')
        self.register()
        self.login()
        self.open(base_url)

        self.create_ticket()

        self.click("#btn-update-testingName")
        self.type("#update-ticket-name", "testingName")
        self.type("#update-ticket-quantity", "1000")
        self.type("#update-ticket-price", "20")
        self.type("#update-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#update-ticket-button')
        
        self.assert_element("#error_msg")
        self.assert_text("Please select 1 to 100 tickets", "#error_msg")

    def test_price_small(self): # Test case R5.4.1
        """ /update[POST] Price has to be more than/equal to 10 """
        self.open(base_url + '/logout')
        self.register()
        self.login()
        self.open(base_url)

        self.create_ticket()

        self.click("#btn-update-testingName")
        self.type("#update-ticket-name", "testingName")
        self.type("#update-ticket-quantity", "10")
        self.type("#update-ticket-price", "5")
        self.type("#update-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#update-ticket-button')
        
        self.assert_element("#error_msg")
        self.assert_text("Please enter an amount between 10 and 100", "#error_msg")

    def test_price_large(self): # Test case R5.4.2 
        """ /update[POST] Price has to be less/than equal to 100 """
        self.open(base_url + '/logout')
        self.register()
        self.login()
        self.open(base_url)

        self.create_ticket()

        self.click("#btn-update-testingName")
        self.type("#update-ticket-name", "testingName")
        self.type("#update-ticket-quantity", "10")
        self.type("#update-ticket-price", "9000")
        self.type("#update-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#update-ticket-button')
        
        self.assert_element("#error_msg")
        self.assert_text("Please enter an amount between 10 and 100", "#error_msg")

    def test_bad_date(self): # Test case R5.5.1
        """ /update[POST] Date must be given in the format YYYYMMDD (e.g. 20200901) """
        self.open(base_url + '/logout')
        self.register()
        self.login()
        self.open(base_url)

        self.create_ticket()

        self.click("#btn-update-testingName")
        self.type("#update-ticket-name", "testingName")
        self.type("#update-ticket-quantity", "10")
        self.type("#update-ticket-price", "20")
        self.type("#update-datetime", "1977/12/10")
        self.click('#update-ticket-button')
        
        self.assert_element("#error_msg")
        self.assert_text("This ticket has expired", "#error_msg")

    # Seperate function to test
    def test_handles_duplicates(self):

        self.open(base_url + '/logout')
        self.register()
        self.login()
        self.open(base_url)

        self.create_ticket()
        self.create_ticket()

        self.assert_element("#error_msg")
        self.assert_text("There is a ticket already specified", "#error_msg")
