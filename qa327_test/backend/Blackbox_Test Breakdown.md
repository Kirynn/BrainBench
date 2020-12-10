# Test Breakdown for `validate_password`

## Acceptance Testing

### Valid Passwords Tested
* Tester!
* ThisIsValid!
* !testTT
* !testT                    *(This is smallest possible case)*

*Cases with one or more space(s) were omitted as they will never be given to `validate_password`. They are automatically handled striped when being passed to it.*

### Invliad Passwords Tested
* thisisinvalid
* DoNotAcceptMe
* D_oNotAcceptMe
* !test!
* (empty string)
