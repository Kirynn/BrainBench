# Whitebox Testing of `validate_ticket_inputs`
---

Type of whitebox testing used: 

```python
    def validate_ticket_inputs(name, price, day, amount, user):

1      if not bool(re.search(r'^[A-Za-z0-9 ]*$', name):
          return "Name must be alphanumeric"

2      if (6 > len(name) > 60):
          return "Name length must be between 6 and 60 characters"

3      if not (price in range(10, 101)):
          return "Please enter an amount between 10 and 100"

4      if datetime.strptime(day, '%Y%m%d').date() < date.today():
          return "This ticket has expired"

5      if user.balance < price:
         return "You do not have enough funds to purchase this"

6      if not (amount in range(1, 101)):
          return "Please select 1 to 100 tickets"

       return None
```

|Decision|Branch|Name Input|Price Input|Day Input|Amount Input|User.balance Input|Test Number|
|---|---|---|---|---|---|---|---|
|1|TRUE|"Test Ticket"|11|"20990101"|50|5000|1|
|1|FALSE|"TestTicket!"|11|"20990101"|50|5000|2|
|2|TRUE|"Test Ticket"|11|"20990101"|50|5000|1|
|2|FALSE|"Test"|11|"20990101"|50|5000|3|
|2|FALSE|"Test this really super long ticket name that violates rule 1 woohoo"|11|"20990101"|50|5000|3|
|3|TRUE|"Test Ticket"|11|"20990101"|50|5000|1|
|3|FALSE|"Test Ticket"|4|"20990101"|50|5000|4|
|3|FALSE|"Test Ticket"|999|"20990101"|50|5000|4|
|4|TRUE|"Test Ticket"|11|"20990101"|50|5000|1|
|4|FALSE|"Test Ticket"|11|"19990101"|50|5000|5|
|5|TRUE|"Test Ticket"|11|"20990101"|50|5000|1|
|5|FALSE|"Test Ticket"|11|"20990101"|50|5000|6|
|6|TRUE|"Test Ticket"|11|"20990101"|50|5000|1|
|6|FALSE|"Test Ticket"|11|"20990101"|50|0|7|
|6|FALSE|"Test Ticket"|11|"20990101"|50|999|7|
|7|TRUE|"Test Ticket"|11|"20990101"|0|5000|1|
|7|FALSE|"Test Ticket"|11|"20990101"|255|5000|8|
