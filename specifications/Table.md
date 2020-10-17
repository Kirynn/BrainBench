|Specification|Test Case ID|Purpose|
|:-:|:-:|:-:|
|If the user has logged in, redirect back to the user profile page /|R2.1.1|Make sure the user can see their profile page|
|If the user is not logged in, show the user registration page with the correct fields|R2.1.2|Check to make sure the user can see the register|
|The registration can be submitted as a POST request to /register|R2.2.3|Check to see that the user's request to make an account is recieved by the backend|
|Validate the registration page has a email field|R2.3.1|Check that the user has somewhere to enter their email|
|Validate the registration page has a `#password` field|R2.3.2|Make sure the user has somewhere to enter their password|
|Validate the registration page has a `#password2` field|R2.3.3|Make sure the user has a field to double check their password|
|Validate that the /register page contains a `#name` field|R.3.4|Make sure the user has a field to enter their name|
|Validate the registration page `#email` field accepts valid inputs|R4.4.1|Check to make sure the user can only enter valid emails|
|Validate that an email is not in use|R2.4.2|Make sure the user has not already created an account|
|Validate that the field `#password` acceps valid inputs|R2.4.3|Make sure the user enters a password that is: minimum length 6, at least one upper case, at least one lower case, and at least one special character|
|Validate that the field `#password2` accepts valid inputs|R2.4.4|Make sure their second password is: minimum length 6, at least one upper case, at least one lower case, and at least one special character|
|Validate that the `#password` and `#password2` fields recieve a matching input|R2.4.5|Check that the registration will procede if and only if the two passwords enter match|
|Validate that the `#name` field takes the correct input|R2.4.6|Make sure only alphanumeric names are allowed with spaces not allowed at the beginning or end and is at least length 2 and at most 20 characters|
|Validate that a user is created properly|R2.5.1|Validate that a user when created is created in the backend with the correct parameters|
||
|The name of the ticket must be alphanumeric|R6.1.1|Ensure the the user can only enter ticket names that are alphanumeric|
|The name of the ticket may not have a space at the start or end|R6.1.2|Make sure there are no spaces at the start or the end of the entered ticket name|
|The name of the ticket may not be longer then 60 characters|R6.1.3|Check to make sure the ticket named entered is less then 61 characters.|
|The user cannot orders more then 0 tickets|R6.2.1|Check to make sure a user cannot order 0 tickets|
|The user can only order at most 100 tickets|R6.2.2|Check to make sure a user cannot more then 100 tickets.|
|The requested ticket is in the database|R6.3.1|Check to make sure the database contains the ticket that the user is looking for|
|The requested ticket has enough stock|R6.3.2|Check to make sure the user cannot order more tickets then there are available|
|The user has enough funds to purchase the ticket|R.6.4.1|Check to make sure the user cannot order more tickets then they can afford|
||