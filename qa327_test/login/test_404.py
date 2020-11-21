import pytest
import requests
from seleniumbase import BaseCase

from qa327_test.conftest import base_url


@pytest.mark.usefixtures('server')
def test_server_is_live():
	r = requests.get(base_url)
	assert r.status_code == 200

@pytest.mark.usefixtures('server')
class test404Page(BaseCase):

	def testNot404OnHomepage(self):
		self.open(base_url + '/')
		self.assert_no_404_errors()

	def testNot404OnLogin(self):
		self.open(base_url + '/login')
		self.assert_no_404_errors()

	def testNot404OnRegister(self):
		self.open(base_url + '/register')
		self.assert_no_404_errors()

	def testNot404OnLogout(self):
		self.open(base_url + '/logout')
		self.assert_no_404_errors()

	# These next tests will be changed once the appropriate pages are implemented
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