
##R3
**Test case R3.1 - If the user is not logged in, redirect to login page**
```
#No data necessary
```
Mocking:
* No data necessary

Actions:
* Open /logout to make sure user is logged out
* Open /
* Check to see if page is /login

**Test case R3.2 - This page shows a header 'Hi {}'.format(user.name)**
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
```
Mocking:
* Mock backend.get_user to return a test_user instance

Actions:
* open /logout (to invalidate any logged-in sessions that may exist)
* open /login
* enter test_user's email into element #email
* enter test_user's password into element #password
* click element input[type="submit"]
* open /login again
* validate that #welcome-header element contains "test_frontend"

**Test case R3.3 - This page shows user balance.**
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
    balance=12.34
)
```
Mocking:
* Mock backend.get_user to return a test_user instance

Actions:
* open /logout (to invalidate any logged-in sessions that may exist)
* open /login
* enter test_user's email into element #email
* enter test_user's password into element #password
* click element input[type="submit"]
* open /login again
* check that #balance contains "$12.34"

**Test case R3.4 - This page shows a logout link, pointing to /logout**
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
```
Mocking:
* Mock backend.get_user to return a test_user instance

Actions:
* open /logout (to invalidate any logged-in sessions that may exist)
* open /login
* enter test_user's email into element #email
* enter test_user's password into element #password
* click element input[type="submit"]
* open /login again
* Validate that class "col-lg-8" contains a link named "logout"

**Test case R3.5 - This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired.**
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)

test_ticket = Ticket(
    owner='test_frontend@test.com',
    name='test_ticket_yo',
    quantity=10,
    price=10,
    date='20200901'
)
```
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
* validate that a ticket is listed with the same data as test_ticket

**Test case R3.6 - This page contains a form that a user can submit new tickets for sell. Fields: name, quantity, price, expiration date**
```
test_ticket = Ticket(
    owner='test_frontend@test.com',
    name='test_ticket_yo',
    quantity=10,
    price=10,
    date='20200901'
)
```
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
* enter test_ticket's name into element #name
* enter test_ticket's quantity into element #quantity
* enter test_ticket's price into element #price
* enter test_ticket's date into element #expiration
* * click element input[type="submit"]

**Test case R3.7 - This page contains a form that a user can buy new tickets. Fields: name, quantity**
```
```
Mocking:
* 

Actions:
*

**Test case R3.8 - This page contains a form that a user can update existing tickets. Fields: name, quantity, price, expiration date**
```
```
Mocking:
* 

Actions:
*

**Test case R3.9 - The ticket-selling form can be posted to /sell**
```
```
Mocking:
* 

Actions:
*

**Test case R3.10 - The ticket-buying form can be posted to /buy**
```
```
Mocking:
* 

Actions:
*

**Test case R3.11 - The ticket-update form can be posted to /update**
```
```
Mocking:
* 

Actions:
*