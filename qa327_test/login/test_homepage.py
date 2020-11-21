import pytest
import requests
from seleniumbase import BaseCase

from qa327_test.conftest import base_url


@pytest.mark.usefixtures('server')
def test_server_is_live():
	r = requests.get(base_url)
	assert r.status_code == 200

@pytest.mark.usefixtures('server')
class homepageTest(BaseCase):

	def testLogoutRedirect(self):
		self.open(base_url + "/logout")
		self.open(base_url + "/")
		self.assert_equal(self.get_current_url(), base_url + "/login")

	def registerTestUser(self):
		"""register new user"""
		self.open(base_url + '/register')
		self.type("#email", "test_frontend@test.com")
		self.type("#name", "test_frontend")
		self.type("#password", "Test_frontend!")
		self.type("#password2", "Test_frontend!")
		self.click('input[type="submit"]')

	def login(self):
		self.open(base_url + '/login')
		self.type("#email", "test_frontend@test.com")
		self.type("#password", "Test_frontend!")
		self.click('input[type="submit"]')

	def testPageHeader(self):
		self.open(base_url + "/logout")
		self.registerTestUser()
		self.login()
		self.open(base_url + '/')
		self.assert_element('#welcome-header')
		self.assert_text('Welcome test_frontend!', '#welcome-header')

	''' THIS ISN'T IMPLEMENTED YET
	def testUserBalance(self):
		self.open(base_url + '/logout')
		self.login()
		self.assert_element('#balance')
		self.assert_text('$0.00', '#balance')
	'''

	def testLogoutButtonExists(self):
		self.open(base_url + '/logout')
		self.login()
		self.assert_element("#logout-button")

	def testNewTicketSubmission(self):
		self.open(base_url + '/logout')
		self.login()
		self.click('#btn-add-ticket')
		self.type("#add-ticket-name", "test_ticket_2")
		self.type("#add-ticket-quantity", "20")
		self.type("#add-ticket-price", "20")
		self.type("#add-ticket-expiry", "20")
		self.type("#submit-datetime", "01/01/2099")
		self.click('#submit-ticket-button')

	def testBuyNewTicket(self):
		self.open(base_url + '/logout')
		self.login()
		self.click('#btn-buy-test')
		self.type("#buy-ticket-name", "test_frontend")
		self.type("#buy-ticket-quan", "1")
		self.click("buy-ticket-button")

	def testUpdateExistingTicket(self):
		self.open(base_url + '/logout')
		self.login()
		self.click('#btn-update-test 2')
		self.type("#add-ticket-name", "test_ticket_2")
		self.type("#add-ticket-quantity", "20")
		self.type("#add-ticket-price", "20")
		self.type("#add-ticket-expiry", "20")
		self.type("#submit-datetime", "01/01/2099")
		self.click('#submit-ticket-button')

	#These next tests will be changed once the appropriate pages are implemented
	def testSellPost(self):
		self.open(base_url + "/sell")
		status = self.get_link_status_code(self.get_current_url())
		self.assert_equal(status, "404")

	def testBuyPost(self):
		self.open(base_url + "/buy")
		status = self.get_link_status_code(self.get_current_url())
		self.assert_equal(status, "404")

	def testUpdatePost(self):
		self.open(base_url + "/update")
		status = self.get_link_status_code(self.get_current_url())
		self.assert_equal(status, "404")