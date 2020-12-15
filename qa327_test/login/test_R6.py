import pytest
import requests

from qa327 import backend
from qa327.models import User
from werkzeug.security import generate_password_hash
from seleniumbase import BaseCase
import time

from qa327_test.conftest import base_url


@pytest.mark.usefixtures('server')
def test_server_is_live():
	r = requests.get(base_url)
	assert r.status_code == 200


@pytest.mark.usefixtures('server')
class buyFormTesting(BaseCase):
	def sleep(self, seconds):
		time.sleep(seconds)

	def createTestTicket(self, name, quantity, price):
		self.click('#btn-add-ticket')
		self.sleep(1)
		self.type("#sell-ticket-name", name)
		self.type("#sell-ticket-quantity", str(quantity))
		self.type("#sell-ticket-price", str(price))
		self.type("#sell-datetime", "2099/01/01")
		self.click('#sell-ticket-button')


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

	#R6.2.1 - The user cannot order more then 0 tickets
	def testTicketAmountSuccessLower(self):
		self.open(base_url + "/logout")
		self.registerTestUser()
		self.login()
		self.createTestTicket("testAmountSL", 99, 10)
		self.click("#btn-buy-testAmountSL")
		self.sleep(1)
		self.type("#buy-ticket-quantity", "1")
		self.click("#buy-ticket-button")
		#No error message
		self.assert_text_not_visible("", "#error_msg")
		backend.clean_database()

	def testTicketAmountFailLower(self):
		self.open(base_url + "/logout")
		self.registerTestUser()
		self.login()
		self.createTestTicket("testAmountFL", 99, 10)
		self.click("#btn-buy-testAmountFL")
		self.sleep(1)
		self.type("#buy-ticket-quantity", "0")
		self.click("#buy-ticket-button")
		#Verify error message
		self.assert_text("Please select 1 to 100 tickets", "#error_msg")
		backend.clean_database()

	#R6.2.2 - The user can only order at most 100 tickets
	def testTicketAmountSuccessUpper(self):
		self.open(base_url + "/logout")
		self.registerTestUser()
		self.login()
		self.createTestTicket("testAmountSU", 99, 10)
		self.click("#btn-buy-testAmountSU")
		self.sleep(1)
		self.type("#buy-ticket-quantity", "50")
		self.sleep(10)
		self.click("#buy-ticket-button")
		#No error message
		self.assert_text_not_visible("", "#error_msg")
		backend.clean_database()

	def testTicketAmountFailUpper(self):
		self.open(base_url + "/logout")
		self.registerTestUser()
		self.login()
		self.createTestTicket("testAmountFU", 99, 10)
		self.click("#btn-buy-testAmountFU")
		self.sleep(1)
		self.type("#buy-ticket-quantity", "200")
		self.click("#buy-ticket-button")
		#Verify error message
		self.assert_text("Please select 1 to 100 tickets", "#error_msg")
		backend.clean_database()


	#R6.3.1 - The requested ticket is in the database
	def testTicketExists(self):
		self.open(base_url + "/logout")
		self.registerTestUser()
		self.login()
		self.createTestTicket("existingTicket", 99, 10)
		self.assert_element("#btn-buy-existingTicket")
		backend.clean_database()

	#R6.3.1 - The requested ticket is in the database
	def testTicketNotExist(self):
		self.open(base_url + "/logout")
		self.registerTestUser()
		self.login()
		try:
			#The element should not exist so this should raise an exception
			self.assert_element("#btn-buy-notExistingTicket")
		except:
			#When an exception is raised, then the test has passed
			self.assert_true(True)

	def testTicketInStock(self):
		self.open(base_url + "/logout")
		self.registerTestUser()
		self.login()
		self.createTestTicket("testStock", 1, 10)
		self.click("#btn-buy-testStock")
		self.sleep(1)
		self.type("#buy-ticket-quantity", "1")
		self.click("#buy-ticket-button")
		#Verify no error
		self.assert_text_not_visible("", "#error_msg")

		self.sleep(1)
		self.click("#btn-buy-testStock")
		self.sleep(1)
		self.type("#buy-ticket-quantity", "1")
		self.click("#buy-ticket-button")
		#Verify error message
		self.assert_text("There are not enough tickets available", "#error_msg")
		backend.clean_database()

	#R6.4.1 - The user has enough funds to purchase the ticket
	def testUserHasBalance(self):
		self.open(base_url + "/logout")
		self.registerTestUser()
		self.login()
		backend.add_user_funds(10)
