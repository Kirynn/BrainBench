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
class SimpleLoggingTests(BaseCase):

    def register(self):
        """register new user"""
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

    def test_loginCheck(self): #R1.1, R1.2
        """  If the user hasn't logged in, show the login page + current page has a message that says 'please login'"""
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.open(base_url)
        self.assert_element("#login-prompt")
        self.assert_text("Please Log In", "#login-prompt")


    def test_registerlogin(self):
        """ If the user has logged in, redirect to the user profile page 
        The login form can be submitted as a POST request to the current URL (/login) """
        self.register()
        self.login()
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "pytest@test.com")
        self.type("#password", "PYTESTpassword!")
        self.click('input[type="submit"]')
        self.open(base_url)
        self.assert_element("#welcome-header")
        self.assert_text("Welcome pytest!", "#welcome-header") #validate for R1.3 and R1.5


    def test_loginForm(self): #R1.4
        """ Check login form requests two fields (email + password)"""
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.assert_element("#email")
        self.assert_element("#password")

    def test_loginemailCheck(self): #R1.6.1
        """  Validate that the #email field takes the correct inputs - Cannot be empty """
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#password", "PYTESTpassword!")
        self.click('input[type="submit"]') #todo


    def test_passwordCheck(self): #R1.6.2 
        """ Validate that the #password field takes the correct inputs - Cannot be empty """
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "pytest@test.com")
        self.click('input[type="submit"]') #todo

    def test_passwordEmailCheck(self): #R1.6.3
        """ Validate that the #password and #email fields take the correct inputs - Both cannot be empty """
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        #todo

    def test_emailCheckNegErrCase(self): #R1.7.1 
        """ email field takes correct inputs - negative error case """
        self.register()
        self.login()
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "pytest@test.com")
        self.type("#password", "PYTESTpassword!")
        self.click('input[type="submit"]')
        self.open(base_url)
        self.assert_element("#welcome-header")

    def test_EmailCheckPosErrCase(self): #R1.7.2 
        """ email field takes correct inputs - positive error case """
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "testertest.com")
        self.type("#password", "PYTESTpassword!")
        self.click('input[type="submit"]')
        self.assert_text("login failed", "#login_msg")

    def test_passwordCheckNegErrCase(self): #R1.8.1 
        """ password field takes correct inputs - negative error case """
        self.register()
        self.login()
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "pytest@test.com")
        self.type("#password", "PYTESTpassword!")
        self.click('input[type="submit"]')
        self.open(base_url)
        self.assert_element("#welcome-header")

    def test_passwordCheckPosErrCase2(self): #R1.8.2
        """ password field takes correct inputs - positive error case - no capital """
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "pytest@test.com")
        self.type("#password", "pytestpassword!")
        self.click('input[type="submit"]')
        self.assert_text("login failed", "#login_msg")

    def test_passwordCheckPosErrCase3(self): #R1.8.3
        """ password field takes correct inputs - positive error case - no lowercase """
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "pytest@test.com")
        self.type("#password", "PYTESTPASSWORD!")
        self.click('input[type="submit"]')
        self.assert_text("login failed", "#login_msg")

    def test_passwordCheckPosErrCase4(self): #R1.8.4
        """ password field takes correct inputs - positive error case - < 6 letters """
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "pytest@test.com")
        self.type("#password", "test!")
        self.click('input[type="submit"]')
        self.assert_text("login failed", "#login_msg")

    def test_emailFormattingErrors(self): #R1.9.1
        """ For any formatting errors, render the login page and show the message 'email format is incorrect. """
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "pytesttest.com")
        self.type("#password", "P")
        self.click('input[type="submit"]')
        self.assert_text("login failed", "#login_msg")

    def test_loginFailed(self): #R1.9.1
        """ Otherwise, redict to /login and show message 'email/password combination incorrect. """
        self.register()
        self.login()
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "pytest@test.com")
        self.type("#password", "NOTPYTESTpassword!")
        self.click('input[type="submit"]')
        self.assert_text("login failed", "#login_msg")
        