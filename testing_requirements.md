# R4

Test Data:
```python
test_user = User(  
    email="tester@test.com,  
    name="tester",  
    password=generate_password_hash("test")
)

test_tickets = [
    {'name': 't1', 'price': '100'}
]

test_ticket = Ticket(
    owner='test_frontend@test.com',
    name='test_ticket_yo',
    quantity=10,
    price=10,
    date='20200901'
)
```

## Test case R4.1 - /sell[post] The name of the ticket is alphanumeric-only, and space allowed only if it is not the first or the last character - positive
Mocking:
* Mock backend.get_user to return a test_user instance
* Mock backend.get_ticket to return a test_ticket instance

Actions:
* open /logout (to invalidate any logged-in sessions that may exist)
* open /login
* enter test_user's email into element #email
* enter test_user's password into element #password
* click element input[type="submit"]
* open /
* enter test_ticket's name into element `#sell_name`
* enter test_ticket's quantity into element `#sell_quantity`
* click element `#sell_submit`
* validate that the `#sell_message` element shows `successful`
* open /logout (clean up)

#
#
## Test case R4.1 - /sell[post] The name of the ticket is alphanumeric-only, and space allowed only if it is not the first or the last character - negative

Mocking:
* Mock backend.get_user to return a test_user instance
* Mock backend.get_all_tickets to return a test_ticket instance

Actions:
* open /logout (to invalidate any logged-in sessions that may exist)
* open /login
* enter test_user's email into element #email
* enter test_user's password into element #password
* click element input[type="submit"]
* open /
* 
* 
* 
* 
* 
#
#

## Test case R4.2 - /sell[post] The name of the ticket is no longer than 60 characters - positive
Mocking:
* item1

Actions:
* item1

#
#
## Test case R4.2 - /sell[post] The name of the ticket is no longer than 60 characters - negative
Mocking:
* item1

Actions:
* item1
#
#

## Test case R4.3 - /sell[post] The quantity of the tickets has to be more than 0, and less than or equal to 100 - positive
Mocking:
* item1

Actions:
* item1

#
#
## Test case R4.3 - /sell[post] The quantity of the tickets has to be more than 0, and less than or equal to 100 - negative
Mocking:
* item1

Actions:
* item1
#
#

## Test case R4.4 - /sell[post] Price has to be of range [10, 100] - positive
Mocking:
* item1

Actions:
* item1

#
#
## Test case R4.4 - /sell[post] Price has to be of range [10, 100] - negative
Mocking:
* item1

Actions:
* item1
#
#

## Test case R4.5 - /sell[post] Date must be given in the format YYYYMMDD (e.g. 20200901) - positive
Mocking:
* item1

Actions:
* item1

#
#
## Test case R4.5 - /sell[post] Date must be given in the format YYYYMMDD (e.g. 20200901) - negative
Mocking:
* item1

Actions:
* item1
#
#

## Test case R4.6 - For any errors, redirect back to / and show an error message
Mocking:
* item1

Actions:
* item1

## Test case R4.7 - The added new ticket information will be posted on the user profile page
Mocking:
* item1

Actions:
* item1





| Specification | Test Case ID | Purpose |
|:-------------:|:------------:|:-------:|
|The name of the ticket is alphanumeric-only|R4.1.1|Check if the selling actions succeed when the ticket names is alphanumeric-only|
|The name of the ticket is alphanumeric-only|R4.1.2|Check if the selling actions fail when the ticket names contains special characters|
|Space allowed only if it is not the first or the last character|R4.1.3|Check if the selling actions succeed when the ticket names doesn't start or end with a space|
|Space allowed only if it is not the first or the last character|R4.1.4|Check if the selling actions fail when the ticket names doesn't start or end with a space|

