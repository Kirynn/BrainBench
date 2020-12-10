import pytest
import requests
from seleniumbase import BaseCase
import time

from qa327_test.conftest import base_url


@pytest.mark.usefixtures('server')
def test_server_is_live():
	r = requests.get(base_url)
	assert r.status_code == 200

@pytest.mark.usefixtures('server')
class homepageTest(BaseCase):
	
	def sleep(self, seconds):
		time.sleep(seconds)

	def testLogoutRedirect(self):
		self.open(base_url + "/logout")
		self.open(base_url + "/")
		self.assert_equal(self.get_current_url(), base_url + "/login")

	def registerTestUser(self):
		"""register new user"""
		self.open(base_url + '/register')
		self.type("#email", "test_frontend@test.com")
		self.type("#name", "testFrontend")
		self.type("#password", "TestFrontend!")
		self.type("#password2", "TestFrontend!")
		self.click('input[type="submit"]')

	def login(self):
		self.open(base_url + '/login')
		self.type("#email", "test_frontend@test.com")
		self.type("#password", "TestFrontend!")
		self.click('input[type="submit"]')

	def testPageHeader(self):
		self.open(base_url + "/logout")
		self.registerTestUser()
		self.login()
		self.open(base_url + '/')
		self.assert_element('#welcome-header')
		self.assert_text('Welcome testfrontend!', '#welcome-header')

	def testUserBalance(self):
		self.open(base_url + '/logout')
		self.registerTestUser()
		self.login()
		self.assert_element('#balance')

	def testTicket(self):
		#Testing new ticket submission
		self.open(base_url + '/logout')
		self.registerTestUser()
		self.login()
		self.click('#btn-add-ticket')
		self.sleep(1)
		self.type("#sell-ticket-name", "testTicket")
		self.type("#sell-ticket-quantity", 10)
		self.type("#sell-ticket-price", 20)
		self.type("#sell-datetime", "2099/01/01")
		self.click('#sell-ticket-button')

		self.sleep(1)

		#Testing updating new ticket
		self.click('#btn-update-testTicket')
		self.sleep(1)
		self.type("#update-ticket-name", "testTicketUpdated")
		self.type("#update-ticket-quantity", 15)
		self.type("#update-ticket-price", 25)
		self.type("#update-datetime", "2099/01/01")
		self.click('#update-ticket-button')

		self.sleep(1)

		#Testing purchasing of ticket
		self.click('#btn-buy-testTicketUpdated')
		self.sleep(1)
		self.type("#buy-ticket-quantity", 10)
		self.click("#buy-ticket-button")

	def testLogoutButtonExists(self):
		self.open(base_url + '/logout')
		self.registerTestUser()
		self.login()
		self.assert_element("#logout-button")

	#These next tests will be changed once the appropriate pages are implemented
	def testPost(self):
		#Test for post on add ticket
		self.open(base_url + '/logout')
		self.registerTestUser()
		self.login()
		self.click('#btn-add-ticket')
		self.sleep(1)
		self.type("#sell-ticket-name", "postTicket")
		self.type("#sell-ticket-quantity", 10)
		self.type("#sell-ticket-price", 20)
		self.type("#sell-datetime", "2099/01/01")
		#Check for POST method in form
		sellFormMethod = self.get_attribute("#sell-ticket-form", "method")
		self.assert_equal(sellFormMethod, "post")
		self.click('#sell-ticket-button')

		self.sleep(1)

		#Test for post on update ticket
		self.click('#btn-update-postTicket')
		self.sleep(1)
		self.type("#update-ticket-name", "postTicket")
		self.type("#update-ticket-quantity", 15)
		self.type("#update-ticket-price", 25)
		self.type("#update-datetime", "2099/01/01")
		#Check for POST method in form
		updateFormMethod = self.get_attribute("#update-ticket-form", "method")
		self.assert_equal(updateFormMethod, "post")
		self.click('#update-ticket-button')

		self.sleep(1)

		#Test for post on buy ticket
		self.click('#btn-buy-postTicket')
		self.sleep(1)
		self.type("#buy-ticket-quantity", 10)
		#Check for POST method in form
		buyFormMethod = self.get_attribute("#buy-ticket-form", "method")
		self.assert_equal(buyFormMethod, "post")
		self.click("#buy-ticket-button")
