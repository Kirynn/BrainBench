import pytest
from qa327.backend import validate_password



"""
Test validation of passwords
(I know I Don't need '== True' or '== False', its for clear definitions of tests
"""
class TestPassword(object):

    def test_valid_password(self):

        assert validate_password('Tester!')['state'] == True
        assert validate_password('ThisIsValid!')['state'] == True
        assert validate_password('!testTT')['state'] == True
        assert validate_password('!testT')['state'] == True         # Smallest case
        assert validate_password('pleaS@acceptme')['state'] == True
        assert validate_password('uhohSpaceatStart*')['state'] == True

    def test_invalid_password(self):
 
        assert validate_password('thisisinvalid')['state'] == False
        assert validate_password('DoNotAcceptMe')['state'] == False
        assert validate_password('D_oNotAcceptMe')['state'] == False
        assert validate_password('!tetT')['state'] == False
        assert validate_password('')['state'] == False
        assert validate_password('This has spaces!')['state'] == False