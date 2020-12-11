import pytest
import requests
import time

from qa327 import backend
from qa327.models import User
from werkzeug.security import generate_password_hash
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from datetime import date


@pytest.mark.usefixtures('server')
def test_server_is_live():
    r = requests.get(base_url)
    assert r.status_code == 200

@pytest.mark.usefixtures('server')
class Tests_R4(BaseCase):
    def register(self):
        """ Register new user"""
        self.open(base_url + '/register')
        self.type("#email", "pytest@test.com")
        self.type("#name", "pytest")
        self.type("#password", "PYTESTpassword!")
        self.type("#password2", "PYTESTpassword!")
        self.click('input[type="submit"]')

    def login(self):
        """ Login to Swag Labs and verify that login was successful. """
        self.open(base_url + '/login')
        self.type("#email", "pytest@test.com")
        self.type("#password", "PYTESTpassword!")
        self.click('input[type="submit"]')

    def refresh(self):
        backend.clean_database()
        self.open(base_url + '/logout')
        self.register()
        self.login()
        self.open(base_url)

    def test_nameAlphaNumeric_Positive(self): # Test case R4.1.1 
        """ /sell[POST] The name of the ticket is alphanumeric - positive case"""
        self.refresh()

        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "b@d!_nam3")
        self.type("#sell-ticket-quantity", "10")
        self.type("#sell-ticket-price", "20")
        self.type("#sell-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#sell-ticket-button')

        self.assert_element("#error_msg")
        self.assert_text("Name must be alphanumeric", "#error_msg")

    def test_nameAlphaNumeric_Negative(self): # Test case R4.1.1
        """ /sell[POST] The name of the ticket is alphanumeric - negative case"""
        self.refresh()

        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "validTicketName")
        self.type("#sell-ticket-quantity", "10")
        self.type("#sell-ticket-price", "20")
        self.type("#sell-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#sell-ticket-button')
        
        self.assert_text_not_visible("Name must be alphanumeric", "#error_msg")

    def test_nameSpace_Negative(self): # Test case R4.1.2
        """ /sell[POST] The name of the ticket allows spaces only if it is not the first or the last character - negative error case, .strip is used"""
        self.refresh()

        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "   validTicketName ")
        self.type("#sell-ticket-quantity", "10")
        self.type("#sell-ticket-price", "20")
        self.type("#sell-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#sell-ticket-button')
        
        self.assert_element("#validTicketName") #confirm name has been stripped and is availble for purchase
    
    def test_nameLength_Positive(self): # Test case R4.2.1
        """ /sell[POST] The name of the ticket is no longer than 60 characters - positive error case"""
        self.refresh()

        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "verylongstringohmythisisanextemelywrongnameIwonderifievenspeltextremelycorrectly")
        self.type("#sell-ticket-quantity", "10")
        self.type("#sell-ticket-price", "20")
        self.type("#sell-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#sell-ticket-button')
        
        self.assert_text("Name length must be between 6 and 60 characters", "#error_msg")
        
    def test_nameLength_Negative(self): # Test case R4.2.1
        """ /sell[POST] The name of the ticket is no longer than 60 characters - negative error case"""
        self.refresh()

        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "validName2")
        self.type("#sell-ticket-quantity", "10")
        self.type("#sell-ticket-price", "20")
        self.type("#sell-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#sell-ticket-button')
        
        self.assert_text_not_visible("Name length must be between 6 and 60 characters", "#error_msg")
    
    def test_quantityZero_Positive(self): # Test case R4.3.1 
        """ /sell[POST] The quantity of the tickets has to be more than 0 - positive error case"""
        self.refresh()
        self.sleep(2)

        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "validName")
        self.type("#sell-ticket-quantity", "0")
        self.type("#sell-ticket-price", "20")
        self.type("#sell-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#sell-ticket-button')
        
        self.assert_text("Please select 1 to 100 tickets", "#error_msg")
        
    def test_quantityZero_Negative(self): # Test case R4.3.1
        """" /sell[POST] The quantity of the tickets has to be more than 0 - negative error case"""
        self.refresh()
        

        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "validName")
        self.type("#sell-ticket-quantity", "1")
        self.type("#sell-ticket-price", "20")
        self.type("#sell-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#sell-ticket-button')
        
        self.assert_text_not_visible("Please select 1 to 100 tickets", "#error_msg")

    def test_quantityHundred_Positive(self): # Test case R4.3.2
        """ /sell[POST] The quantity of the tickets has to be less than or equal to 100 - positive error case"""
        self.refresh()
        self.sleep(2)

        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "validName")
        self.type("#sell-ticket-quantity", "101")
        self.type("#sell-ticket-price", "20")
        self.type("#sell-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#sell-ticket-button')
        
        self.assert_text("Please select 1 to 100 tickets", "#error_msg")

    def test_quantityHundred_Negative(self): # Test case R4.3.2
        """ /sell[POST] The quantity of the tickets has to be less than or equal to 100 - negative error case"""
        self.refresh()

        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "validName")
        self.type("#sell-ticket-quantity", "100")
        self.type("#sell-ticket-price", "20")
        self.type("#sell-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#sell-ticket-button')
        
        self.assert_text_not_visible("Please select 1 to 100 tickets", "#error_msg")

    def test_priceTen_Positive(self): # Test case R4.4.1
        """ /sell[POST] Price has to be more than/equal to 10 - positive error case"""
        self.refresh()

        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "validName")
        self.type("#sell-ticket-quantity", "10")
        self.type("#sell-ticket-price", "9")
        self.type("#sell-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#sell-ticket-button')
        
        self.assert_text("Please enter an amount between 10 and 100", "#error_msg")

    def test_priceTen_Negative(self): # Test case R4.4.1
        """ /sell[POST] Price has to be more than/equal to 10 - negative error case"""
        self.refresh()

        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "validName")
        self.type("#sell-ticket-quantity", "10")
        self.type("#sell-ticket-price", "10")
        self.type("#sell-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#sell-ticket-button')
        
        self.assert_text_not_visible("Please enter an amount between 10 and 100", "#error_msg")

    def test_priceHundred_Positive(self): # Test case R4.4.2
        """ /sell[POST] Price has to be less/than equal to 100 - positive error case"""
        self.refresh()

        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "validName")
        self.type("#sell-ticket-quantity", "10")
        self.type("#sell-ticket-price", "101")
        self.type("#sell-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#sell-ticket-button')
        
        self.assert_text("Please enter an amount between 10 and 100", "#error_msg")
    
    def test_priceHundred_Negative(self): # Test case R4.4.2
        """ /sell[POST] Price has to be less/than equal to 100 - negative error case"""
        self.refresh()

        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "validName")
        self.type("#sell-ticket-quantity", "10")
        self.type("#sell-ticket-price", "100")
        self.type("#sell-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#sell-ticket-button')
        
        self.assert_text_not_visible("Please enter an amount between 10 and 100", "#error_msg")
    
    def test_wrongDate_Positive(self): # Test case R4.5.1
        """ /sell[POST] Date must be after the current date YYYYMMDD (e.g. 20200901) - positive error case"""
        self.refresh()

        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "validName")
        self.type("#sell-ticket-quantity", "10")
        self.type("#sell-ticket-price", "100")
        self.type("#sell-datetime", "20200901")
        self.click('#sell-ticket-button')
        
        self.assert_text("This ticket has expired", "#error_msg")
    
    def test_wrongDate_Negative(self): # Test case R4.5.1 
        """ /sell[POST] Date must be given in the format YYYYMMDD (e.g. 20200901) - negative error case"""
        self.refresh()

        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "validName")
        self.type("#sell-ticket-quantity", "10")
        self.type("#sell-ticket-price", "100")
        self.type("#sell-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#sell-ticket-button')
        
        self.assert_text_not_visible("This ticket has expired", "#error_msg")
    
    def test_redirectConfirm(self): # Test case R4.6.1 
        """ For any errors, redirect back to / and show an error message """
        self.refresh()

        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "b@dn@m3")
        self.type("#sell-ticket-quantity", "10")
        self.type("#sell-ticket-price", "100")
        self.type("#sell-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#sell-ticket-button')
        
        assert str(self.get_link_status_code(base_url + "/"))
        self.assert_text("Name must be alphanumeric", "#error_msg")
    
    def test_ownerConfirm(self): # Test case R4.7.1 
        """ The added new ticket information will be posted on the user profile page - owner """
        self.refresh()

        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "validName")
        self.type("#sell-ticket-quantity", "10")
        self.type("#sell-ticket-price", "100")
        self.type("#sell-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#sell-ticket-button')
        self.assert_element("#btn-update-validName") #user will be able to see and update their own ticket confirmation
        

    def test_nameConfirm(self): # Test case R4.7.2 
        """ The added new ticket information will be posted on the user profile page - name """
        self.refresh()

        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "validName")
        self.type("#sell-ticket-quantity", "10")
        self.type("#sell-ticket-price", "100")
        self.type("#sell-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#sell-ticket-button')

        self.assert_element("#btn-update-validName") #user will be able to see and update their own ticket confirmation
    
    def test_quantityConfirm(self): # Test case R4.7.3
        """ The added new ticket information will be posted on the user profile page - quantity """
        self.refresh()

        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "validName")
        self.type("#sell-ticket-quantity", "10")
        self.type("#sell-ticket-price", "100")
        self.type("#sell-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#sell-ticket-button')
        self.assert_text_visible("10") 

    def test_priceConfirm(self): # Test case R4.7.4
        """ The added new ticket information will be posted on the user profile page - price """
        self.refresh()

        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "validName")
        self.type("#sell-ticket-quantity", "10")
        self.type("#sell-ticket-price", "100")
        self.type("#sell-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#sell-ticket-button')
        self.assert_text_visible("100.0")

    def test_dateConfirm(self): # Test case R4.7.5 
        """ The added new ticket information will be posted on the user profile page - date """
        self.refresh()

        self.click("#btn-add-ticket")
        self.type("#sell-ticket-name", "validName")
        self.type("#sell-ticket-quantity", "10")
        self.type("#sell-ticket-price", "100")
        self.type("#sell-datetime", date.today().strftime("%Y/%m/%d"))
        self.click('#sell-ticket-button')
        self.assert_text_visible(date.today().strftime("%Y%m%d")) 


