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

	''' THIS ISN'T IMPLEMENTED YET
	def testUserBalance(self):
		self.open(base_url + '/logout')
		self.registerTestUser()
		self.login()
		self.assert_element('#balance')
		self.assert_text('$0.00', '#balance')
	'''

	def testLogoutButtonExists(self):
		self.open(base_url + '/logout')
		self.registerTestUser()
		self.login()
		self.assert_element("#logout-button")

	def testNewTicketSubmission(self):
		self.open(base_url + '/logout')
		self.registerTestUser()
		self.login()
		self.click('#btn-add-ticket')
		self.type("#submit-ticket-name", "test_ticket_2")
		self.type("#submit-ticket-quantity", 10)
		self.type("#submit-ticket-price", 20)
		self.type("#submit-datetime", "01/01/2099")
		self.click('#submit-ticket-button')

	def testBuyNewTicket(self):
		self.open(base_url + '/logout')
		self.registerTestUser()
		self.login()
		self.click('#btn-buy-test')
		self.sleep(2)
		#self.type("#buy-ticket-name", "test_frontend")
		#self.click("#buy-ticket-quantity")
		self.type("#buy-ticket-quantity", 10)
		#self.click("#buy-ticket-name")
		self.click("#buy-ticket-button")

	def testUpdateExistingTicket(self):
		self.open(base_url + '/logout')
		self.registerTestUser()
		self.login()
		self.click('#btn-update-test')
		self.type("#submit-ticket-name", "test_ticket_2")
		self.type("#submit-ticket-quantity", 10)
		self.type("#submit-ticket-price", 20)
		self.type("#submit-datetime", "01/01/2099")
		self.click('#submit-ticket-button')

	#These next tests will be changed once the appropriate pages are implemented
	def testSellPost(self):
		self.open(base_url + "/sell")
		self.assert_element("#Error-funny")

	def testBuyPost(self):
		self.open(base_url + "/buy")
		self.assert_element("#Error-funny")

	def testUpdatePost(self):
		self.open(base_url + "/update")
		self.assert_element("#Error-funny")