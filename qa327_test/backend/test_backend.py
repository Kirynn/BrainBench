import pytest
from qa327.backend import validate_password, validate_ticket_inputs
from qa327.models import User



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

    def test_validate_ticket_inputs(self):

        assert validate_ticket_inputs("Test Ticket", 11, "20990101", 50, User(balance=5000)) == None
        assert validate_ticket_inputs("TestTicket!", 11, "20990101", 50, User(balance=5000)) == "Name must be alphanumeric"
        assert validate_ticket_inputs("Test", 11, "20990101", 50, User(balance=5000)) == "Name length must be between 6 and 60 characters"
        assert validate_ticket_inputs("Test this really super long ticket name that violates rule 1 woohoo", 11, "20990101", 50, User(balance=5000)) == "Name length must be between 6 and 60 characters"
        assert validate_ticket_inputs("Test Ticket", 4, "20990101", 50, User(balance=5000)) == "Please enter an amount between 10 and 100"
        assert validate_ticket_inputs("Test Ticket", 11, "19990101", 50, User(balance=5000)) == "This ticket has expired"
        assert validate_ticket_inputs("Test Ticket", 11, "20990101", 50, User(balance=0)) == "You do not have enough funds to purchase this"
        assert validate_ticket_inputs("Test Ticket", 11, "20990101", 255, User(balance=5000)) == "Please select 1 to 100 tickets"
