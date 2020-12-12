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
		self.assert_element_absent("#Error-funny")

	def testNot404OnLogin(self):
		self.open(base_url + '/login')
		self.assert_element_absent("#Error-funny")

	def testNot404OnRegister(self):
		self.open(base_url)
		self.assert_element_absent("#Error-funny")

	def testNot404OnLogout(self):
		self.open(base_url + '/logout')
		self.assert_element_absent("#Error-funny")

	def test404OnSell(self):
		assert str(self.get_link_status_code(base_url + "/sell")).startswith('40')

	def test404OnBuy(self):
		assert str(self.get_link_status_code(base_url + "/buy")).startswith('40')

	def test404OnUpdate(self):
		assert str(self.get_link_status_code(base_url + "/update")).startswith('40')

	def test404(self):
		self.open(base_url + "/asdf")
		self.assert_element("#Error-funny")
