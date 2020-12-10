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

    def test_nameAlphaNumeric_Positive(self): # Test case R4.1.1 
        """ /sell[POST] The name of the ticket is alphanumeric - positive """
        self.open(base_url + '/logout')
        self.login()
        self.open(base_url + '/sell')
        self.type("#ticket-name", "testing_name")
        self.assert_element_absent() #todo: make element ticketname_error

    def test_nameAlphaNumeric_Negative(self): # Test case R4.1.2 
        """ /sell[POST] The name of the ticket is alphanumeric - negative """
        self.open(base_url + '/logout')
        self.login()
        self.open(base_url + '/sell')
        self.type("#ticket-name", "testing_name")
        self.assert_element_absent() #todo: make element ticketname_error
    
    def test_nameLength_Postive(self): # Test case R4.2.1
        """ /sell[POST] The name of the ticket is no longer than 60 characters - positive"""
        self.open(base_url + '/logout')
        self.login()
        self.open(base_url + '/sell')
        self.type("#ticket-name", "testing_name")
        self.assert_element_absent() #todo: make element ticketname_error
        
    
    def test_nameLength_Negative(self): # Test case R4.1.2
        """ /sell[POST] The name of the ticket allows spaces only if it is not the first or the last character - negative """
        self.open(base_url + '/logout')
        self.login()
        self.open(base_url + '/sell')
        self.type("#ticket-name", "testing_name")
        self.assert_element_absent() #todo: make element ticketname_error
        
    
    def test_quantityZero_Positive(self): # Test case R4.3.1 
        """ /sell[POST] The quantity of the tickets has to be more than 0 - positive """
        self.open(base_url + '/logout')
        self.login()
        self.open(base_url + '/sell')
        self.type("#ticket-name", "testing_name")
        self.assert_element_absent() #todo: make element ticketname_error
        
    def test_quantityZero_Negative(self): # Test case R4.3.1
        """" /sell[POST] The quantity of the tickets has to be more than 0 - negative """
        self.open(base_url + '/logout')
        self.login()
        self.open(base_url + '/sell')
        self.type("#ticket-name", "testing_name")
        self.assert_element_absent() #todo: make element ticketname_error

    def test_sellnameNegative(self): # Test case R4.3.2
        """ /sell[POST] The quantity of the tickets has to be less than or equal to 100 - positive """
        self.open(base_url + '/logout')
        self.login()
        self.open(base_url + '/sell')
        self.type("#ticket-name", "testing_name")
        self.assert_element_absent() #todo: make element ticketname_error

    def test_sellnameNegative(self): # Test case R4.3.2
        """ /sell[POST] The quantity of the tickets has to be less than or equal to 100 - negative """
        self.open(base_url + '/logout')
        self.login()
        self.open(base_url + '/sell')
        self.type("#ticket-name", "testing_name")
        self.assert_element_absent() #todo: make element ticketname_error

    def test_sellnameNegative(self): # Test case R4.4.1
        """ /sell[POST] Price has to be more than/equal to 10 - positive """
        self.open(base_url + '/logout')
        self.login()
        self.open(base_url + '/sell')
        self.type("#ticket-name", "testing_name")
        self.assert_element_absent() #todo: make element ticketname_error

    def test_sellnameNegative(self): # Test case R4.4.1
        """ /sell[POST] Price has to be more than/equal to 10 - negative """
        self.open(base_url + '/logout')
        self.login()
        self.open(base_url + '/sell')
        self.type("#ticket-name", "testing_name")
        self.assert_element_absent() #todo: make element ticketname_error

    def test_sellnameNegative(self): # Test case R4.4.2
        """ /sell[POST] Price has to be less/than equal to 100 - positive """
        self.open(base_url + '/logout')
        self.login()
        self.open(base_url + '/sell')
        self.type("#ticket-name", "testing_name")
        self.assert_element_absent() #todo: make element ticketname_error
    
    def test_sellnameNegative(self): # Test case R4.4.2
        """ /sell[POST] Price has to be less/than equal to 100 - negative """
    
    def test_sellnameNegative(self): # Test case R4.5.1
        """ /sell[POST] Date must be given in the format YYYYMMDD (e.g. 20200901) - positive """
    
    def test_sellnameNegative(self): # Test case R4.5.1 - /sell[POST] Date must be given in the format YYYYMMDD (e.g. 20200901) - negative  
        "FKSDLF"
    
    def test_sellnameNegative(self): # Test case R4.6.1 - For any errors, redirect back to / and show an error message
        "FKSDLF"
    
    def test_sellnameNegative(self): # Test case R4.7.1 - The added new ticket information will be posted on the user profile page - owner
        "FKSDLF"
    
    def test_sellnameNegative(self): # Test case R4.7.2 - The added new ticket information will be posted on the user profile page - name
        "FKSDLF"
    
    def test_sellnameNegative(self): # Test case R4.7.3 - The added new ticket information will be posted on the user profile page - quantity
        "FKSDLF"

    def test_sellnameNegative(self): # Test case R4.7.4 - The added new ticket information will be posted on the user profile page - price
        "FKSDLF"

    def test_sellnameNegative(self): # Test case R4.7.5 - The added new ticket information will be posted on the user profile page - date
        "FKSDLF"
    

