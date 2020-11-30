from qa327.models import db, User, Ticket, Order
from werkzeug.security import generate_password_hash, check_password_hash

from datetime import date, datetime
from typing import List, Union
import re

"""
This file defines all backend logic that interacts with database and other services
"""

def validate_email(email):

    # RFC 5322 specification: https://emailregex.com/
    regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return re.search(regex, email)

def validate_name(name):

    if 2 > len(name) > 20: return "Username must be between 2 and 20 characters."
    if not name.isalnum(): return "Name must be alphanumeric only."

    return None

def validate_password(password):

    pkg = {'state': True, 'msg': ''}

    regex = r"(^(?=.*[a-z])(?=.*[A-Z])(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$)"
    if len(password) < 6: 
        pkg['state'] = False
        pkg['msg'] = "Password length must be greator then 6."
    elif re.search(regex, password) == None:
        pkg['state'] = False
        pkg['msg'] = "You password must meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character (@$!%*?&)"

    return pkg

def get_user(email):
    """
    Get a user by a given email
    :param email: the email of the user
    :return: a user that has the matched email address
    """
    user = User.query.filter_by(email=email).first()
    return user


def login_user(email, password):
    """
    Check user authentication by comparing the password
    :param email: the email of the user
    :param password: the password input
    :return: the user if login succeeds
    :return: message "email/password combination incorrect" if login fails
    """
    # if this returns a user, then the name already exists in database

    email = email.strip()
    password = password.strip()

    user = get_user(email)
    if not user or not check_password_hash(user.password, password):
        return None
    return user


def register_user(email, name, password, password2):
    """
    Register the user to the database
    :param email: the email of the user
    :param name: the name of the user
    :param password: the password of user
    :param password2: another password input to make sure the input is correct
    :return: an error message if there is any, or None if register succeeds
    """
    email = email.strip()
    name = name.strip().lower()
    password = password.strip()
    password2 = password2.strip()

    user = User.query.filter_by(email=email).first()

    if user:
        return "This email is already in use."

    name_validation_error = validate_name(name)
    if not name_validation_error == None:
        return name_validation_error

    password_validation_error = validate_password(password)

    if not password_validation_error['state']:
        return password_validation_error['msg']

    if password != password2:
        return "The passwords do not match."

    if not validate_email(email):
        return 'Invalid Email.'

    hashed_pw = generate_password_hash(password, method='sha256')
    # store the encrypted password rather than the plain password
    new_user = User(email=email, name=name, password=hashed_pw, balance=5000)

    db.session.add(new_user)
    db.session.commit()
    return None


def create_ticket(name, quantity, price, date):
    ticket = Ticket.query.filter_by(name=name).first()

    if ticket:
        return "Ticket already exists"

    if not name.isalnum():
        return "Ticket name isn't alpha-numeric"

    if not (name[0] == " " or name[-1] == " "):
        return "Ticket starts or ends with a space"

    if len(name) > 60:
        return "Ticket name too long"

    if quantity < 1:
        return "Quantity of ticket must be more than 0"

    if quantity > 100:
        return "Quantity of ticket must be less than equal to 100"

    if price < 10:
        return "Price of ticket must be more than equal to 10"

    if price > 100:
        return "Price of ticket must be less than equal to 100"

    if len(date) != 8 or isinstance(date, str):
        return "Date must be given in the format YYYYMMDD"
    
    new_ticket = Ticket(name=name, quantity=quantity, price=price, date=date)

    db.session.add(new_ticket)
    db.session.commit()
    return None


def get_available_tickets(user : User = None) -> List[Ticket]:

    if (user):
        return Ticket.query.filter_by(creator=user.id)
    return Ticket.query.all()


def check_if_expired(ticket : Ticket) -> bool:

    return ticket.date <= date.today().strftime("%Y%m%d")

def validate_ticket_inputs(name, price, day, amount, user):

    day : str = day.replace("/", "")
    name : str = name.strip()
    price : int = int(price)
    amount : int = int(amount)

    if re.sub(r'[^A-Za-z0-9 ]+', '', name) == None:
        return "Name must be alphanumeric"

    if (6 > len(name) > 60):
        return "Name length must be between 6 and 60 characters"

    if (10 > price > 100):
        return "Please enter an amount between 10 and 100"

    if datetime.strptime(day, '%Y%m%d').date() < date.today():
        return "This ticket has expired"

    if user.balance < price:
        return "You do not have enough funds to purchase this"

    if 0 > amount > 100:
        return "Please select 1 to 100 tickets"

    return None

def buy_ticket(name : str, price : str, day : str, amount : str, user : User) -> Union[str, None]:


    errors = validate_ticket_inputs(name, price, day, amount, user)

    if (errors != None): return errors

    ticket = Ticket.query.filter_by(name=name).filter_by(date=day).first()

    if (ticket == None):
        return "The requested ticket was not found"

    if (ticket.quantity > amount):
        return "There are not enough tickets available"

    if (user.balance < price):
        return "You do not have enough money to purcahse the tickets"


    ticket.quantity -= amount
    user.balance -= price
    order = Order(user.id, ticket.id, amount)

    db.session.add(order)
    db.session.commit()

def sell_ticket(name : str, price : str, day : str, amount : str, user : User):

    errors = validate_ticket_inputs(name, price, day, amount, user)

    if (errors != None): return errors

    ticket = Ticket(name=name, price=float(price), date=day.replace("/", ""), creator=user.id, quantity=int(amount))

    db.seesion.add(ticket)
    db.session.commmit()

def update_ticket(name : str, price : str, day : str, amount : str, user : User):

    errors = validate_ticket_inputs(name, price, day, amount, user)

    if (errors != None): return errors

    ticket = Ticket.query.filter_by(name=name).filter_by(date=day).first()

    if (ticket == None):
        return "The requested ticket was not found"

    if (ticket.quantity > amount):
        return "There are not enough tickets available"

    if (user.balance < price):
        return "You do not have enough money to purcahse the tickets"

    ticket.name = name
    ticket.price = float(price)
    ticket.quantity = int(amount)
    ticket.date = day.replace("/", "")

    db.session.commit()
